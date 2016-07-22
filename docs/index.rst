:tocdepth: 2

==============
First News App
==============

A step-by-step guide to publishing a simple news application.

This tutorial will walk you through the process of building an interactive data visualization
from a structured dataset. You will get hands-on experience in every stage of the
development process, writing Python, HTML and JavaScript and recording it in Git's
version control system. By the end you will have published your work on the World Wide Web.

This guide was prepared for training sessions of `Investigative Reporters and Editors (IRE) <http://www.ire.org/>`_
and the `National Institute for Computer-Assisted Reporting (NICAR) <http://data.nicar.org/>`_
by `Ben Welsh <http://palewi.re/who-is-ben-welsh/>`_. It debuted on February 27, 2014, `at NICAR's annual conference
in Baltimore <https://ire.org/events-and-training/event/973/1026/>`_. A revised version was presented at
`the following year's conference <http://ire.org/conferences/nicar2015/hands-on-training/>`_ in Atlanta. It
is scheduled to be taught again at `the upcoming Denver conference <http://www.ire.org/conferences/nicar2016/schedule/>`_
on March 11 and 12, 2016.

* Code: `github.com/ireapps/first-news-app <https://github.com/ireapps/first-news-app>`_
* Demonstration: `ireapps.github.io/first-news-app/build/index.html <http://ireapps.github.io/first-news-app/build/index.html>`_
* Issues: `github.com/ireapps/first-news-app/issues <https://github.com/ireapps/first-news-app/issues>`_

******************
What you will make
******************

This tutorial will guide you through the process of publishing an interactive database and map
about the more than 60 people who died during the riots that swept Los Angeles
for five days in 1992. You will repurpose the data from `a Los Angeles Times
application <http://spreadsheets.latimes.com/la-riots-deaths/>`_ that
accompanied a story released on the 20th anniversary of the riots.

A working example can be found at `ireapps.github.io/first-news-app/build/index.html <http://ireapps.github.io/first-news-app/build/index.html>`_

**********************
Prelude: Prerequisites
**********************

Before you can begin, your computer needs the following tools installed and working
to participate.

1. A `command-line interface <https://en.wikipedia.org/wiki/Command-line_interface>`_ to interact with your computer
2. A `text editor <https://en.wikipedia.org/wiki/Text_editor>`_ to work with plain text files
3. `Git <http://git-scm.com/>`_ version control software and an account at `GitHub.com <http://www.github.com>`_
4. Version 2.7 of the `Python <http://python.org/download/releases/2.7.6/>`_ programming language
5. The `pip <https://pip.pypa.io/en/latest/installing.html>`_ package manager and `virtualenv <http://www.virtualenv.org/en/latest/>`_ environment manager for Python

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
Apple computers, you open the `"Terminal" application
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

    # You don't have to type the "$" It's just a generic symbol
    # geeks use to show they're working on the command line.
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
<https://www.python.org/download/releases/2.7.8/>`_. In Windows, it's also crucial to make sure that the
Python program is available on your system's ``PATH`` so it can be called from anywhere on the command line. `This screencast <http://showmedo.com/videotutorials/video?name=960000&fromSeriesID=96>`_ can guide
you through that process.

Python 2.7 is preferred but you can probably find a
way to make most of this tutorial work with other versions if you futz a little.

pip and virtualenv
------------------

The `pip package manager <https://pip.pypa.io/en/latest/>`_
makes it easy to install open-source libraries that
expand what you're able to do with Python. Later, we will use it to install everything
needed to create a working web application.

If you don't have it already, you can get pip by following
`these instructions <https://pip.pypa.io/en/latest/installing.html>`_. In Windows, it's necessary to make sure that the
Python ``Scripts`` directory is available on your system's ``PATH`` so it can be called from anywhere on the command line. `This screencast <http://showmedo.com/videotutorials/video?name=960000&fromSeriesID=96>`_ can help.

Verify pip is installed with the following.

.. code-block:: bash

    $ pip -V

The `virtualenv environment manager <http://www.virtualenv.org/en/latest/>`_
makes it possible to create an isolated corner of your computer where all the different
tools you use to build an application are sealed off.

It might not be obvious why you need this, but it quickly becomes important when you need to juggle different tools
for different projects on one computer. By developing your applications inside separate
virtualenv environments, you can use different versions of the same third-party Python libraries without a conflict.
You can also more easily recreate your project on another machine, handy when
you want to copy your code to a server that publishes pages on the Internet.

You can check if virtualenv is installed with the following.

.. code-block:: bash

    $ virtualenv --version

If you don't have it, install it with pip.

.. code-block:: bash

    $ pip install virtualenv
    # If you're on a Mac or Linux and get an error saying you lack the right permissions, try it again as a superuser.
    $ sudo pip install virtualenv

If that doesn't work, `try following this advice <http://virtualenv.readthedocs.org/en/latest/installation.html>`_.

.. _activate:

****************
Act 1: Hello Git
****************

Start by creating a new development environment with virtualenv. Name it after our application.

.. code-block:: bash

    # You don't have to type the "$" It's just a generic symbol
    # geeks use to show they're working on the command line.
    $ virtualenv first-news-app

Jump into the directory it created.

.. code-block:: bash

    $ cd first-news-app

Turn on the new virtualenv, which will instruct your terminal to only use those libraries installed
inside its sealed space. You only need to create the virtualenv once, but you'll need to repeat these
"activation" steps each time you return to working on this project.

.. code-block:: bash

    # In Linux or Mac OSX try this...
    $ . bin/activate
    # In Windows it might take something more like...
    $ cd Scripts
    $ activate
    $ cd ..

Create a new Git repository.

.. code-block:: bash

    $ git init repo

Jump into the repository.

.. code-block:: bash

    $ cd repo

Visit `GitHub <http://www.github.com>`_ and create a new public repository named ``first-news-app``. Don't check "Initialize with README."
You want to start with a blank repository.

Then connect your local directory to it with the following.

.. code-block:: bash

    $ git remote add origin https://github.com/<yourusername>/first-news-app.git

Create your first file, a blank ``README`` with a `Markdown <https://en.wikipedia.org/wiki/Markdown>`_
file extension since that's `the preferred format of GitHub <https://help.github.com/articles/github-flavored-markdown>`_.

.. code-block:: bash

    # Macs or Linux:
    $ touch README.md
    # In Windows fire it up in your text editor right away:
    $ start notepad++ README.md

Open up the README in your text editor and type something in it. Maybe something like:

.. code-block:: markdown

    My first news app
    =================

Make sure to save it. Then officially add the file to your repository for tracking with Git's ``add`` command.

.. code-block:: bash

    $ git add README.md

Log its creation with Git's ``commit`` command. You can include a personalized message after the ``-m`` flag.

.. code-block:: bash

    $ git commit -m "First commit"

If this is your first time using Git, you may be prompted to configure you name and email.
If so, take the time now. Then run the ``commit`` command above again.

.. code-block:: bash

    $ git config --global user.email "your@email.com"
    $ git config --global user.name "your name"

Now, finally, push your commit up to GitHub.

.. code-block:: bash

    $ git push origin master

Reload your repository on GitHub and see your handiwork.

