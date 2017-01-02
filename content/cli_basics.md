Title: Quick Guide to Command Line Basics
Date: 2016-12-09
Tags: cli, bash, zsh, cli
Category: tech
Slug: cli-basics
Summary: This is a quick overview of some command line basics as well as a few tips on how to make your experience more efficient (and cool)

<!-- for more detailed overview see command line tutorial -->

Before graphical user interfaces (GUI), drag and drop desktops, and voice activated assistances (e.g., Siri), the only way to interact with a computer was through written commands using the command line interface (CLI). Although you could be quite successful at using a computer without ever knowing what the CLI is, mastery of the CLI is that gateway to becoming a power user and unlocking the full potential of your computer. This is a quick overview of some command line basics as well as a few tips on how to make your experience more efficient (and cool).

# Terminal

To access the command line interface on macOS you need to open Terminal. It is located in `/Applications/Utilities/Terminal`; the easiest way to open it is to use spotlight (`⌘+space`) and simply type `terminal`.

An alternative to Terminal is [iTerm](https://www.iterm2.com). iTerm is a terminal emulator that can be used as a replacement for the native Terminal app. iTerm adds a host of new [features](https://www.iterm2.com/features.html) that provided much needed productivity boosters like autocompletion and split panes.

# Basic Commands

Below are a few basic commands that form the bedrock of command line interaction. If you ever have any questions about a command you come across [Explain Shell](http://explainshell.com) is an excellent resource as well as this [cheatsheet](https://github.com/0nn0/terminal-mac-cheatsheet).

Before we begin, here are a few tips:

* The term "directory" is just a way of referring to folders; "directory" is preferred on \*nix operating systems as opposed to "folder" on Windows (checkout [this](http://superuser.com/questions/169457/directory-vs-folder) for the super nerd answer)

* The action that a command performs can be modified using flags. These are typically a "-" followed by a single letter. For example, to list the visible AND the hidden the contents in a directory you would type the list command `ls` followed by the flag `-a`.

<!-- screenshots; tree -->

**Creating Files and Folders**

* `mkdir [dir_name]` make a directory

* `touch [file_name]` change file timestamps; easy way to create files

* `rm [file_name]` removes files (does not remove directories by default)
    * `-r [dir_name]` remove directories and their contents recursively

**Moving Around and Exploring the Computer**

* `cd` traverse the directory structure forward (i.e., open a directory)

* `../` traverse the directory structure backward (i.e., exit a directory)

* `ls` list contents of current directory
    * `-l` list detailed info such as permissions, owners, size, etc.
    * `-a` list all contents including hidden contents
    * `-S` sort
    * `Sr` reverse sort
* `cp [file] [path]` copy source file to a destination

* `mv` rename source to destination or move source to a directory; whereas `cp` duplicates the file, `mv` only keeps one copy (either with the new name or in the new location)

* `grep ["pattern"] [file_name]` print lines matching a pattern

* `find [file_name]` find a file

* `cat [file_name]` display contents of file

* `echo ["string"]` display a line of text

**Other Useful Commands**

* `sudo [command]` execute command as super user (requires password)

* `[command] | [command]` piping --- feed output of one command into the input of another command

* `echo ["string"] > [file_name]` overwrite file with string
    * `echo ["string"] >> [file_name]` append file with string

* Text editors
    * `nano [file_name]` a very simple text editor
    * `vim [file_name]` a more robust and extensible text editor
    * `emacs [file_name]` a more robust and extensible text editor

# Shells

While terminal is an application, the underlying software that you are using to do the command line interfacing is known as a shell. The default shell for macOS is Bash (Bourne Again Shell). Although Bash has stood the test of time, I currently using Zsh (pronounced Zee Shell) which provides useful features like command line completions, spell corrections, themeable prompts, etc.

<!-- ## Bash -->

## ZSH

The easiest way to get started with zsh is to install it using brew (checkout my other [post](timothykylethomas.me/package-management) for instructions on how to use brew). To install zsh this way, simply type:

``` bash
brew install zsh zsh-completions
```
To get the most out of zsh, you can try one of the several frameworks available. I am currently using [oh my zsh](http://ohmyz.sh). Oh my zsh gives you easy access to many useful [plugins](https://github.com/robbyrussell/oh-my-zsh/wiki/Plugins)


<!-- need post on how I customized my setup

# iTerm

split but can also use tmux

# Extras

`rtv`
`t`
other commands from brew (XX see package management for tips on Brew) -->
