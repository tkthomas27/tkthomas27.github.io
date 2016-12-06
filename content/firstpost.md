Title: First Post
Date: 2016-11-17
Tags: first
Category: test
Slug: first-post
Summary: Short summary of first-post


# Machine Preparation
each one of these can be a post in a series

## Machine Configuration
*  Key Mappings
	*  Capslock = ESC
	*  ctrl + arrow = left right max
	*  shift + ctrl + arrow = switch desktops
	*  cmd + esc = open iTerm

## Package Management
* `brew`: basic package management for command line software (distributed under open source)
	* install: `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
	* `brew search` search for packages/formulas
	* `brew tap caskroom/cask` taps into cask repo allowing you access to formulas in that repo
	* `brew link --overwrite --dry-run`
	* [homebrew formula cookbook](https://github.com/Homebrew/brew/blob/master/docs/Formula-Cookbook.md#homebrew-terminology)
	* use brew to install and maintain important programs like r/rstudio
* `cask`: extension of brew for more complicated, licensed software (`brew cask`)
	* install:
	* `cleanup`
	* `doctor`
	* `brew cask info caskroom/cask/rstudio` check version of app before installing (might need to `tap` first)
	* https://github.com/caskroom/homebrew-cask/blob/master/USAGE.md
* `npm`: package manager for javascript
	* install:
* `gem`: package manager for ruby
	* install:
* Misc:
	* macports - alternative but not using

## Shell
* iterm: terminal replacement; heavily customizable
	* install: `brew cask install iterm2`
	* need profile saved?
	* color schemes: currently using solarized dark
* tmux: terminal multiplexer; built into iterm
	* install: `brew install tmux`
	* cheatsheet:  https://tmuxcheatsheet.com
* teamocil : save window/pane layouts for tmux
	* install: `gem install teamocil`
	* `tmux` then `teamocil general` to runt he layout "general"
* zsh: alternative to bash
	* install:
	* `run-help foo` see help for built in command
	* `chsh` change shell --- need more
	* plugins
		* osx
		* internet
		* syntax-highlighting
		* need to add more
* ohmyzsh: zsh framework
	* install:
	* features: themes, shortcuts?
	* what is the point
* powerline: prompt configuration
	* install:
	* need fonts from github
	* `sh install.sh`
* configuration
	* works well: http://rick.cogley.info/post/use-homebrew-zsh-instead-of-the-osx-default/
	* works for getting powerline/vim to work: https://blog.codefront.net/2013/10/27/installing-powerline-on-os-x-homebrew/
	* .zshrc: automatically modified by ohmyzsh
	* .vimrc: awesomevim?
	* .tmux.conf: maybe bunsen?
	* dotfile repo: place to store and version control dotfiles
		* https://www.digitalocean.com/community/tutorials/how-to-use-git-to-manage-your-user-configuration-files-on-a-linux-vps
* twitter `t`
	* https://computers.tutsplus.com/tutorials/how-to-tweet-from-terminal-on-a-mac--cms-24177
	* `sudo gem install -n /usr/local/bin t` becasue of SIP
	* `t stream timeline` to stream timeline
* Ruby
	* install:
	* `rvm get stable` update to latest version
* Miscellaneous: each can be installed by `brew foo`
	* `cowsay` cow saying things
	* `cowsay -f dragon` dragon saying things
	* `fortune`gives fortune
	* `fortune | cowsay` has cow saying a fortune
	* `sl` steam locomotive
	* `figlet -f epic welcome` writes "welcome" in epic font
	* `telnet towel.blinkenlights.nl` shows star wars in terminal
	*  `htop` shows computer diagnostics
	*  `lolcat`
	*  tetris: `emacs` Esc x `tetris`
	* `cmatrix -a`
	* `givegif`
	* `movie Alien::Aliens`
	* `ansiweather -l Cambridge,MA -u imperial -d true`
	* `glances`
	* `emojify`
	* `rvt`

## Version Control
* git
	* need to install with homebrew
	* then switch system git to this brew version
	* http://michaelcrump.net/step-by-step-how-to-update-git/
* github

git submodules

## Python
* python version control: mac comes with default 2.7
* `pip`
	* `pip install --upgrade pip`
* `virtualenv -p python3 envname` for virtual environment and python 3 -- doesn't work
* currently setting up python 3.5 by downloading anaconda
* `conda create -n yourenvname python=x.x anaconda` for creating virtual environment
	* https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/
* jupyter: ipython notebooks
* rodeo: rstudio ide clone for python
* docker images



https://dougblack.io/words/a-good-vimrc.html
https://justin.abrah.ms/vim/vim_and_python.html

## R/RStudio
managing r and rstudio with brew
docker images
need to maintain packages even during installation of new versions

hadley advanced r: http://adv-r.had.co.nz

spring R

---

## Text Editing
* Markdown
* Sublime Text
	* install: brew?
	* package control
	* packages:
		* Stata
		* R
		* Latexing
		* latex cwl
* Evernote + Marxico
* Atom

### Latex
* install via brew, maybe use basictex if it is faster and lighter
* pdf viewer
* basictex?

### Vim
plugins: http://vimawesome.com
* vundler: plugin manager
	* intall: `git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim`
* `sv` `vs` open vertically/horizontally
* `ctrl+hjkl`  change panes
* `:ls` list open buffers
* https://realpython.com/blog/python/vim-and-python-a-match-made-in-heaven/
	* for most of setup

---

## Applications
* bar tender: for osx toolbar management
* istats menu: for toolbar diagnostics
* ubersicht: for desktop items
* moom vs bettersnaptool
* onyx: for maintenance of computer

---

## Pelican
* Pelican: python based, simple, fast
* https://www.fullstackpython.com/pelican.html
* github pages for free hosting?
	* need to redirect

downloaded pelican themes

http://guizishanren.com/guide-to-set-up-github-page-and-pelican/
this looks good

### Theme
- git clone xxxpelican themes
- chose Flex theme (responsive)
- themes in pelicanconf
- need relative url to be uncommented
- Flex documentation
https://github.com/alexandrevicenzi/Flex/tree/5bc235cf579cb03bcc8f54b6029ff74493a0cb44

#### Theme Formatting
- update pelican theme configuration using Flex author's config
https://github.com/alexandrevicenzi/Flex/wiki/Configuration-example
- change css
- `npm install -g less`
- `npm install -g less-plugin-clean-css`
- `cd` to `static/stylesheet` in Flex
- `lessc --clean-css style.less style.min.css`

### Pelican Plugins
- git clone xxxpelican plugins
- add lines in pelicanconf
- jax rendering works
	- maybe do some formating (render_math pelican plugin)
- investigate
	- Auto Pages
	- Category Order
	- Figure References
	- Filetime from Git: no b/c all articles get commited at once
	- Neighbor articles
	- Open graph
	- Pelican Cite
	- pelican-toc
	- Pelican YouTube
	- pelicanfly
	- Random article
	- Section number
	- Summary
	- Video Privacy Enhancer

### Local Testing
- `make html`
- `make devserver`
- `./develop_server.sh stop`
- use blog template

### Publish
- `ghp-import output -b master`
- `git push origin master`

---



##




## Learning
* Dataquest
* Codeacademy
* Datacamp
* Coursera
	* Scala
* edX
* vim adventure: for learning vim




### Code block
``` python
@requires_authorization
def somefunc(param1='', param2=0):
    '''A docstring'''
    if param1 > param2: # interesting
        print 'Greater'
    return (param2 - param1 + 1) or None
class SomeClass:
    pass
>>> message = '''interpreter
... prompt'''
```

### LaTeX expression
$$	x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a} $$

### Table
| Item      |    Value | Qty  |
| :-------- | --------:| :--: |
| Computer  | 1600 USD |  5   |
| Phone     |   12 USD |  12  |
| Pipe      |    1 USD | 234  |





---
To Do:
git backup config files/dotfiles
for macbook air: use hadleyverse docker for quickly getting setup




https://www.codementor.io/linux/tutorial/configure-linux-toolset-zsh-tmux-vim




from brew install vim (not sure if this is necessary)
By default non-brewed cpan modules are installed to the Cellar. If you wish
for your modules to persist across updates we recommend using `local::lib`.

You can set that up like this:
  PERL_MM_OPT="INSTALL_BASE=$HOME/perl5" cpan local::lib
  echo 'eval "$(perl -I$HOME/perl5/lib/perl5 -Mlocal::lib)"' >> ~/.zshrc