******************
Act 2: Hello Flask
******************

Use pip on the command line to install `Flask <http://flask.pocoo.org/>`_, the Python "microframework"
we'll use to put together our website.

.. code-block:: bash

    $ pip install Flask

Create a new file called ``app.py`` where we will configure Flask.

.. code-block:: bash

    # Again, Macs and Linux:
    $ touch app.py
    # Windows:
    $ start notepad++ app.py

Open ``app.py`` with your text editor and import the Flask basics. This is the file that will serve as your
application's "backend," routing data to the appropriate pages.

.. code-block:: python

    from flask import Flask
    app = Flask(__name__)  # Note the double underscores on each side!

Next we will configure Flask to make a page at your site's root URL.

Configure Flask to boot up a test server when you run ``app.py``.

.. code-block:: python
    :emphasize-lines: 4-6

    from flask import Flask
    app = Flask(__name__)

    if __name__ == '__main__':
        # Fire up the Flask test server
        app.run(debug=True, use_reloader=True)

.. note::

    You're probably asking, "What the heck is ``if __name__ == '__main__'``?" The short answer: It's just one of the weird things in Python you have to memorize. But it's worth the brain space because it allows you to run any Python script as a program.

    Anything indented inside that particular ``if`` clause is executed when the script is called from the command line. In this case, that means booting up your web site using Flask's built-in ``app.run`` function.

Don't forget to save your changes. Then run ``app.py`` on the command-line and open up your browser to `localhost:5000 <http://localhost:5000>`_

.. code-block:: bash

    $ python app.py

Here's what you should see. A website with nothing to show.

.. image:: /_static/hello-flask-404.png

Next we'll put a page there. Our goal is to publish the complete list of
people who died during the riots using a template called ``index.html``.

That starts by importing ``render_template``, a Flask function we can use to combine data with HTML to make a webpage.

.. code-block:: python
    :emphasize-lines: 2

    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    if __name__ == '__main__':
        # Fire up the Flask test server
        app.run(debug=True, use_reloader=True)

Then create a function called ``index`` that returns our rendered ``index.html`` template.

.. code-block:: python
    :emphasize-lines: 5-8

    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    def index():
        template = 'index.html'
        return render_template(template)

    if __name__ == '__main__':
        # Fire up the Flask test server
        app.run(debug=True, use_reloader=True)

Now use one of Flask's coolest tricks, the ``app.route`` decorater, to connect
that function with the root URL of our site, ``/``.

.. code-block:: python
    :emphasize-lines: 5

    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    @app.route("/")
    def index():
        template = 'index.html'
        return render_template(template)

    if __name__ == '__main__':
        # Fire up the Flask test server
        app.run(debug=True, use_reloader=True)

Return to your command-line interface and create a directory to store your templates in `the default location Flask expects <http://flask.pocoo.org/docs/quickstart/#rendering-templates>`_.

.. code-block:: bash

    $ mkdir templates

Next create the ``index.html`` file we referenced in ``app.py``. This is the HTML file where your will lay out your webpage.

.. code-block:: bash

    # Macs and Linux:
    $ touch templates/index.html
    # Windows:
    $ start notepad++ templates/index.html

Open it up in your text editor and write something clever.

.. code-block:: html

    Hello World!

Head back to your browser and visit `localhost:5000 <http://localhost:5000>`_ again. You should see
the contents of your template displayed on the page.

.. image:: /_static/hello-flask-hello-world.png

We're approaching the end of this act, so it's time to save your work by returning to the
command line and committing these changes to your Git repository.

.. note::

    To get the terminal back up, you will either need to quit out of ``app.py`` by hitting ``CTRL-C``, or open a second terminal and do additional work there. If you elect to open a second terminal, which is recommended, make sure to check into the virtualenv by repeating the ``. bin/activate`` part of :ref:`activate`. If you choose to quit out of ``app.py``, you will need to turn it back on later by calling ``python app.py`` where appropriate.

I bet you remember how from above. But here's a reminder.

.. code-block:: bash

    $ git add .
    $ git commit -m "Flask app.py and first template"

Push it up to GitHub and check out the changes there.

.. code-block:: bash

    $ git push origin master

Congratulations, you've made a real web page with Flask. Now to put something useful in it.

*****************
Act 3: Hello HTML
*****************

Start over in your ``templates/index.html`` file with a bare-bones HTML document.

.. code-block:: html

    <!doctype html>
    <html lang="en">
        <head></head>
        <body>
            <h1>Deaths during the L.A. riots</h1>
        </body>
    </html>

Commit the changes to your repository, if only for practice.

.. code-block:: bash

    $ git add templates/index.html
    $ git commit -m "Real HTML"
    $ git push origin master

Make a directory to store data files.

.. code-block:: bash

    $ mkdir static

Download `the comma-delimited file <https://raw.github.com/ireapps/first-news-app/master/static/la-riots-deaths.csv>`_ that will be the backbone of our application and save it there as ``la-riots-deaths.csv``. Add it to your git repository.

.. code-block:: bash

    $ git add static
    $ git commit -m "Added CSV source data"
    $ git push origin master

Next we will open up ``app.py`` in your text editor and create a function that uses Python's ``csv`` module to access the CSV data.

First, create the new function and give it the path to your CSV file.

.. code-block:: python
    :emphasize-lines: 1, 6-8

    import csv
    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    def get_csv():
        csv_path = './static/la-riots-deaths.csv'

    @app.route("/")
    def index():
        template = 'index.html'
        return render_template(template)

    if __name__ == '__main__':
        app.run(debug=True, use_reloader=True)

Open up the file path for reading with Python using the built-in `open <https://docs.python.org/2/library/functions.html#open>`_ function.

.. code-block:: python
    :emphasize-lines: 8

    import csv
    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    def get_csv():
        csv_path = './static/la-riots-deaths.csv'
        csv_file = open(csv_path, 'rb')

    @app.route("/")
    def index():
        template = 'index.html'
        return render_template(template)

    if __name__ == '__main__':
        app.run(debug=True, use_reloader=True)

Pass it into the csv module's `DictReader <https://docs.python.org/2/library/csv.html#csv.DictReader>`_, to be parsed and returned as a list of dictionaries.

.. code-block:: python
    :emphasize-lines: 9

    import csv
    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    def get_csv():
        csv_path = './static/la-riots-deaths.csv'
        csv_file = open(csv_path, 'rb')
        csv_obj = csv.DictReader(csv_file)

    @app.route("/")
    def index():
        template = 'index.html'
        return render_template(template)

    if __name__ == '__main__':
        app.run(debug=True, use_reloader=True)

.. note::

    Don't know what a dictionary is? That's okay. You can read more about them `here <http://learnpythonthehardway.org/book/ex39.html>`_ but the minimum you need to know now is that they are Python's way of handling each row in your CSV. The columns there, like ``id`` or ``gender``, are translated in "keys" on dictionary objects that you can access like ``row['id']``.

A quirks of CSV objects is that once they're used they disappear. There's a good reason related to efficiency and memory limitations and all that but we won't bother with that here. Just take our word and use Python's built-in ``list`` function to convert this one to a permanent list.

