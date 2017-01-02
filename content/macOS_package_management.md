Title: macOS Package Management
Date: 2016-12-07
Tags: macos, brew, cask, tips
Category: tech
Slug: package-management
Summary: Overview of `brew`, a package manager for macOS

This is the first in a series of articles about package managers for various programs. Packages are optional plugins that provide some extra functionality to a program you use. They are often free and open source software (FOSS) made by individuals or consortiums. Packages are available to download for a range of programs: from apps you download (Sublime Text) to the operating system itself (macOS).

On macOS for example, the `git` package gives you the super-popular version control language git while the `htop` package will display computer diagnostics in your terminal.

Equally important are package managers that give you easy access to packages as well as the ability to maintain and update packages. Unfortunately, there is no unified package manager for all programs.

This series of articles will review packages and package managers for a variety of programs such as macOS, frameworks (node), languages (R, Python, Ruby), and text editors (Sublime, Atom, and Vim).

<!-- You will need to be at least somewhat familiar with the command line to work with `brew`; please see XXX for a quick guide. -->


# homebrew

`brew`: basic package management for command line software (distributed under open source). A simple run down and further documentation details are found at the [brew website](http://brew.sh).

For installation simply type:

``` bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

A breakdown of what is happening with the installation command above:

* `/usr/bin/ruby` calls ruby (which is used to install homebrew); ruby is pre-installed on macOS
* `-e` tells ruby to run raw code that is being passed to it
* `curl` program to download contents at specified URL
* `fsSL` this is actually four flags
	* `-f` fail silently if something goes wrong
	* `-s` silent mode; not progress or failure message
	* `-S` display error message if fails in silent mode
	* `-L` if server says that webpage has moved to a new location, curl will try that location
* URL: location of installation script

Terminology (for more details checkout the [formula cookbook](https://github.com/Homebrew/brew/blob/master/docs/Formula-Cookbook.md#homebrew-terminology)

* **formula** is a package
* **keg** is the installation prefix
* **cellar** is where packages are installed

Some useful commands:

* `brew install [formula]` install formula
* `brew search` search for formulas
* `brew cleanup` check for problems and fix them
* `brew doctor` diagnostic check
* `brew tap caskroom/cask` not all formulas are available on the main homebrew repository; to access these, you need to tap into a cask repo
	* Example: to install `R` you must first `brew tap homebrew/science` and then `brew install R`

# cask

`cask` There is an extension for `brew` called `cask` for the installation of licensed software. Because `cask` is an extension of `brew` it works the same as `brew` in terms of commands and taps.

To install `cask`:

``` bash
brew tap caskroom/cask
brew install brew-cask
```

To install a program like RStudio:

`brew install Caskroom/cask/rstudio`

# Current Packages

Below is a select list of packages that I use brew to manage. Some are trivial (e.g., `cowsay`) while others are frequently used system wide (e.g., `r`, `ruby`)

## Brew Packages

`ansiweather` display weather in terminal

<!-- `cairo` 2D graphics library -->

`cmatrix` turn your terminal into the Matrix

`coreutils` utilities for GNU

`cowsay` display a cow (or other creature) saying something

<!-- `cscope` browse source code -->

`curl` transfer data with URL syntax

`doxygen` source code documentation and analysis tool

`elinks` text based web browser

`emojify` emojis on the command line

`fasd` quick access to files and directories

`figlet` display text as ascii art

`fortune` random quote

`gcc` GNU compiler collection

`gdbm` GNU database functions

`git` version control

`givegif` display gifs

`glib` core application building blocks for apps written in C

`htop` show computer diagnostics

`node` javascript framework

`pipes-sh` pipes screen saver

`python` python

`r` r

`ruby` ruby

`sl` have a steam locomotive run across your terminal

`tmux` terminal multiplexer

`tree` display directories as a tree

`vim` text editor

`youtube-dl` download youtube videos

`zsh` bash alternative

`zsh-completions` completions for zsh

Over the next few days I'll add to this list and show some of the cool things you can do with them.

## Cask Packages

`RStudio` IDE for developing R; `brew` is terrific for managing the frequent [updates](https://www.rstudio.com)

<!-- what about packages? -->

`anaconda` scientific computing stack provided by [Continuum](https://www.continuum.io)

<!-- Github file to download all of these commands? -->


# Future Installments

Below are future articles for other package managers that I frequently use.

* npm
* gem
* Python
* R
* Text editors: Sublime, Atom, Vim
* Docker

<!--  
what about zsh plugins? pelican (pelican plugins)?

## node
* `npm`: package manager for javascript
	* install:

## ruby
* `gem`: package manager for ruby
	* install:

`gem query` list installed packages

tmuxinator
teamocil

## Others
* macports - alternative but not using






# Python

conda?
pip -- is the main thing

problem with updating

# R

R studio

See XXXother article on R package management

brew?

problem with updating

# Sublime

https://packagecontrol.io

auto update

persistence?

See XXXother article for useful Sublime packages

# Atom
Take care of already

# Docker

a way to sidestep the issue all together

-->
