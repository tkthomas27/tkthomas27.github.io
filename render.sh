#!/bin/bash

#http://cfss.uchicago.edu/fall2016/project_python.html

# convert jupyter notebooks to markdown
for notebook in $( ls *.ipynb ); do
/Users/$USER/anaconda/bin/jupyter nbconvert --to markdown $notebook
done

# render_site using rmarkdown
Rscript -e 'rmarkdown::render_site()'