.. code-block:: python
    :emphasize-lines: 10

    import csv
    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    def get_csv():
        csv_path = './static/la-riots-deaths.csv'
        csv_file = open(csv_path, 'rb')
        csv_obj = csv.DictReader(csv_file)
        csv_list = list(csv_obj)

    @app.route("/")
    def index():
        template = 'index.html'
        return render_template(template)

    if __name__ == '__main__':
        app.run(debug=True, use_reloader=True)

Close the function by return the csv list.

.. code-block:: python
    :emphasize-lines: 11

    import csv
    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    def get_csv():
        csv_path = './static/la-riots-deaths.csv'
        csv_file = open(csv_path, 'rb')
        csv_obj = csv.DictReader(csv_file)
        csv_list = list(csv_obj)
        return csv_list

    @app.route("/")
    def index():
        template = 'index.html'
        return render_template(template)

    if __name__ == '__main__':
        app.run(debug=True, use_reloader=True)

Next have your ``index`` function pull the CSV data using your new code and pass it on the top the template, where it will be named ``object_list``.

.. code-block:: python
    :emphasize-lines: 16,17

    import csv
    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    def get_csv():
        csv_path = './static/la-riots-deaths.csv'
        csv_file = open(csv_path, 'r')
        csv_obj = csv.DictReader(csv_file)
        csv_list = list(csv_obj)
        return csv_list

    @app.route("/")
    def index():
        template = 'index.html'
        object_list = get_csv()
        return render_template(template, object_list=object_list)

    if __name__ == '__main__':
        app.run(debug=True, use_reloader=True)

Make sure to save ``app.py``. Then return to the ``index.html`` template. There you can dump out the ``object_list`` data using Flask's templating language `Jinja <http://jinja.pocoo.org/>`_.

.. code-block:: jinja
    :emphasize-lines: 6

    <!doctype html>
    <html lang="en">
        <head></head>
        <body>
            <h1>Deaths during the L.A. riots</h1>
            {{ object_list }}
        </body>
    </html>

If it isn't already running, return the command line, restart your test server and visit `localhost:5000 <http://localhost:5000>`_ again.

.. code-block:: bash

    $ python app.py

.. image:: /_static/hello-html-dump.png

Now we'll use Jinja to sculpt the data in ``index.html`` to create `an HTML table <http://www.w3schools.com/html/html_tables.asp>`_ that lists all the names. Flask's templating language allows us to loop through the data list and print out a row for each record.

.. code-block:: jinja
    :emphasize-lines: 6-15

    <!doctype html>
    <html lang="en">
        <head></head>
        <body>
            <h1>Deaths during the L.A. riots</h1>
            <table border=1 cellpadding=7>
                <tr>
                    <th>Name</th>
                </tr>
                {% for obj in object_list %}
                <tr>
                    <td>{{ obj.full_name }}</td>
                </tr>
                {% endfor %}
            </table>
        </body>
    </html>

Pause to reload your browser page.

.. image:: /_static/hello-html-names.png

Next expand the table to include a lot more data.

.. code-block:: jinja
    :emphasize-lines: 9-14, 19-24

    <!doctype html>
    <html lang="en">
        <head></head>
        <body>
            <h1>Deaths during the L.A. riots</h1>
            <table border=1 cellpadding=7>
                <tr>
                    <th>Name</th>
                    <th>Date</th>
                    <th>Type</th>
                    <th>Address</th>
                    <th>Age</th>
                    <th>Gender</th>
                    <th>Race</th>
                </tr>
                {% for obj in object_list %}
                <tr>
                    <td>{{ obj.full_name }}</td>
                    <td>{{ obj.date }}</td>
                    <td>{{ obj.type }}</td>
                    <td>{{ obj.address }}</td>
                    <td>{{ obj.age }}</td>
                    <td>{{ obj.gender }}</td>
                    <td>{{ obj.race }}</td>
                </tr>
                {% endfor %}
            </table>
        </body>
    </html>

Reload your page in the browser again to see the change.

.. image:: /_static/hello-html-table.png

Then commit your work.

.. code-block:: bash

    $ git add . # Using "." is a trick that will quickly stage *all* files you've changed.
    $ git commit -m "Created basic table"
    $ git push origin master

Next we're going to create a unique "detail" page dedicated to each person. Start by returning to ``app.py`` in your text editor and adding the URL and template that will help make this happen.

.. code-block:: python
    :emphasize-lines: 19-23

    import csv
    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    def get_csv():
        csv_path = './static/la-riots-deaths.csv'
        csv_file = open(csv_path, 'r')
        csv_obj = csv.DictReader(csv_file)
        csv_list = list(csv_obj)
        return csv_list

    @app.route("/")
    def index():
        template = 'index.html'
        object_list = get_csv()
        return render_template(template, object_list=object_list)

    @app.route('/<row_id>/')
    def detail(row_id):
        template = 'detail.html'
        return render_template(template)

    if __name__ == '__main__':
        app.run(debug=True, use_reloader=True)

.. note::

    Notice a key difference between the URL route for the index and the one we just added. This time, both the URL route and function accept an argument, named ``row_id``. Our goal is for the number passed into the URL and then through the function where it can be used to pull the record with the corresponding ``id`` from the CSV. Once we have our hands on it, we can pass it on to the template to render its unique page.

Create a new file in your templates directory called ``detail.html`` for it to connect with.

.. code-block:: bash

    # Macs and Linux:
    $ touch templates/detail.html
    # Windows:
    $ start notepad++ templates/detail.html

Put something simple in it with your text editor.

.. code-block:: html

    Hello World!

Then, if it's not running, restart your test server and use your browser to visit `localhost:5000/1/ <http://localhost:5000/1/>`_, `localhost:5000/200/ <http://localhost:5000/200/>`_ or any other number.

.. code-block:: bash

    $ python app.py

.. image:: /_static/hello-html-hello-detail.png

To customize the page for each person, we will need to connect the ``row_id`` in the URL with the ``id`` column in the CSV data file.

First, return to ``app.py`` and pull the CSV data into the ``detail`` view.

.. code-block:: python
    :emphasize-lines: 22

    import csv
    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    def get_csv():
        csv_path = './static/la-riots-deaths.csv'
        csv_file = open(csv_path, 'r')
        csv_obj = csv.DictReader(csv_file)
        csv_list = list(csv_obj)
        return csv_list

    @app.route("/")
    def index():
        template = 'index.html'
        object_list = get_csv()
        return render_template(template, object_list=object_list)

    @app.route('/<row_id>/')
    def detail(row_id):
        template = 'detail.html'
        object_list = get_csv()
        return render_template(template)

    if __name__ == '__main__':
        app.run(debug=True, use_reloader=True)

Then have the ``detail`` function loop through the CSV data list, testing each row'd ``id`` field against the ``row_id`` provided by the URL. When you find a match, pass that row out to the template for rendering with the name ``object``.

