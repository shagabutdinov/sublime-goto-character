import re
import sublime
import sublime_plugin
from Expression import expression

clean_required = False

class GotoCharacter(sublime_plugin.TextCommand):

  def run(self, edit, character, extend = None, delete = False,
    backward = False, line = False):

    if extend == None:
      extend = self.view.sel()[0].a != self.view.sel()[0].b

    options = {
      'extend': extend,
      'delete': delete,
      "backward": backward,
      'line': line,
    }

    self._move_to(edit, character, options)

  def _move_to(self, edit, character, options = {}):
    selections = []

    delete = options.get('delete', False)
    if delete:
      options['extend'] = True

    for sel in self.view.sel():
      start, end = self._move_cursor_to(edit, sel, character, options)
      if start == None:
        continue

      if delete:
        self.view.erase(edit, sublime.Region(start, end + 1))
      else:
        selections.append(sublime.Region(start, end))

    if delete or len(selections) == 0:
      return

    self.view.sel().clear()
    for region in selections:
      self.view.sel().add(region)

    if len(self.view.sel()) == 1:
      self.view.show(self.view.sel()[0].b)

  def _move_cursor_to(self, edit, sel, character, options):
    backward = options.get("backward", None)
    line = options.get('line', None)
    text = self.view.substr(sublime.Region(0, self.view.size()))

    start = sel.b

    match_options = {
      'backward': backward,
      'string': True,
      'nesting': True,
      'comment': True,
      'limit': 5
    }

    if backward:
      match_options['cursor'] = [1]

    matches = expression.find_matches(
      self.view,
      sel.b,
      '.(' + re.escape(character) + ')',
      match_options
    )

    if len(matches) == 0:
      return sel.a, sel.b

    self._highlight(matches)

    end = matches[0]
    start = end.start(1)
    if options.get('extend', None) and end != None:
      start = sel.a

    return start, end.start(1)

  def _highlight(self, matches):
    self.view.erase_regions('goto_character')
    regions = []
    for match in matches[1:]:
      regions.append(sublime.Region(match.end(0), match.end(0) - 1))

    draw = sublime.DRAW_EMPTY | sublime.DRAW_OUTLINED
    self.view.add_regions('goto_character', regions, 'string', '', draw)

    global clean_required
    clean_required = True

class GotoCharacterRegionsCLeaner(sublime_plugin.EventListener):
  def on_selection_modified_async(self, view):
    global clean_required
    if not clean_required:
      return

    last_command, _, _ = view.command_history(0)
    if last_command == 'goto_character':
      return

    clean_required = False
    view.erase_regions('goto_character')