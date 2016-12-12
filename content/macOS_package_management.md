Title: macOS Package Management
Date: 2016-12-07
Tags: macos, brew, cask
Category: the cyber
Slug: package-management
Summary: Overview of package management tools for macOS, particularly homebrew.

why package management; management of dpendencies; cross sytem use; prserverance of states

Package managers allow for ... This is the first in a series were we go over package managers for various things will focus on mac operating system (now referred to as macOS)


# homebrew

`brew`: basic package management for command line software (distributed under open source). A simple run down and further documentation details are found at the [brew webiste](http://brew.sh).

For installation simply type: `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

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

* `brew tap caskroom/cask`
* `brew install brew-cask`

# Current Packages

## Brew Packages

A few packages I installed using `brew`

`ansiweather` display weather in terminal

`cmatrix` turn your terminal into the Matrix

`htop` show computer diagnostics

## Cask Packages

RStudio



Github file to download all of these commands?


# Future Installments

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