.. code-block:: python
    :emphasize-lines: 23,24,25

    import csv
    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    def get_csv():
        csv_path = './static/la-riots-deaths.csv'
        csv_file = open(csv_path, 'r')
        csv_obj = csv.DictReader(csv_file)
        csv_list = list(csv_obj)
        return csv_list

    @app.route("/")
    def index():
        template = 'index.html'
        object_list = get_csv()
        return render_template(template, object_list=object_list)

    @app.route('/<row_id>/')
    def detail(row_id):
        template = 'detail.html'
        object_list = get_csv()
        for row in object_list:
            if row['id'] == row_id:
                return render_template(template, object=row)

    if __name__ == '__main__':
        app.run(debug=True, use_reloader=True)

Now clear ``detail.html`` and make a new HTML document with a headline drawn from the data we've passed in from the dictionary.

.. code-block:: html

    <!doctype html>
    <html lang="en">
        <head></head>
        <body>
            <h1>{{ object.full_name }}</h1>
        </body>
    </html>

Restart your test server and take a look at ``http://localhost:5000/1/`` again.

.. code-block:: bash

    $ python app.py

.. image:: /_static/hello-html-hello-cesar.png

Return to ``index.html`` and add a hyperlink to each detail page to the table.

.. code-block:: html
    :emphasize-lines: 18

    <!doctype html>
    <html lang="en">
        <head></head>
        <body>
            <h1>Deaths during the L.A. riots</h1>
            <table border=1 cellpadding=7>
                <tr>
                    <th>Name</th>
                    <th>Date</th>
                    <th>Type</th>
                    <th>Address</th>
                    <th>Age</th>
                    <th>Gender</th>
                    <th>Race</th>
                </tr>
            {% for obj in object_list %}
                <tr>
                    <td><a href="{{ obj.id }}/">{{ obj.full_name }}</a></td>
                    <td>{{ obj.date }}</td>
                    <td>{{ obj.type }}</td>
                    <td>{{ obj.address }}</td>
                    <td>{{ obj.age }}</td>
                    <td>{{ obj.gender }}</td>
                    <td>{{ obj.race }}</td>
                </tr>
            {% endfor %}
            </table>
        </body>
    </html>

Restart your test server and take a look at ``http://localhost:5000/``.

.. code-block:: bash

    $ python app.py

.. image:: /_static/hello-html-hello-links.png

In ``detail.html`` you can use the rest of the data fields to write a sentence about the victim.

.. code-block:: html
    :emphasize-lines: 5-10

    <!doctype html>
    <html lang="en">
        <head></head>
        <body>
            <h1>
                {{ object.full_name }}, a {{ object.age }} year old,
                {{ object.race }} {{ object.gender|lower }} died on {{ object.date }}
                in a {{ object.type|lower }} at {{ object.address }} in {{ object.neighborhood }}.
            </h1>
        </body>
    </html>

Reload `localhost:5000/1/ <http://localhost:5000/1/>`_ to see it.

.. image:: /_static/hello-html-hello-graf.png

Then once again commit your work.

.. code-block:: bash

    $ git add .
    $ git commit -m "Created a detail page about each victim."
    $ git push origin master

One last thing before we move on. What if somebody vists an URL for an ``id`` that doesn't exist, like `localhost:5000/99999/ <http://localhost:5000/99999/>`_? Right now Flask throws an ugly error.

.. image:: /_static/hello-html-error.png

The polite thing to do is return what is called a `404 response code <http://en.wikipedia.org/wiki/HTTP_404>`_. To do that Flask, you only need to import a function called ``abort`` and run it after our loop finishes without finding a match.

.. code-block:: python
    :emphasize-lines: 3,27

    import csv
    from flask import Flask
    from flask import abort
    from flask import render_template
    app = Flask(__name__)

    def get_csv():
        csv_path = './static/la-riots-deaths.csv'
        csv_file = open(csv_path, 'r')
        csv_obj = csv.DictReader(csv_file)
        csv_list = list(csv_obj)
        return csv_list

    @app.route("/")
    def index():
        template = 'index.html'
        object_list = get_csv()
        return render_template(template, object_list=object_list)

    @app.route('/<row_id>/')
    def detail(row_id):
        template = 'detail.html'
        object_list = get_csv()
        for row in object_list:
            if row['id'] == row_id:
                return render_template(template, object=row)
        abort(404)

    if __name__ == '__main__':
        app.run(debug=True, use_reloader=True)

Reload your bad URL and you'll see the change.

.. image:: /_static/hello-html-404.png

***********************
Act 4: Hello JavaScript
***********************

Next we will work to make a map with every victim in ``index.html`` using the
`Leaflet <http://leafletjs.com/>`_ JavaScript library. Start by importing it in your page.

.. code-block:: html
    :emphasize-lines: 4-5

    <!doctype html>
    <html lang="en">
        <head>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/leaflet.css" />
            <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/leaflet.js"></script>
        </head>
        <body>
            <h1>Deaths during the L.A. riots</h1>
            <table border=1 cellpadding=7>
                <tr>
                    <th>Name</th>
                    <th>Date</th>
                    <th>Type</th>
                    <th>Address</th>
                    <th>Age</th>
                    <th>Gender</th>
                    <th>Race</th>
                </tr>
            {% for obj in object_list %}
                <tr>
                    <td><a href="{{ obj.id }}/">{{ obj.full_name }}</a></td>
                    <td>{{ obj.date }}</td>
                    <td>{{ obj.type }}</td>
                    <td>{{ obj.address }}</td>
                    <td>{{ obj.age }}</td>
                    <td>{{ obj.gender }}</td>
                    <td>{{ obj.race }}</td>
                </tr>
            {% endfor %}
            </table>
        </body>
    </html>

Create an HTML element to hold the map and use Leaflet to boot it up and center on Los Angeles.

.. code-block:: html
    :emphasize-lines: 8,32-40

    <!doctype html>
    <html lang="en">
        <head>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/leaflet.css" />
            <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/leaflet.js"></script>
        </head>
        <body>
            <div id="map" style="width:100%; height:300px;"></div>
            <h1>Deaths during the L.A. riots</h1>
            <table border=1 cellpadding=7>
                <tr>
                    <th>Name</th>
                    <th>Date</th>
                    <th>Type</th>
                    <th>Address</th>
                    <th>Age</th>
                    <th>Gender</th>
                    <th>Race</th>
                </tr>
            {% for obj in object_list %}
                <tr>
                    <td><a href="{{ obj.id }}/">{{ obj.full_name }}</a></td>
                    <td>{{ obj.date }}</td>
                    <td>{{ obj.type }}</td>
                    <td>{{ obj.address }}</td>
                    <td>{{ obj.age }}</td>
                    <td>{{ obj.gender }}</td>
                    <td>{{ obj.race }}</td>
                </tr>
            {% endfor %}
            </table>
            <script type="text/javascript">
                var map = L.map('map').setView([34.055, -118.35], 9);
                var osmLayer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 18,
                    attribution: 'Data, imagery and map information provided by <a href="http://www.openstreetmap.org/" target="_blank">OpenStreetMap</a>.'
                });
                map.addLayer(osmLayer);
            </script>
        </body>
    </html>

Reload the root URL of your site at `localhost:5000 <http://localhost:5000/>`_.

.. image:: /_static/hello-js-empty-map.png

Loop through the CSV data and format it as a `GeoJSON <https://en.wikipedia.org/wiki/GeoJSON>`_ object, which Leaflet can easily load.

