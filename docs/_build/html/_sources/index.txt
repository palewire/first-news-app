:tocdepth: 2

==============
First News App
==============

A step-by-step guide to publishing a simple news application.

This tutorial will walk you through the process of building an interactive data visualization 
from a structured dataset. You will get hands-on experience in every stage of the development process,
writing Python, HTML and JavaScript with Git. By the end you will have published your work on the World Wide Web.

This guide was prepared for training sessions of `Investigative Reporters and Editors (IRE) <http://www.ire.org/>`_ 
and the `National Institute for Computer-Assisted Reporting (NICAR) <http://data.nicar.org/>`_
by `Ben Welsh <http://palewi.re/who-is-ben-welsh/>`_. It is still under construction but will debut on February 27 `at the 
2014 CAR Conference in Baltimore, MD <https://ire.org/events-and-training/event/973/1026/>`_.

Resources:

* Code repository: `https://github.com/ireapps/first-news-app <https://github.com/ireapps/first-news-app>`_
* Demonstration: `http://ireapps.github.io/first-news-app/build/index.html <http://ireapps.github.io/first-news-app/build/index.html>`_.
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
4. Version 2.7 of the `Python <http://python.org>`_ programming language
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
<http://www.python.org/download/releases/2.7.6/>`_. Python 2.7 is preferred but you can probably find a
way to make most of this tutorial work with other versions if you futz a little.

pip and virtualenv
------------------

The `pip package manager <http://www.pip-installer.org/en/latest/index.html>`_
makes it easy to install open-source libraries that 
expand what you're able to do with Python. Later, we will use it to install everything
needed to create a working web application. 

If you don't have it already, you can get pip by following 
`these instructions <http://www.pip-installer.org/en/latest/installing.html>`_.
Verify it's installed with the following.

.. code-block:: bash

    $ pip -V

The `virtualenv environment manager <http://www.virtualenv.org/en/latest/>`_
makes it possible to create an isolated corner of your computer where all the different
tools you use to build an application are sealed off. 

It might not be obvious why you need this, but it quickly becomes essential when you need to juggle different tools
for different projects on one computer. By developing your applications inside separate
virtualenv environments, you can use different versions of the same third-party Python libraries without a conflict.
You can also more easily recreate your project on another machine, handy when
you want to copy your code to a server that publishes pages on the Internet.

You can check if virtualenv is installed with the following.

.. code-block:: bash

    $ virtualenv --version

If you don't have it, install it with pip. You might want to use the sudo command 
to put virtualenv in your system's global directories where it can always be called, just
like other common commands like ``ls`` or ``cd``.

.. code-block:: bash

    $ sudo pip install virtualenv

****************
Act 1: Hello Git
****************

Start by creating a new development environment with virtualenv. Name it after our application.

.. code-block:: bash

    $ virtualenv first-news-app

Jump into the directory it created.

.. code-block:: bash

    $ cd first-news-app

Turn on the virtualenv, which will instruct your terminal to only use those libraries installed
inside its sealed space.

.. code-block:: bash

    $ . bin/activate

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

    $ touch README.md

Open up the README in your text editor and type something in it. Maybe something like:

.. code-block:: markdown

    My first news app
    =================

Officially add the file to your repository for tracking with git's ``add`` command.

.. code-block:: bash

    $ git add README.md

Log its creation with git's ``commit`` command.

.. code-block:: bash

    $ git commit -m "First commit"

Push it up to GitHub.

.. code-block:: bash

    $ git push origin master

Reload your repository on GitHub and see your handiwork.

******************
Act 2: Hello Flask
******************

Use pip to install `Flask <http://flask.pocoo.org/>` the Python "microframework"
we'll use to put together our website.

.. code-block:: bash

    $ pip install Flask

Create a new file called ``app.py`` where we will configure Flask.

.. code-block:: bash

    $ touch app.py

Open it with your text editor and import the Flask basics.

.. code-block:: python

    from flask import Flask
    app = Flask(__name__)

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

Create a directory to store your templates in `the default location Flask expects <http://flask.pocoo.org/docs/quickstart/#rendering-templates>`_.

.. code-block:: bash

    $ mkdir templates

Create the ``index.html`` we referenced in ``app.py``.

.. code-block:: bash

    $ touch templates/index.html

Open it up and write something clever.

.. code-block:: html

    Hello World!

Configure Flask to boot up a test server when you run ``app.py``.

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

Run ``app.py`` and open up your browser to ``localhost:8000`` or ``127.0.0.1:8000``.

.. code-block:: bash

    $ python app.py

Commit our work to your Git repository.

.. code-block:: bash

    $ git add .
    $ git commit -m "Flask app.py and first template"

Push it up to GitHub and check out the changes there.

.. code-block:: bash

    $ git push origin master

*****************
Act 3: Hello HTML
*****************

.. code-block:: bash

    $ mkdir static

Download the data file and load it into the template context and dump it into the HTML template

.. code-block:: bash

    $ git add .
    $ git commit -m "Added CSV source data"

Show how GitHub nicely formats CSV in the website

.. code-block:: python
    :emphasize-lines: 1,8,9,11

    import csv
    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    @app.route("/")
    def index():
        csv_path = './static/baltimore-cctv-locations.csv'
        object_list = csv.DictReader(open(csv_path, 'r'))
        return render_template('index.html',
            object_list=object_list,
        )

    if __name__ == '__main__':
        app.run( 
            host="0.0.0.0",
            port=8000,
            use_reloader=True,
            debug=True,
        )

Create basic table in HTML page

