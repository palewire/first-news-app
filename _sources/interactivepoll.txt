Interactive Poll
================

A step-by-step guide for building an interactive poll. Based on
an application designed by `Aron Pilhofer <http://twitter.com/pilhofer>`_, it has been adapted here by `Ben Welsh <http://palewire.com/who-is-ben-welsh/>`_.

.. image:: images/interactivepoll.png

To see a working demonstration of what you'll be building, visit http://palewire.com/nicar/polls/1/

Prelude: Hello Django
---------------------

Before you you can begin work, you need to get your Django environment up and flying. If you havn't
done it already, follow one of our :ref:`getting started guides<gettingstarted>`. 

If you elected to install Bitnami for Windows, you'll need to fire it up by clicking "Use Bitnami DjangoStack"
in the start menu. That should bring up a terminal where you can being work.

.. image:: images/bootingbitnamiwindows.png

Act 1: Hello Database
---------------------

First, create your Django project

.. code-block:: bash

    $ django-admin.py startproject interactive_poll

Jump and start it up for the first time

.. code-block:: bash

    $ cd interactive_poll
    $ python manage.py runserver

If you visit http://localhost:8000 in your browser, you should see Django's "Hello World" page, 
indicating that you've got everything properly configured and are ready to begin work.

Then you start in on your app by first settings your database connection. For this app,
we'll be creating a Sqlite database.

In your settings.py file, replace the default database configuration with::
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'database.db'
        }
    }

Then back in your shell run the following command to create your database. When it asks, be sure to create a superuser. We'll need it later.

.. code-block:: bash

    $ python manage.py syncdb

Now we will create an "application", Django slang for a package of code. We'll call it "polls."

.. code-block:: bash

    $ python manage.py startapp polls

You'll now find a folder called "polls" where we'll be building our app. The models file is where we define our database tables.
Go in there and add the following to the models.py file, which will act as the blueprint for two new tables. ::

    class Project(models.Model):
        title = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')
        active_flag = models.BooleanField()

    class Vote(models.Model):
        project = models.ForeignKey(Project)
        choice = models.IntegerField()

Now return do the settings.py file and add a line to the INSTALLED_APPS list with the name of our new app.

.. code-block:: python
   :emphasize-lines: 12

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        # Uncomment the next line to enable the admin:
        # 'django.contrib.admin',
        # Uncomment the next line to enable admin documentation:
        # 'django.contrib.admindocs',
        'polls',
    )

Sync your database again and your new tables will be created in the database.

.. code-block:: bash

    $ python manage.py syncdb

Act 2: Hello Admin
------------------

Jump back into models.py and add a string representation of your object to the model Project.

.. code-block:: python
   :emphasize-lines: 6,7

    class Project(models.Model):
        title = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')
        active_flag = models.BooleanField()
        
        def __unicode__(self):
            return self.title
  
Go back into settings.py and set ADMIN_MEDIA_PREFIX if it isn't set to this:

.. code-block:: python

   ADMIN_MEDIA_PREFIX = '/static/admin/'

Uncomment "django.contrib.admin" in INSTALLED_APPS

.. code-block:: python
   :emphasize-lines: 9

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        # Uncomment the next line to enable the admin:
        'django.contrib.admin',
        # Uncomment the next line to enable admin documentation:
        # 'django.contrib.admindocs',
        'polls',
    )

Sync the database to create the admin's set of tables.

.. code-block:: bash

    $ python manage.py syncdb

Now go into the urls.py file and uncomment the lines related to the admin, look like so

.. code-block:: python
   :emphasize-lines: 4,5,16

    from django.conf.urls.defaults import patterns, include, url
    
    # Uncomment the next two lines to enable the admin:
    from django.contrib import admin
    admin.autodiscover()
    
    urlpatterns = patterns('',
        # Examples:
        # url(r'^$', 'interactive_poll.views.home', name='home'),
        # url(r'^interactive_poll/', include('interactive_poll.foo.urls')),
        
        # Uncomment the admin/doc line below to enable admin documentation:
        # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
        
        # Uncomment the next line to enable the admin:
        url(r'^admin/', include(admin.site.urls)),
    )

Now fire up the runserver,

.. code-block:: bash

    $ python manage.py runserver

And now log in at http://localhost:8000/admin/, where you'll see Django's generic administration 
system. But you'll notice that your app's database tables aren't in there. 

