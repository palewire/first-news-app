:tocdepth: 2

==============
First News App
==============

A step-by-step guide to publishing a simple news application.

This tutorial will walk you through the process of building an interactive data visualization 
from a structured dataset. You will get hands-on experience in every stage of the development process,
writing Python, HTML and JavaScript and recording it in Git's version control system. 
By the end you will have published your work on the World Wide Web.

This guide was prepared for training sessions of `Investigative Reporters and Editors (IRE) <http://www.ire.org/>`_ 
and the `National Institute for Computer-Assisted Reporting (NICAR) <http://data.nicar.org/>`_
by `Ben Welsh <http://palewi.re/who-is-ben-welsh/>`_. It is still under construction but will debut on February 27 `at the 
2014 CAR Conference in Baltimore, MD <https://ire.org/events-and-training/event/973/1026/>`_.

* Code repository: `https://github.com/ireapps/first-news-app <https://github.com/ireapps/first-news-app>`_
* Demonstration: `http://ireapps.github.io/first-news-app/build/index.html <http://ireapps.github.io/first-news-app/build/index.html>`_
* Documentation: `http://first-news-app.rtfd.org/ <http://first-news-app.rtfd.org/>`_
* Issues: `https://github.com/ireapps/first-news-app/issues <https://github.com/ireapps/first-news-app/issues>`_

******************
What you will make
******************

This tutorial will guide you through the process of publishing an interactive database and map
about the more than 60 people who died during the riots that swept Los Angeles
for five days in 1992. You will repurpose the data from `a Los Angeles Times 
application <http://spreadsheets.latimes.com/la-riots-deaths/>`_ that 
accompanied a story released on the 20th anniversary of the riots.

A working example can be found at `http://ireapps.github.io/first-news-app/build/index.html <http://ireapps.github.io/first-news-app/build/index.html>`_

**********************
Prelude: Prerequisites
**********************

Before you can begin, your computer needs the following tools installed and working 
to participate.

1. A `command-line interface <https://en.wikipedia.org/wiki/Command-line_interface>`_ to interact with your computer
2. A `text editor <https://en.wikipedia.org/wiki/Text_editor>`_ to work with plain text files
3. `Git <http://git-scm.com/>`_ version control software and an account at `GitHub.com <http://www.github.com>`_
4. Version 2.7 of the `Python <http://python.org/download/releases/2.7.6/>`_ programming language
5. The `pip <http://www.pip-installer.org/en/latest/installing.html>`_ package manager and `virtualenv <http://www.virtualenv.org/en/latest/>`_ environment manager for Python

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
<http://www.python.org/download/releases/2.7.6/>`_. In Windows, it's also crucial to make sure that the 
Python program is available on your system's ``PATH`` so it can be called from anywhere on the command line. `This screencast <http://showmedo.com/videotutorials/video?name=960000&fromSeriesID=96>`_ can guide
you through that process.

Python 2.7 is preferred but you can probably find a
way to make most of this tutorial work with other versions if you futz a little.

pip and virtualenv
------------------

The `pip package manager <http://www.pip-installer.org/en/latest/index.html>`_
makes it easy to install open-source libraries that 
expand what you're able to do with Python. Later, we will use it to install everything
needed to create a working web application. 

If you don't have it already, you can get pip by following 
`these instructions <http://www.pip-installer.org/en/latest/installing.html>`_. In Windows, it's necessary to make sure that the 
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

If that doesn't work, `try following this advice <http://www.virtualenv.org/en/latest/virtualenv.html#installation>`_.

****************
Act 1: Hello Git
****************

