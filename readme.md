# Sublime GotoCharacter plugin

Go to given character. Like f<character> in vim.


### Demo

![Demo](https://raw.github.com/shagabutdinov/sublime-goto-character/master/demo/demo.gif "Demo")


### Installation

This plugin is part of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
plugin set. You can install sublime-enhanced and this plugin will be installed
automatically.

If you would like to install this package separately check "Installing packages
separately" section of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
package.


### Features

1. Go to character forward/backward

2. Delete to character forward/backward

3. Select to character forward/backward

This plugin works especially good with [repeat command](http://github.com/shagabutdinov/sublime-repeat-command)
plugin to skip several characters at once.


### Usage

##### Go to character

  ```
  # before
  |string

  # after goto "g"
  strin|g
  ```

##### Select to character

  ```
  # before
  |string

  # after select to "g"
  {strin}g # selection
  ```

##### Delete to character

  ```
  # before
  |string

  # after delete to "g"
  |g
  ```

### Commands

| Description                  | Keyboard shortcut                      |
|------------------------------|----------------------------------------|
| Go to character              | alt+a, &lt;character&gt;               |
| Select to character          | alt+a, alt+s, &lt;character&gt;        |
| Delete to character          | alt+a, alt+d, &lt;character&gt;        |
| Go to character backward     | alt+a, alt+a, &lt;character&gt;        |
| Select to character backward | alt+a, alt+a, alt+s, &lt;character&gt; |
| Delete to character backward | alt+a, alt+a, alt+d, &lt;character&gt; |

### Todo

- Found character occurences highlighting