To add them, create a file called admin.py in the "polls" folder and add the following.

.. code-block:: python

    from polls.models import Project, Vote
    from django.contrib import admin
    
    admin.site.register(Project)
    admin.site.register(Vote)

Now, if you visit http://localhost:8000/admin/ again you should find administration panels
for entering data into the poll's database tables.

For the purposes of this demonstration, I created a poll Project with the title
"Python is the best programming language". When we finish our site, users will be able
vote up or down my claim. Feel free to insert your own title, but drop one or two in there, and check
the active flag, so we have something to work with.

Act 3: Hello Internets
----------------------

First add the following to the top of your settings.py file.

.. code-block:: python

    import os
    settings_dir = os.path.dirname(__file__)

And change the TEMPLATE_DIRS variable.

.. code-block:: python

    TEMPLATE_DIRS = (
        os.path.join(settings_dir, 'templates'),
    )

Then replace all of urls.py file with the following.

.. code-block:: python

    from django.conf.urls.defaults import *
    from django.contrib import admin
    admin.autodiscover()
    
    urlpatterns = patterns('',
        (r'^admin/', include(admin.site.urls)),
        url(r'^$', view='polls.views.index', name='polls_index_view'),
        url(r'^polls/(?P<poll_id>\d+)/$', view='polls.views.detail', name='polls_detail_view'),
        url(r'^polls/(?P<poll_id>\d+)/vote/$', view='polls.views.vote, name='polls_vote_view'),
        url(r'^local-media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT, 'show_indexes': True
        }),
    )

Open up views.py in the polls folder and all all of the following.

.. code-block:: python

    from django.db.models import Sum
    from polls.models import Project, Vote
    from django.views.decorators.csrf import csrf_exempt
    from django.shortcuts import get_object_or_404, render
    from django.http import HttpResponseRedirect, HttpResponse
    
    def index(request):
        projects = Project.objects.all().order_by('-pub_date')[:5]
        return render(request, 'index.html', {
            'projects': projects
        })
    
    def detail(request, poll_id):
        p = Project.objects.get(pk=poll_id)
        total = p.vote_set.aggregate(Sum('choice'))
        return render(request, 'detail.html', {
            'project': p,
            'total': total['choice__sum'],
            'request': request,
        })
    
    @csrf_exempt
    def vote(request, poll_id):
        p = get_object_or_404(Project, pk=poll_id)
        data = request.POST.get("data", None)
        if not data:
            return HttpResponse(status=405)
        if data == "-1":
            value = -1
        else:
            value = 1
        v = p.vote_set.create(choice=value)
        v.save()
        return HttpResponse(status=200)

Create a "templates" folder in the base of your project and create an index.html file in there. Add the following.

.. code-block:: html+django

    {% load url from future %}

    <ul>
    {% for project in projects %}
        <li><a href="{% url "polls_detail_view" %}">{{ project.title }}</a></li>
    {% empty %}
        <p>No projects are available.</p>
    {% endfor %}
    </ul>

Add a detail.html template where it all comes together.

.. code-block:: html+django

    <html>
    <head>
        <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.6.4/jquery.min.js"></script>
        <style type="text/css">
            h3 {margin-bottom:40px;}
            .button { display:inline; background-color: black; color:white; padding:7px; margin: 0 15px; cursor:pointer; }
            .button:hover { background-color:#CCC; }
        </style>
    </head>
    <body>
        <div align="center">
            <h1 id="title">{{ project }}</h1>
            <h3 id="total">Total: {{ total|default_if_none:0 }}</h3>
            <div>
                <div id="yes" class="button">YES</div>
                <div id="no" class="button">NO</div>
            </div>
        </div>
        <script type="text/javascript">
            var currentTotal = {{ total|default_if_none:0 }};
            var vote = function(data) {
                $.ajax({
                  type: 'POST',
                  url: 'http://{{ request.get_host }}/polls/{{ project.id }}/vote/',
                  data: {'data': data}
                });
                currentTotal += data;
                $("#total").html("Total: " + currentTotal.toString());
            };
            $("#yes").click(function() {
                vote(1);
            });
            $("#no").click(function () {
                vote(-1);
            });
        </script>
    </body>
    </html>

Now fire up the runserver and watch it fly in your browser at http://localhost:8000.

.. code-block:: bash

    $ python manage.py runserver