.. code-block:: jinja

    <h1>Baltimore CCTV locations</h1>

    <table>
    {% for obj in object_list %}
        <tr>
            <td>{{ obj.number }}</td>
            <td>{{ obj.location }}</td>
            <td>{{ obj.project }}</td>
        </tr>
    {% endfor %}
    </table>

.. code-block:: bash

    $ git add .
    $ git commit -m "Created basic table"

***********************
Act 4: Hello JavaScript
***********************

.. code-block:: html

    <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.7.1/leaflet.css" />
    <script src="http://cdn.leafletjs.com/leaflet-0.7.1/leaflet.js?2"></script>

.. code-block:: html
    :emphasize-lines: 4

    <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.7.1/leaflet.css" />
    <script src="http://cdn.leafletjs.com/leaflet-0.7.1/leaflet.js?2"></script>

    <div id="map" style="width:100%; height:800px;"></div>

.. code-block:: html
    :emphasize-lines: 6-15

    <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.7.1/leaflet.css" />
    <script src="http://cdn.leafletjs.com/leaflet-0.7.1/leaflet.js?2"></script>

    <div id="map" style="width:100%; height:800px;"></div>

    <script type="text/javascript">
        var map = L.map('map').setView([39.295, -76.61219], 14);

        var mapquestLayer = new L.TileLayer('http://{s}.mqcdn.com/tiles/1.0.0/map/{z}/{x}/{y}.png', {
            maxZoom: 18,
            attribution: 'Data, imagery and map information provided by <a href="http://open.mapquest.co.uk" target="_blank">MapQuest</a>,<a href="http://www.openstreetmap.org/" target="_blank">OpenStreetMap</a> and contributors.',
            subdomains: ['otile1','otile2','otile3','otile4']
        });
        map.addLayer(mapquestLayer);
    </script>

.. code-block:: html
    :emphasize-lines: 16-37

    <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.7.1/leaflet.css" />
    <script src="http://cdn.leafletjs.com/leaflet-0.7.1/leaflet.js?2"></script>

    <div id="map" style="width:100%; height:800px;"></div>

    <script type="text/javascript">
        var map = L.map('map').setView([39.295, -76.61219], 14);

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
                "number": {{ obj.number }},
                "location": "{{ obj.location }}",
                "project": "{{ obj.project }}",
              },
              "geometry": {
                "type": "Point",
                "coordinates": [
                  {{ obj.x }},
                  {{ obj.y }}
                ]
              }
            }{% if not loop.last %},{% endif %}
            {% endfor %}
          ]
        };

        var dataLayer = L.geoJson(data, {
            onEachFeature: function(feature, layer) {
                layer.bindPopup(
                    "Camera #" + 
                    feature.properties.number + 
                    "<br>" + 
                    feature.properties.location +
                    "<br>" + 
                    feature.properties.project
                );
            }
        });
        map.addLayer(dataLayer);
    </script>

.. code-block:: html
    :emphasize-lines: 39-40

    <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.7.1/leaflet.css" />
    <script src="http://cdn.leafletjs.com/leaflet-0.7.1/leaflet.js?2"></script>

    <div id="map" style="width:100%; height:800px;"></div>

    <script type="text/javascript">
        var map = L.map('map').setView([39.295, -76.61219], 14);

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
                "number": {{ obj.number }},
                "location": "{{ obj.location }}",
                "project": "{{ obj.project }}",
              },
              "geometry": {
                "type": "Point",
                "coordinates": [
                  {{ obj.x }},
                  {{ obj.y }}
                ]
              }
            }{% if not loop.last %},{% endif %}
            {% endfor %}
          ]
        };

        var dataLayer = L.geoJson(data);
        map.addLayer(dataLayer);
    </script>

.. code-block:: html
    :emphasize-lines: 39-50

    <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.7.1/leaflet.css" />
    <script src="http://cdn.leafletjs.com/leaflet-0.7.1/leaflet.js?2"></script>

    <div id="map" style="width:100%; height:800px;"></div>

    <script type="text/javascript">
        var map = L.map('map').setView([39.295, -76.61219], 14);

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
                "number": {{ obj.number }},
                "location": "{{ obj.location }}",
                "project": "{{ obj.project }}",
              },
              "geometry": {
                "type": "Point",
                "coordinates": [
                  {{ obj.x }},
                  {{ obj.y }}
                ]
              }
            }{% if not loop.last %},{% endif %}
            {% endfor %}
          ]
        };

        var dataLayer = L.geoJson(data, {
            onEachFeature: function(feature, layer) {
                layer.bindPopup(
                    "Camera #" + 
                    feature.properties.number + 
                    "<br>" + 
                    feature.properties.location +
                    "<br>" + 
                    feature.properties.project
                );
            }
        });
        map.addLayer(dataLayer);
    </script>

.. code-block:: bash

    $ git add .
    $ git commit -m "Replaced table with map"

*********************
Act 5: Hello Internet
*********************

.. code-block:: bash

    $ pip install Frozen-Flask

.. code-block:: bash

    $ touch freeze.py

Fill in freeze app

.. code-block:: python

    from flask_frozen import Freezer
    from app import app

    app.config['FREEZER_RELATIVE_URLS'] = True

    freezer = Freezer(app)

    if __name__ == '__main__':
        freezer.freeze()

.. code-block:: bash

    $ python freeze.py

.. code-block:: bash

    $ git add .
    $ git commit -m "Frozen our app"

Open up the frozen page in the browser and point out differences

.. code-block:: bash

    $ git checkout gh-pages
    $ git rebase master
    $ git push origin gh-pages

The big reveal at http://<yourusername>.github.io/first-news-app/build/index.html
