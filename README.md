# AHOpen homepage

## build

Install python stuff [inside a virtual environment](https://wiki.archlinux.org/title/Python/Virtual_environment):

~~~bash
$ git submodule update --init --recursive
$ python -m venv build
$ source build/bin/activate
$ pip install -e libs/mkdocs-badges
$ pip install -e libs/mkdocs-link-embeds
~~~

Run [your local site](localhost:8000) during development/writing:

~~~bash
$ # inside the virtual environment:
$ mkdocs serve
~~~

## TODO
* create good guides for students:
  - how to create a nice looking and easy portfolio using github/github pages 
  * how to use markdown and pandoc for writing
  * how to use Github for your studies. Git, Gists and more. Collaboration.
* create pandoc/latex template for diploma writing
* create a curated list of good learning resources for courses at AHO, preferably 
  Wikipedia and similar open sources. Maybe use our own github wiki for that?