.. code-block:: html
    :emphasize-lines: 40-59

    <!doctype html>
    <html lang="en">
        <head>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/leaflet.css" />
            <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/leaflet.js"></script>
        </head>
        <body>
            <div id="map" style="width:100%; height:300px;"></div>
            <h1>Deaths during the L.A. riots</h1>
            <table border=1 cellpadding=7>
                <tr>
                    <th>Name</th>
                    <th>Date</th>
                    <th>Type</th>
                    <th>Address</th>
                    <th>Age</th>
                    <th>Gender</th>
                    <th>Race</th>
                </tr>
            {% for obj in object_list %}
                <tr>
                    <td><a href="{{ obj.id }}/">{{ obj.full_name }}</a></td>
                    <td>{{ obj.date }}</td>
                    <td>{{ obj.type }}</td>
                    <td>{{ obj.address }}</td>
                    <td>{{ obj.age }}</td>
                    <td>{{ obj.gender }}</td>
                    <td>{{ obj.race }}</td>
                </tr>
            {% endfor %}
            </table>
            <script type="text/javascript">
                var map = L.map('map').setView([34.055, -118.35], 9);
                var osmLayer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 18,
                    attribution: 'Data, imagery and map information provided by <a href="http://www.openstreetmap.org/" target="_blank">OpenStreetMap</a> and contributors.'
                });
                map.addLayer(osmLayer);
                var data = {
                  "type": "FeatureCollection",
                  "features": [
                    {% for obj in object_list %}
                    {
                      "type": "Feature",
                      "properties": {
                        "full_name": "{{ obj.full_name }}",
                        "id": "{{ obj.id }}"
                      },
                      "geometry": {
                        "type": "Point",
                        "coordinates": [{{ obj.x }}, {{ obj.y }}]
                      }
                    }{% if not loop.last %},{% endif %}
                    {% endfor %}
                  ]
                };
                var dataLayer = L.geoJson(data);
                map.addLayer(dataLayer);
            </script>
        </body>
    </html>

Reload the page.

.. image:: /_static/hello-js-pins.png

Add a popup on the map pins that shows the name of the victim.

.. code-block:: html
    :emphasize-lines: 58-62

    <!doctype html>
    <html lang="en">
        <head>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/leaflet.css" />
            <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/leaflet.js"></script>
        </head>
        <body>
            <div id="map" style="width:100%; height:300px;"></div>
            <h1>Deaths during the L.A. riots</h1>
            <table border=1 cellpadding=7>
                <tr>
                    <th>Name</th>
                    <th>Date</th>
                    <th>Type</th>
                    <th>Address</th>
                    <th>Age</th>
                    <th>Gender</th>
                    <th>Race</th>
                </tr>
            {% for obj in object_list %}
                <tr>
                    <td><a href="{{ obj.id }}/">{{ obj.full_name }}</a></td>
                    <td>{{ obj.date }}</td>
                    <td>{{ obj.type }}</td>
                    <td>{{ obj.address }}</td>
                    <td>{{ obj.age }}</td>
                    <td>{{ obj.gender }}</td>
                    <td>{{ obj.race }}</td>
                </tr>
            {% endfor %}
            </table>
            <script type="text/javascript">
                var map = L.map('map').setView([34.055, -118.35], 9);
                var osmLayer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 18,
                    attribution: 'Data, imagery and map information provided by <a href="http://www.openstreetmap.org/" target="_blank">OpenStreetMap</a> and contributors.'
                });
                map.addLayer(osmLayer);
                var data = {
                  "type": "FeatureCollection",
                  "features": [
                    {% for obj in object_list %}
                    {
                      "type": "Feature",
                      "properties": {
                        "full_name": "{{ obj.full_name }}",
                        "id": "{{ obj.id }}"
                      },
                      "geometry": {
                        "type": "Point",
                        "coordinates": [{{ obj.x }}, {{ obj.y }}]
                      }
                    }{% if not loop.last %},{% endif %}
                    {% endfor %}
                  ]
                };
                var dataLayer = L.geoJson(data, {
                    onEachFeature: function(feature, layer) {
                        layer.bindPopup(feature.properties.full_name);
                    }
                });
                map.addLayer(dataLayer);
            </script>
        </body>
    </html>

Reload the page and click a pin.

.. image:: /_static/hello-js-popup.png

Now wrap the name in a hyperlink to that person's detail page.

.. code-block:: html
    :emphasize-lines: 58-66

    <!doctype html>
    <html lang="en">
        <head>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/leaflet.css" />
            <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/leaflet.js"></script>
        </head>
        <body>
            <div id="map" style="width:100%; height:300px;"></div>
            <h1>Deaths during the L.A. riots</h1>
            <table border=1 cellpadding=7>
                <tr>
                    <th>Name</th>
                    <th>Date</th>
                    <th>Type</th>
                    <th>Address</th>
                    <th>Age</th>
                    <th>Gender</th>
                    <th>Race</th>
                </tr>
            {% for obj in object_list %}
                <tr>
                    <td><a href="{{ obj.id }}/">{{ obj.full_name }}</a></td>
                    <td>{{ obj.date }}</td>
                    <td>{{ obj.type }}</td>
                    <td>{{ obj.address }}</td>
                    <td>{{ obj.age }}</td>
                    <td>{{ obj.gender }}</td>
                    <td>{{ obj.race }}</td>
                </tr>
            {% endfor %}
            </table>
            <script type="text/javascript">
                var map = L.map('map').setView([34.055, -118.35], 9);
                var osmLayer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 18,
                    attribution: 'Data, imagery and map information provided by <a href="http://www.openstreetmap.org/" target="_blank">OpenStreetMap</a> and contributors.'
                });
                map.addLayer(osmLayer);
                var data = {
                  "type": "FeatureCollection",
                  "features": [
                    {% for obj in object_list %}
                    {
                      "type": "Feature",
                      "properties": {
                        "full_name": "{{ obj.full_name }}",
                        "id": "{{ obj.id }}"
                      },
                      "geometry": {
                        "type": "Point",
                        "coordinates": [{{ obj.x }}, {{ obj.y }}]
                      }
                    }{% if not loop.last %},{% endif %}
                    {% endfor %}
                  ]
                };
                var dataLayer = L.geoJson(data, {
                    onEachFeature: function(feature, layer) {
                        layer.bindPopup(
                            '<a href="' + feature.properties.id + '/">' +
                                feature.properties.full_name +
                            '</a>'
                        );
                    }
                });
                map.addLayer(dataLayer);
            </script>
        </body>
    </html>

Reload again and click a pin.

.. image:: /_static/hello-js-pin-link.png

Commit your map.

.. code-block:: bash

    $ git add .
    $ git commit -m "Made a map on the index page"
    $ git push origin master

Open up ``detail.html`` and make a map there, focus on just that victim.

