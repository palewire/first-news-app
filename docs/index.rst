:tocdepth: 2

==============
First News App
==============

A step-by-step guide to publishing a simple news application with Python, Flask and GitHub.

This tutorial will walk you through the process of building a online application 
from a structured dataset. You will get hands-on experience in every stage of the development process,
writing Python, HTML and JavaScript using version control tools. By the end you will have
deployed a working application on the World Wide Web.

This tutorial was prepared for training sessions of `Investigative Reporters and Editors (IRE) <http://www.ire.org/>`_ 
and the `National Institute for Computer-Assisted Reporting (NICAR) <http://data.nicar.org/>`_
by `Ben Welsh <http://palewi.re/who-is-ben-welsh/>`_. It is still under construction but it will have its debut on February 27 `at the 
2014 CAR Conference in Baltimore, MD <https://ire.org/events-and-training/event/973/1026/>`_.

Other resources:

* Code repository: `https://github.com/ireapps/first-news-app <https://github.com/ireapps/first-news-app>`_
* Issues: `https://github.com/ireapps/first-news-app/issues <https://github.com/ireapps/first-news-app/issues>`_
* Documentation: `http://first-news-app.rtfd.org/ <http://first-news-app.rtfd.org/>`_

**********************
Prelude: Prerequisites
**********************

Before you can begin, your computer needs the following tools installed and working 
to participate.

1. A `command-line interface <https://en.wikipedia.org/wiki/Command-line_interface>`_ to interact with your computer
2. A `text editor <https://en.wikipedia.org/wiki/Text_editor>`_ to work with plain text files
3. `Git <http://git-scm.com/>`_ version control software and an account at `GitHub.com <http://www.github.com>`_
4. Version 2.7 of the `Python <http://python.org>`_ programming language
5. The `pip <http://www.pip-installer.org/en/latest/installing.html>`_ package manager for Python

.. note::

    Depending on your experience and operating system, you might already be ready
    to go with everything above. If so, move on to the next chapter. If not, 
    don't worry. And don't give up! It will be a bit of a 
    slog but the instructions below will point you in the right direction.

Command-line interface
----------------------

Unless something is wrong with your computer, there should be a way to open a window that lets you 
type in commands. Different operating systems give this tool slightly different names, but they all have
some form of it, and there are alternative programs you can install as well. 

On Windows you can find the command-line interface by opening the "command prompt." Here are instructions for 
`Windows 8 <http://windows.microsoft.com/en-us/windows/command-prompt-faq#1TC=windows-8>`_ 
and `earlier versions <http://windows.microsoft.com/en-us/windows-vista/open-a-command-prompt-window>`_. On
an Apple desktops, you open the `"Terminal" application 
<http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line>`_. Ubuntu Linux 
comes with a program of the `same name 
<http://askubuntu.com/questions/38162/what-is-a-terminal-and-how-do-i-open-and-use-it>`_.

Text editor
-----------

A program like Microsoft Word, which can do all sorts of text formatting like
change the size and color of words, is not what you need. Do not try to use it below.

You need a program that works with simple `"plain text" files <https://en.wikipedia.org/wiki/Text_file>`_,
and is therefore capable of editing documents containing Python code, HTML markup and other languages without
dressing them up by adding anything extra. Such programs are easy to find and some of the best ones are free, including those below.

For Windows, I recommend installing `Notepad++ <http://notepad-plus-plus.org/>`_. For
Apple computers, try `TextWrangler <http://www.barebones.com/products/textwrangler/download.html>`_. In
Ubuntu Linux you can stick with the pre-installed `gedit <https://help.ubuntu.com/community/gedit>`_ text editor.

Git and GitHub
--------------

`Git <http://git-scm.com/>`_ is a version control program for saving the changes 
you make to files over time. This is useful when you're working on your own, 
but quickly becomes essential with large software projects, especially if you work with other developers. 

`GitHub <https://github.com/>`_ is a website that hosts git code repositories, both public and private. It comes
with many helpful tools for reviewing code and managing projects. It also has some 
`extra tricks <http://pages.github.com/>`_ that make it easy to publish web pages, which we will use later. 

GitHub offers helpful guides for installing Git in 
`Windows <https://help.github.com/articles/set-up-git#platform-windows>`_,
`Macs <https://help.github.com/articles/set-up-git#platform-mac>`_ and
`Linux <https://help.github.com/articles/set-up-git#platform-linux>`_. You can verify
it's installed from your command line like so:

.. code-block:: bash

    $ git --version

Once that's done, you should create an account at GitHub, if you don't already have one.
It shouldn't cost you anything. `The free plan <https://github.com/pricing>`_ 
is all that's required to complete this lesson.

Python
------

If you are using Mac OSX or a common flavor of Linux, Python is probably already installed and you can 
test to see what version, if any, is there waiting for you by typing the following into your terminal. 

.. code-block:: bash

    $ python -V

If you don't have Python installed (a more likely fate for Windows users) try downloading and installing it from `here 
<http://www.python.org/download/releases/2.7.6/>`_. Python 2.7 is preferred but you can probably find a
way to make most of this tutorial work with other versions if you futz a little.

pip
---

The `pip package manager <http://www.pip-installer.org/en/latest/index.html>`_
makes it easy to install open-source libraries that 
expand what you're able to do with Python. Later, we will use it to install everything
needed to create a working web application. 

If you don't have it already, you can get pip by following 
`these instructions <http://www.pip-installer.org/en/latest/installing.html>`_.
Verify it's installed with the following.

.. code-block:: bash

    $ pip -V

****************
Act 1: Hello Git
****************

.. code-block:: bash

    $ git init repo
    $ cd repo
    # Create a new 'first-news-app' app on GitHub
    $ git remote add origin https://github.com/<yourusername>/first-news-app.git
    $ touch README.md
    # Write something in the file
    $ git commit add README.md
    $ git commit -m "First commit"
    $ git push origin master
    # Look at your repo on the web

******************
Act 2: Hello Flask
******************

.. code-block:: bash

    $ pip install Flask
    $ touch app.py
    # Fill it in with basic Flask stuff to make a single page
    $ mkdir templates
    $ touch templates/index.html
    # Write Hello NICAR14 in the template file
    $ python app.py
    # Check it out in the browser
    $ git add .
    $ git commit -m "Flask app.py and first template"
    # Check out the commit message and diff on GitHub


*****************
Act 3: Hello HTML
*****************

.. code-block:: bash

    $ mkdir static
    # Download the data file and load it into the template context and dump
    # it into the HTML template
    $ git add .
    $ git commit -m "Added CSV source data"
    # Show how GitHub nicely formats CSV in the website
    # Create basic table in HTML page
    $ git add .
    $ git commit -m "Created basic table"

***********************
Act 4: Hello JavaScript
***********************

.. code-block:: bash

    # Convert to Leaflet map
    $ git add .
    $ git commit -m "Replaced table with map"

*********************
Act 5: Hello Internet
*********************

.. code-block:: bash

    $ pip install Frozen-Flask
    $ touch freeze.py
    # Fill in freeze app
    $ python freeze.py
    $ git add .
    $ git commit -m "Frozen our app"
    # Open up the frozen page in the browser and point out differences
    $ git checkout gh-pages
    $ git rebase master
    $ git push origin gh-pages
    # The big reveal at http://<yourusername>.github.io/first-news-app/build/index.html