Start by creating a new development environment with virtualenv. Name it after our application.
(Note that any line in this tutoral that begins with "$" should be run from the command line. And you don't type the "$".)

.. code-block:: bash

    $ virtualenv first-news-app

Jump into the directory it created.

.. code-block:: bash

    $ cd first-news-app

Turn on the virtualenv, which will instruct your terminal to only use those libraries installed
inside its sealed space.

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

Visit `GitHub <http://www.github.com>`_ and create a new public repository named ``first-news-app``.
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
    app = Flask(__name__) # Note the double underscores on each side! You'll see them again.

Now configure Flask to make a page at your site's root URL, where we will publish
the complete list of people who died during the riots using a template called ``index.html``.

.. code-block:: python
    :emphasize-lines: 2, 5-7

    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template('index.html')

Return your command-line interface and create a directory to store your templates in `the default location Flask expects <http://flask.pocoo.org/docs/quickstart/#rendering-templates>`_.

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

Return to ``app.py`` and Configure Flask to boot up a test server when you run it.

.. code-block:: python
    :emphasize-lines: 9-15

    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template('index.html')

    if __name__ == '__main__':
        app.run( 
            host="0.0.0.0",
            port=8000,
            use_reloader=True,
            debug=True,
        )

Don't forget to save your changes. Then run ``app.py`` on the command-line and open up your browser to ``http://localhost:8000`` or ``http://127.0.0.1:8000``.

.. code-block:: bash

    $ python app.py

Now return to the command line and commit your work to your Git repository. (To
get the terminal back up, you will either need to quit out of ``app.py``
by hitting ``CTRL-C``, or open a second terminal and do additional work there. 
If you elect to open a second terminal, which is recommended, make sure to check into the 
virtualenv with the ``activate`` step we used earlier. If you choose to quit out
of ``app.py``, you will need to turn it back on later by calling ``python app.py`` where appropriate.)

.. code-block:: bash

    $ git add .
    $ git commit -m "Flask app.py and first template"

Push it up to GitHub and check out the changes there.

.. code-block:: bash

    $ git push origin master

*****************
Act 3: Hello HTML
*****************

Start over in your ``index.html`` file with a bare-bones HTML document.

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

Download `the comma-delimited file <https://raw.github.com/ireapps/first-news-app/master/static/la-riots-deaths.csv>`_
that will be the backbone of our application and save it there as ``la-riots-deaths.csv``. Add it to your git repository.

.. code-block:: bash

    $ git add static
    $ git commit -m "Added CSV source data"
    $ git push origin master

Open up ``app.py`` in your text editor and use Python's ``csv`` module to access the CSV data.

.. code-block:: python
    :emphasize-lines: 1, 6-8

    import csv
    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    csv_path = './static/la-riots-deaths.csv'
    csv_obj = csv.DictReader(open(csv_path, 'r'))
    csv_list = list(csv_obj)

    @app.route("/")
    def index():
        return render_template('index.html')

    if __name__ == '__main__':
        app.run( 
            host="0.0.0.0",
            port=8000,
            use_reloader=True,
            debug=True,
        )

Next pass the list to your template, ``index.html``, so you can use it there.

.. code-block:: python
    :emphasize-lines: 12-14

    import csv
    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    csv_path = './static/la-riots-deaths.csv'
    csv_obj = csv.DictReader(open(csv_path, 'r'))
    csv_list = list(csv_obj)

    @app.route("/")
    def index():
        return render_template('index.html',
            object_list=csv_list,
        )

    if __name__ == '__main__':
        app.run( 
            host="0.0.0.0",
            port=8000,
            use_reloader=True,
            debug=True,
        )

Make sure to save ``app.py``. Then dump the data out in ``index.html``. This is an example of Flask's templating language `Jinja <http://jinja.pocoo.org/>`_

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

If it isn't already running, return the command line, restart your test server and visit ``http://localhost:8000`` again.

.. code-block:: 

        $ python app.py

Now we'll use Jinja to sculpt the data in ``index.html`` to create `an HTML table <http://www.w3schools.com/html/html_tables.asp>`_ that lists all the names.

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

Pause to reload your browser page. Next expand the table to include a lot more data.

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

Look at your webpage again to see the change. Then commit your work.

.. code-block:: bash

    $ git add .
    $ git commit -m "Created basic table"
    $ git push origin master

Next we're going to create a unique "detail" page dedicated to each person. Start by opening
up ``app.py`` and adding the URL that will help make this happen.

.. code-block:: python
    :emphasize-lines: 16-18

    import csv
    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    csv_path = './static/la-riots-deaths.csv'
    csv_obj = csv.DictReader(open(csv_path, 'r'))
    csv_list = list(csv_obj)

    @app.route("/")
    def index():
        return render_template('index.html',
            object_list=csv_list,
        )

    @app.route('/<number>/')
    def detail(number):
        return render_template('detail.html')

    if __name__ == '__main__':
        app.run( 
            host="0.0.0.0",
            port=8000,
            use_reloader=True,
            debug=True,
        )

Create a new file in your templates directory called ``detail.html`` for it to connect with. 

.. code-block:: bash

    # Macs and Linux:
    $ touch templates/detail.html
    # Windows:
    $ start notepad++ templates/detail.html


Put something simple in it. Then use your browser to visit ``localhost:8000/1/``, ``or localhost:8000/200/`` or any other number.

.. code-block:: html

    Hello World!

To customize the page for each person, we will need to connect the ``number`` in the URL
with the ``id`` column in the CSV data file. First, use Python to transform the data list
we currently have into a dictionary with each records ``id`` value as the key.

.. code-block:: python
    :emphasize-lines: 9

    import csv
    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    csv_path = './static/la-riots-deaths.csv'
    csv_obj = csv.DictReader(open(csv_path, 'r'))
    csv_list = list(csv_obj)
    csv_dict = dict([[o['id'], o] for o in csv_list])

    @app.route("/")
    def index():
        return render_template('index.html',
            object_list=csv_list,
        )

    @app.route('/<number>/')
    def detail(number):
        return render_template('detail.html')

    if __name__ == '__main__':
        app.run( 
            host="0.0.0.0",
            port=8000,
            use_reloader=True,
            debug=True,
        )

Then have the ``detail`` function connect the number from the URL with the corresponding record
in the dictionary and pass it through the template.

.. code-block:: python
    :emphasize-lines: 19-21

    import csv
    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    csv_path = './static/la-riots-deaths.csv'
    csv_obj = csv.DictReader(open(csv_path, 'r'))
    csv_list = list(csv_obj)
    csv_dict = dict([[o['id'], o] for o in csv_list])

    @app.route("/")
    def index():
        return render_template('index.html',
            object_list=csv_list,
        )

    @app.route('/<number>/')
    def detail(number):
        return render_template('detail.html',
            object=csv_dict[number],
        )

    if __name__ == '__main__':
        app.run( 
            host="0.0.0.0",
            port=8000,
            use_reloader=True,
            debug=True,
        )

Now use the person's name in a real HTML document to make a headline in ``detail.html``. 
Reload ``localhost:8000/1/``.

.. code-block:: html

    <!doctype html>
    <html lang="en">
        <head></head>
        <body>
            <h1>{{ object.full_name }}</h1> 
        </body>
    </html>

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

In ``detail.html`` you can use the rest of the data fields to write a sentence about the victim
and print out the summary that's been written in the data file.

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
            <p>{{ object.story }}</p>
        </body>
    </html>

Once again, commit your work.

.. code-block:: bash

    $ git add .
    $ git commit -m "Created a detail page about each victim."
    $ git push origin master

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
            <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.7.1/leaflet.css" />
            <script type="text/javascript" src="http://cdn.leafletjs.com/leaflet-0.7.2/leaflet.js?2"></script>
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
            <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.7.1/leaflet.css" />
            <script type="text/javascript" src="http://cdn.leafletjs.com/leaflet-0.7.2/leaflet.js?2"></script>
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
                var mapquestLayer = new L.TileLayer('http://{s}.mqcdn.com/tiles/1.0.0/map/{z}/{x}/{y}.png', {
                    maxZoom: 18,
                    attribution: 'Data, imagery and map information provided by <a href="http://open.mapquest.co.uk" target="_blank">MapQuest</a>,<a href="http://www.openstreetmap.org/" target="_blank">OpenStreetMap</a> and contributors.',
                    subdomains: ['otile1','otile2','otile3','otile4']
                });
                map.addLayer(mapquestLayer);
            </script>
        </body>
    </html>

Loop through the CSV data and format it as a `GeoJSON <https://en.wikipedia.org/wiki/GeoJSON>`_ object, which Leaflet can easily load.

.. code-block:: html
    :emphasize-lines: 40-59

    <!doctype html>
    <html lang="en">
        <head>
            <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.7.1/leaflet.css" />
            <script type="text/javascript" src="http://cdn.leafletjs.com/leaflet-0.7.2/leaflet.js?2"></script>
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
                var mapquestLayer = new L.TileLayer('http://{s}.mqcdn.com/tiles/1.0.0/map/{z}/{x}/{y}.png', {
                    maxZoom: 18,
                    attribution: 'Data, imagery and map information provided by <a href="http://open.mapquest.co.uk" target="_blank">MapQuest</a>,<a href="http://www.openstreetmap.org/" target="_blank">OpenStreetMap</a> and contributors.',
                    subdomains: ['otile1','otile2','otile3','otile4']
                });
                map.addLayer(mapquestLayer);
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

Add a popup on the map pins that shows the name of the victim.

.. code-block:: html
    :emphasize-lines: 58-62

    <!doctype html>
    <html lang="en">
        <head>
            <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.7.1/leaflet.css" />
            <script type="text/javascript" src="http://cdn.leafletjs.com/leaflet-0.7.2/leaflet.js?2"></script>
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
                var mapquestLayer = new L.TileLayer('http://{s}.mqcdn.com/tiles/1.0.0/map/{z}/{x}/{y}.png', {
                    maxZoom: 18,
                    attribution: 'Data, imagery and map information provided by <a href="http://open.mapquest.co.uk" target="_blank">MapQuest</a>,<a href="http://www.openstreetmap.org/" target="_blank">OpenStreetMap</a> and contributors.',
                    subdomains: ['otile1','otile2','otile3','otile4']
                });
                map.addLayer(mapquestLayer);
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

Now wrap the name in a hyperlink to that person's detail page.

.. code-block:: html
    :emphasize-lines: 58-66

    <!doctype html>
    <html lang="en">
        <head>
            <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.7.1/leaflet.css" />
            <script type="text/javascript" src="http://cdn.leafletjs.com/leaflet-0.7.2/leaflet.js?2"></script>
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
                var mapquestLayer = new L.TileLayer('http://{s}.mqcdn.com/tiles/1.0.0/map/{z}/{x}/{y}.png', {
                    maxZoom: 18,
                    attribution: 'Data, imagery and map information provided by <a href="http://open.mapquest.co.uk" target="_blank">MapQuest</a>,<a href="http://www.openstreetmap.org/" target="_blank">OpenStreetMap</a> and contributors.',
                    subdomains: ['otile1','otile2','otile3','otile4']
                });
                map.addLayer(mapquestLayer);
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

Commit your map.

.. code-block:: bash

    $ git add .
    $ git commit -m "Made a map on the index page"
    $ git push origin master

Open up ``detail.html`` and make a map there, focus on just that victim.

.. code-block:: html
    :emphasize-lines: 3-6,8,15-24

    <!doctype html>
    <html lang="en">
        <head>
            <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.7.1/leaflet.css" />
            <script type="text/javascript" src="http://cdn.leafletjs.com/leaflet-0.7.2/leaflet.js?2"></script>
        </head>
        <body>
            <div id="map" style="width:100%; height:300px;"></div>
            <h1>
                {{ object.full_name }}, a {{ object.age }} year old, 
                {{ object.race }} {{ object.gender|lower }} died on {{ object.date }}
                in a {{ object.type|lower }} at {{ object.address }} in {{ object.neighborhood }}.
            </h1>
            <p>{{ object.story }}</p>
            <script type="text/javascript">
                var map = L.map('map').setView([{{ object.y }}, {{ object.x }}], 16);
                var mapquestLayer = new L.TileLayer('http://{s}.mqcdn.com/tiles/1.0.0/map/{z}/{x}/{y}.png', {
                    maxZoom: 18,
                    attribution: 'Data, imagery and map information provided by <a href="http://open.mapquest.co.uk" target="_blank">MapQuest</a>,<a href="http://www.openstreetmap.org/" target="_blank">OpenStreetMap</a> and contributors.',
                    subdomains: ['otile1','otile2','otile3','otile4']
                });
                map.addLayer(mapquestLayer);
                var marker = L.marker([{{ object.y }}, {{ object.x }}]).addTo(map);
            </script>
        </body>
    </html>

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
you've made with Flask as a flat file that can be uploaded to the web.

First, use pip to install Frozen Flask.

.. code-block:: bash

    $ pip install Frozen-Flask

Create a new file called ``freeze.py`` where we will configure what it should create.

.. code-block:: bash

    # Mac and Linux:
    $ touch freeze.py
    # Windows:
    $ start notepad++ freeze.py

Import a basic Frozen Flask configuration.

.. code-block:: python

    from flask_frozen import Freezer
    from app import app
    freezer = Freezer(app)

    if __name__ == '__main__':
        freezer.freeze()

Run it, which will create a new directory called ``build`` in your project with the saved
files. 

.. code-block:: bash

    $ python freeze.py

Try opening one in your browser. Notice that the default configuration only saved ``index.html``, and not all your
detail pages. Edit ``freeze.py`` to give it the instructions it needs to make a page for every record
in the source CSV.

.. code-block:: python
    :emphasize-lines: 2,5-8

    from flask_frozen import Freezer
    from app import app, csv_list
    freezer = Freezer(app)

    @freezer.register_generator
    def detail():
        for row in csv_list:
            yield {'number': row['id']}

    if __name__ == '__main__':
        freezer.freeze()

Run it again and notice all the additional pages it made in the ``build`` directory.

.. code-block:: bash

    $ python freeze.py

Commit all of the flat pages to the repository.

.. code-block:: bash

    $ git add .
    $ git commit -m "Froze my app"
    $ git push origin master

Finally, we will publish these static files to the web using `GitHub's Pages <http://pages.github.com/>`_ feature. All it
requires is that we create a new branch in our repository called ``gh-pages`` and push our files
up to GitHub there. Keep in mind there are many other options for publishing flat files, ranging from 
`Dropbox <https://en.wikipedia.org/wiki/Dropbox_%28service%29>`_
to `Amazon's S3 service <https://en.wikipedia.org/wiki/Amazon_S3>`_.

.. code-block:: bash

    $ git checkout -b gh-pages
    $ git rebase master
    $ git push origin gh-pages

Now wait a minute or two, then visit ``http://<yourusername>.github.io/first-news-app/build/index.html`` to cross the finish line.