.. code-block:: html
    :emphasize-lines: 3-6,8,14-23

    <!doctype html>
    <html lang="en">
        <head>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/leaflet.css" />
            <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/leaflet.js"></script>
        </head>
        <body>
            <div id="map" style="width:100%; height:300px;"></div>
            <h1>
                {{ object.full_name }}, a {{ object.age }} year old,
                {{ object.race }} {{ object.gender|lower }} died on {{ object.date }}
                in a {{ object.type|lower }} at {{ object.address }} in {{ object.neighborhood }}.
            </h1>
            <script type="text/javascript">
                var map = L.map('map').setView([{{ object.y }}, {{ object.x }}], 16);
                var osmLayer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 18,
                    attribution: 'Data, imagery and map information provided by <a href="http://www.openstreetmap.org/" target="_blank">OpenStreetMap</a> and contributors.'
                });
                map.addLayer(osmLayer);
                var marker = L.marker([{{ object.y }}, {{ object.x }}]).addTo(map);
            </script>
        </body>
    </html>

Reload a detail page, like the one at `localhost:5000/1/ <http://localhost:5000/1/>`_.

.. image:: /_static/hello-js-detail-map.png

Commit that.

.. code-block:: bash

    $ git add .
    $ git commit -m "Made a map on the detail page"
    $ git push origin master

*********************
Act 5: Hello Internet
*********************

In this final act, we will publish your application to the Internet using
`Frozen Flask <http://pythonhosted.org/Frozen-Flask/>`_, a Python library that saves every page
you've made with Flask as a flat file that can be uploaded to the web. This is an
alternative publishing method that does not require you configure and host an full-fledged Internet
server.

First, use pip to install Frozen Flask from the command line.

.. code-block:: bash

    $ pip install Frozen-Flask

Create a new file called ``freeze.py`` where we will configure what pages it should convert into flat files.

.. code-block:: bash

    # Mac and Linux:
    $ touch freeze.py
    # Windows:
    $ start notepad++ freeze.py

Use your text editor to write a basic Frozen Flask configuration.

.. code-block:: python

    from flask_frozen import Freezer
    from app import app
    freezer = Freezer(app)

    if __name__ == '__main__':
        freezer.freeze()

Now run it from the command line, which will create a new directory called ``build``
filled with a set of flattened files.

.. code-block:: bash

    $ python freeze.py

Use your browser to open up one of the local files in ``build``, rather that visit the
dynamically generated pages we created at ``localhost``.

You will notice that the default Frozen Flask configuration only flatted out ``index.html``, and not all your detail pages our template could generate using the data file.

To flatten those, again edit ``freeze.py`` to give it the instructions it needs to make a page for every record in the source CSV.

.. code-block:: python
    :emphasize-lines: 2,5-8

    from flask_frozen import Freezer
    from app import app, get_csv
    freezer = Freezer(app)

    @freezer.register_generator
    def detail():
        for row in get_csv():
            yield {'row_id': row['id']}

    if __name__ == '__main__':
        freezer.freeze()

Run it again from the command line and notice all the additional pages it made in the ``build`` directory. Try opening one in your browser.

.. code-block:: bash

    $ python freeze.py

Commit all of the flat pages to the repository.

.. code-block:: bash

    $ git add .
    $ git commit -m "Froze my app"
    $ git push origin master

Finally, we will publish these static files to the web using `GitHub's Pages <http://pages.github.com/>`_ feature. All it requires is that we create a new branch in our repository called ``gh-pages`` and push our files up to GitHub there.

.. code-block:: bash

    $ git checkout -b gh-pages # Create the new branch
    $ git merge master # Pull in all the code from the master branch
    $ git push origin gh-pages # Push up to GitHub from your new branch

Now wait a minute or two, then visit ``http://<yourusername>.github.io/first-news-app/build/index.html`` to cross the finish line.

.. image:: /_static/hello-internet.png

.. note::

    If your page does not appear, make sure that you have verified your email address with GitHub. It is required before the site will allow publishing pages. And keep in mind there are many other options for publishing flat files, ranging from `Dropbox <https://en.wikipedia.org/wiki/Dropbox_%28service%29>`_ to `Amazon's S3 service <https://en.wikipedia.org/wiki/Amazon_S3>`_.

So you've built a site. But it's kind of janky looking. The next chapter, which we won't have time for in class,
will show you how to dress it up to look like the `demonstration site <http://ireapps.github.io/first-news-app/build/index.html>`_.

*******************
Epilogue: Hello CSS
*******************

Before you get started, move back to the master branch of your repository.

.. code-block:: bash

    $ git checkout master

The first step is to create a stylesheet in the static directory where `CSS <https://en.wikipedia.org/wiki/Cascading_Style_Sheets>`_
code that controls the design of the page can be stored.

.. code-block:: bash

    # Macs or Linux:
    $ touch static/style.css
    # In Windows fire it up in your text editor right away:
    $ start notepad++ static/style.css

Add the style tag to the top of ``index.html`` so it imported on the page. Flask's built-in ``url_for``
method will create the URL for us.

.. code-block:: html
    :emphasize-lines: 4

    <!doctype html>
    <html lang="en">
        <head>
            <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" />
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/leaflet.css" />
            <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/leaflet.js"></script>
        </head>
        <body>
            <div id="map" style="width:100%; height:300px;"></div>
            <h1>Deaths during the L.A. riots</h1>
            <table border=1 cellpadding=7>
                <tr>
                    <th>Name</th>
                    <th>Date</th>
                    <th>Type</th>
                    <th>Address</th>
                    <th>Age</th>
                    <th>Gender</th>
                    <th>Race</th>
                </tr>
            {% for obj in object_list %}
                <tr>
                    <td><a href="{{ obj.id }}/">{{ obj.full_name }}</a></td>
                    <td>{{ obj.date }}</td>
                    <td>{{ obj.type }}</td>
                    <td>{{ obj.address }}</td>
                    <td>{{ obj.age }}</td>
                    <td>{{ obj.gender }}</td>
                    <td>{{ obj.race }}</td>
                </tr>
            {% endfor %}
            </table>
            <script type="text/javascript">
                var map = L.map('map').setView([34.055, -118.35], 9);
                var osmLayer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 18,
                    attribution: 'Data, imagery and map information provided by <a href="http://www.openstreetmap.org/" target="_blank">OpenStreetMap</a> and contributors.'
                });
                map.addLayer(osmLayer);
                var data = {
                  "type": "FeatureCollection",
                  "features": [
                    {% for obj in object_list %}
                    {
                      "type": "Feature",
                      "properties": {
                        "full_name": "{{ obj.full_name }}",
                        "id": "{{ obj.id }}"
                      },
                      "geometry": {
                        "type": "Point",
                        "coordinates": [{{ obj.x }}, {{ obj.y }}]
                      }
                    }{% if not loop.last %},{% endif %}
                    {% endfor %}
                  ]
                };
                var dataLayer = L.geoJson(data, {
                    onEachFeature: function(feature, layer) {
                        layer.bindPopup(
                            '<a href="' + feature.properties.id + '/">' +
                                feature.properties.full_name +
                            '</a>'
                        );
                    }
                });
                map.addLayer(dataLayer);
            </script>
        </body>
    </html>


Before we start styling the page, let's do a little reorganization of the HTML
to make a little more like a news site.

First, download this `IRE logo <https://raw.githubusercontent.com/ireapps/first-news-app/master/static/irelogo.png>`_
and throw in the ``static`` directory. We'll add that as an image in a new
navigation bar at the top of the site, then zip up the headline and move it above the map with
with a new byline.

.. code-block:: html
    :emphasize-lines: 9-19

    <!doctype html>
    <html lang="en">
        <head>
            <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" />
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/leaflet.css" />
            <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/leaflet.js"></script>
        </head>
        <body>
            <nav>
                <a href="http://first-news-app.readthedocs.org/">
                    <img src="{{ url_for('static', filename='irelogo.png') }}">
                </a>
            </nav>
            <header>
                <h1>These are the 60 people who died during the L.A. riots</h1>
                <div class="byline">
                    By <a href="http://first-news-app.readthedocs.org/">The First News App Tutorial</a>
                </div>
            </header>
            <div id="map" style="width:100%; height:300px;"></div>
            <table border=1 cellpadding=7>
                <tr>
                    <th>Name</th>
                    <th>Date</th>
                    <th>Type</th>
                    <th>Address</th>
                    <th>Age</th>
                    <th>Gender</th>
                    <th>Race</th>
                </tr>
            {% for obj in object_list %}
                <tr>
                    <td><a href="{{ obj.id }}/">{{ obj.full_name }}</a></td>
                    <td>{{ obj.date }}</td>
                    <td>{{ obj.type }}</td>
                    <td>{{ obj.address }}</td>
                    <td>{{ obj.age }}</td>
                    <td>{{ obj.gender }}</td>
                    <td>{{ obj.race }}</td>
                </tr>
            {% endfor %}
            </table>
            <script type="text/javascript">
                var map = L.map('map').setView([34.055, -118.35], 9);
                var osmLayer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 18,
                    attribution: 'Data, imagery and map information provided by <a href="http://www.openstreetmap.org/" target="_blank">OpenStreetMap</a> and contributors.'
                });
                map.addLayer(osmLayer);
                var data = {
                  "type": "FeatureCollection",
                  "features": [
                    {% for obj in object_list %}
                    {
                      "type": "Feature",
                      "properties": {
                        "full_name": "{{ obj.full_name }}",
                        "id": "{{ obj.id }}"
                      },
                      "geometry": {
                        "type": "Point",
                        "coordinates": [{{ obj.x }}, {{ obj.y }}]
                      }
                    }{% if not loop.last %},{% endif %}
                    {% endfor %}
                  ]
                };
                var dataLayer = L.geoJson(data, {
                    onEachFeature: function(feature, layer) {
                        layer.bindPopup(
                            '<a href="' + feature.properties.id + '/">' +
                                feature.properties.full_name +
                            '</a>'
                        );
                    }
                });
                map.addLayer(dataLayer);
            </script>
        </body>
    </html>

Now go into ``style.css`` and toss in some style we've prepared that will
draw in a dark top bar, limit the width of the page and tighten up the rest
of the page.

.. code-block:: css

    body {
        margin: 0 auto;
        padding: 0;
        font-family: Verdana, sans-serif;
        background-color: ##F2EFEC;
        max-width: 1200px;
    }
    nav {
        background-color: #333132;
        width: 100%;
        height: 50px;
    }
    nav img {
        height: 34px;
        padding: 8px;
    }
    header {
        margin: 25px 10px 15px 10px;
        font-family: Times, Times New Roman, serif;
    }
    h1 {
        margin: 0;
        padding: 0;
        font-size: 44px;
        line-height: 50px;
        font-weight: bold;
        font-style: italic;
    	text-shadow: 0.3px 0.3px 0px gray;
        letter-spacing: .01em;
    }
    .byline {
        margin: 6px 0 0 0;
        font-size: 13px;
        font-weight: bold;
    }
    .byline a {
        text-transform: uppercase;
    }
    table {
        border-collapse:collapse;
        margin: 0 0 20px 0;
        border-width: 0;
        width: 100%;
        font-size: 14px;
    }
    th {
        text-align:left;
    }
    tr, td, th {
        border-color: #f2f2f2;
    }
    tr:hover {
        background-color: #f3f3f3;
    }
    p {
        line-height:140%;
    }
    a {
        color: #4591B8;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }

Reload the page and you should see something a little more presentable.

.. image:: /_static/hello-css-desktop.png

The next step is to upgrade the styles to reshape the page on smaller devices
like tablets and phones. This is done using a system known as `responsive design <https://en.wikipedia.org/wiki/Responsive_web_design>`_
and `CSS media queries <https://en.wikipedia.org/wiki/Media_queries>`_ that set different style rules at different device sizes.

First the HTML page needs an extra tag to turn the system on.

.. code-block:: html
    :emphasize-lines: 4

    <!doctype html>
    <html lang="en">
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" />
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/leaflet.css" />
            <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/leaflet.js"></script>
        </head>
        <body>
            <nav>
                <a href="http://first-news-app.readthedocs.org/">
                    <img src="{{ url_for('static', filename='irelogo.png') }}">
                </a>
            </nav>
            <header>
                <h1>These are the 60 people who died during the L.A. riots</h1>
                <div class="byline">
                    By <a href="http://first-news-app.readthedocs.org/">The First News App Tutorial</a>
                </div>
            </header>
            <div id="map" style="width:100%; height:300px;"></div>
            <table border=1 cellpadding=7>
                <tr>
                    <th>Name</th>
                    <th>Date</th>
                    <th>Type</th>
                    <th>Address</th>
                    <th>Age</th>
                    <th>Gender</th>
                    <th>Race</th>
                </tr>
            {% for obj in object_list %}
                <tr>
                    <td><a href="{{ obj.id }}/">{{ obj.full_name }}</a></td>
                    <td>{{ obj.date }}</td>
                    <td>{{ obj.type }}</td>
                    <td>{{ obj.address }}</td>
                    <td>{{ obj.age }}</td>
                    <td>{{ obj.gender }}</td>
                    <td>{{ obj.race }}</td>
                </tr>
            {% endfor %}
            </table>
            <script type="text/javascript">
                var map = L.map('map').setView([34.055, -118.35], 9);
                var osmLayer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 18,
                    attribution: 'Data, imagery and map information provided by <a href="http://www.openstreetmap.org/" target="_blank">OpenStreetMap</a> and contributors.'
                });
                map.addLayer(osmLayer);
                var data = {
                  "type": "FeatureCollection",
                  "features": [
                    {% for obj in object_list %}
                    {
                      "type": "Feature",
                      "properties": {
                        "full_name": "{{ obj.full_name }}",
                        "id": "{{ obj.id }}"
                      },
                      "geometry": {
                        "type": "Point",
                        "coordinates": [{{ obj.x }}, {{ obj.y }}]
                      }
                    }{% if not loop.last %},{% endif %}
                    {% endfor %}
                  ]
                };
                var dataLayer = L.geoJson(data, {
                    onEachFeature: function(feature, layer) {
                        layer.bindPopup(
                            '<a href="' + feature.properties.id + '/">' +
                                feature.properties.full_name +
                            '</a>'
                        );
                    }
                });
                map.addLayer(dataLayer);
            </script>
        </body>
    </html>

Now the ``style.css`` file should be expanded to include media queries
that will drop columns from the table on smaller devices.

.. code-block:: css
    :emphasize-lines: 64-79

    body {
        margin: 0 auto;
        padding: 0;
        font-family: Verdana, sans-serif;
        background-color: ##F2EFEC;
        max-width: 1200px;
    }
    nav {
        background-color: #333132;
        width: 100%;
        height: 50px;
    }
    nav img {
        height: 34px;
        padding: 8px;
    }
    header {
        margin: 25px 10px 15px 10px;
        font-family: Times, Times New Roman, serif;
    }
    h1 {
        margin: 0;
        padding: 0;
        font-size: 44px;
        line-height: 50px;
        font-weight: bold;
        font-style: italic;
    	text-shadow: 0.3px 0.3px 0px gray;
        letter-spacing: .01em;
    }
    .byline {
        margin: 6px 0 0 0;
        font-size: 13px;
        font-weight: bold;
    }
    .byline a {
        text-transform: uppercase;
    }
    table {
        border-collapse:collapse;
        margin: 0 0 20px 0;
        border-width: 0;
        width: 100%;
        font-size: 14px;
    }
    th {
        text-align:left;
    }
    tr, td, th {
        border-color: #f2f2f2;
    }
    tr:hover {
        background-color: #f3f3f3;
    }
    p {
        line-height:140%;
    }
    a {
        color: #4591B8;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    @media (max-width: 979px) {
        tr th:nth-of-type(n+3),
        tr td:nth-of-type(n+3) {
            display:none;
        }
    }
    @media (max-width: 420px) {
        tr th:nth-of-type(n+2),
        tr td:nth-of-type(n+2) {
            display:none;
        }
    }

Reload the page and size down your browser to see how the page should appear
when visited by a mobile phone.

.. image:: /_static/hello-css-mobile.png

We can punch up the map markers by replacing the Leaflet default pins with custom
designs from the `Mapbox's open-source Maki set <https://www.mapbox.com/maki/>`_.

Download `these <https://github.com/ireapps/first-news-app/blob/master/static/marker-24.png>`_ `two <https://github.com/ireapps/first-news-app/blob/master/static/marker-24%402x.png>`_
black pin images and add them to your ``static`` directory.

Now expand our Leaflet JavaScript code to substitute these images for the defaults.

.. code-block:: html
    :emphasize-lines: 70-75,77-79

    <!doctype html>
    <html lang="en">
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" />
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/leaflet.css" />
            <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/leaflet.js"></script>
        </head>
        <body>
            <nav>
                <a href="http://first-news-app.readthedocs.org/">
                    <img src="{{ url_for('static', filename='irelogo.png') }}">
                </a>
            </nav>
            <header>
                <h1>These are the 60 people who died during the L.A. riots</h1>
                <div class="byline">
                    By <a href="http://first-news-app.readthedocs.org/">The First News App Tutorial</a>
                </div>
            </header>
            <div id="map" style="width:100%; height:300px;"></div>
            <table border=1 cellpadding=7>
                <tr>
                    <th>Name</th>
                    <th>Date</th>
                    <th>Type</th>
                    <th>Address</th>
                    <th>Age</th>
                    <th>Gender</th>
                    <th>Race</th>
                </tr>
            {% for obj in object_list %}
                <tr>
                    <td><a href="{{ obj.id }}/">{{ obj.full_name }}</a></td>
                    <td>{{ obj.date }}</td>
                    <td>{{ obj.type }}</td>
                    <td>{{ obj.address }}</td>
                    <td>{{ obj.age }}</td>
                    <td>{{ obj.gender }}</td>
                    <td>{{ obj.race }}</td>
                </tr>
            {% endfor %}
            </table>
            <script type="text/javascript">
                var map = L.map('map').setView([34.055, -118.35], 9);
                var osmLayer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 18,
                    attribution: 'Data, imagery and map information provided by <a href="http://www.openstreetmap.org/" target="_blank">OpenStreetMap</a> and contributors.'
                });
                map.addLayer(osmLayer);
                var data = {
                  "type": "FeatureCollection",
                  "features": [
                    {% for obj in object_list %}
                    {
                      "type": "Feature",
                      "properties": {
                        "full_name": "{{ obj.full_name }}",
                        "id": "{{ obj.id }}"
                      },
                      "geometry": {
                        "type": "Point",
                        "coordinates": [{{ obj.x }}, {{ obj.y }}]
                      }
                    }{% if not loop.last %},{% endif %}
                    {% endfor %}
                  ]
                };
                var blackIcon = L.Icon.extend({
                    options: {
                        iconUrl: "{{ url_for('static', filename='marker-24.png') }}",
                        iconSize: [24, 24]
                    }
                });
                var dataLayer = L.geoJson(data, {
                    pointToLayer: function (feature, latlng) {
                        return L.marker(latlng, {icon: new blackIcon()});
                    },
                    onEachFeature: function(feature, layer) {
                        layer.bindPopup(
                            '<a href="' + feature.properties.id + '/">' +
                                feature.properties.full_name +
                            '</a>'
                        );
                    }
                });
                map.addLayer(dataLayer);
            </script>
        </body>
    </html>

That will restyle the map to look like this.

.. image:: /_static/hello-css-markers.png

Extending this new design to detail page is simply a matter of repeating the steps above.

.. code-block:: html
    :emphasize-lines: 4-5,10-18,28-34

    <!doctype html>
    <html lang="en">
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" />
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/leaflet.css" />
            <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/leaflet.js"></script>
        </head>
        <body>
            <nav>
                <a href="http://first-news-app.readthedocs.org/">
                    <img src="{{ url_for('static', filename='irelogo.png') }}">
                </a>
            </nav>
            <header>
                <h1>{{ object.full_name }}, a {{ object.age }} year old, {{ object.race|lower }} {{ object.gender|lower }} died on {{ object.date }}
        in a {{ object.type|lower }} at {{ object.address }} in {{ object.neighborhood }}.</h1>
            </header>
            <div id="map" style="width:100%; height:300px;"></div>
            <script type="text/javascript">
                var map = L.map('map').setView([{{ object.y }}, {{ object.x }}], 16);
                var osmLayer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 18,
                    attribution: 'Data, imagery and map information provided by <a href="http://www.openstreetmap.org/" target="_blank">OpenStreetMap</a> and contributors.'
                });
                map.addLayer(osmLayer);
                var blackIcon = L.Icon.extend({
                    options: {
                        iconUrl: "{{ url_for('static', filename='marker-24.png') }}",
                        iconSize: [24, 24]
                    }
                });
                var marker = L.marker([{{ object.y }}, {{ object.x }}], {icon: new blackIcon()}).addTo(map);
            </script>
        </body>
    </html>

That should shape up the page like this.

.. image:: /_static/hello-css-detail.png

Now it is time to build out all the pages by running the freeze script that will save all of
the pages again.

.. code-block:: bash

    $ python freeze.py

Commit all of the flat pages to the repository.

.. code-block:: bash

    $ git add .
    $ git commit -m "Froze my restyled app"
    $ git push origin master

Republish your work by going back to the ``gh-pages`` branch and pushing up the code.

.. code-block:: bash

    $ git checkout gh-pages
    $ git merge master
    $ git push origin gh-pages

Now wait a minute or two, then visit ``http://<yourusername>.github.io/first-news-app/build/index.html`` to see
the restyled application.
