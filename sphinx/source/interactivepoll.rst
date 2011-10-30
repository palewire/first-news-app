Interactive Poll
================

A step-by-step guide for building a Flash-based interactive poll. Based on
an application designed by `Aron Pilhofer <http://twitter.com/pilhofer>`_.

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

Go back into settings.py and uncomment "django.contrib.admin" in INSTALLED_APPS

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

Then set the MEDIA_ROOT variable lower in the file.

.. code-block:: python

    MEDIA_ROOT = os.path.join(settings_dir, 'media')

And change the TEMPLATE_DIRS variable.

.. code-block:: python

    TEMPLATE_DIRS = (
        os.path.join(settings_dir, 'templates'),
    )

Then replace all of urls.py file with the following.

.. code-block:: python

    from django.conf.urls.defaults import *
    from django.conf import settings
    from django.contrib import admin
    admin.autodiscover()
    
    urlpatterns = patterns('',
        (r'^admin/', include(admin.site.urls)),
        url(r'^$', 'polls.views.index'),
        url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
        url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
        url(r'^polls/(?P<poll_id>\d+)/data.xml$', 'polls.views.data'),
        url(r'^crossdomain.xml$', 'polls.views.crossdomain'),
        url(r'^local-media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT, 'show_indexes': True
        }),
    )

Open up views.py in the polls folder and all all of the following.

.. code-block:: python

    from django.shortcuts import get_object_or_404, render
    from polls.models import Project, Vote
    from django.http import HttpResponseRedirect, HttpResponse
    from django.core.urlresolvers import reverse
    from django.db.models import Sum
    from django.views.decorators.csrf import csrf_exempt
    
    def index(request):
        projects = Project.objects.all().order_by('-pub_date')[:5]
        return render(request, 'index.html', {'projects': projects})
    
    def detail(request, poll_id):
        p = Project.objects.get(pk=poll_id)
        total = p.vote_set.count()
        return render(request, 'detail.html', {
            'project': p,
            'vote_total': total, 
            'request': request,
        })
    
    def data(request, poll_id):
        p = Project.objects.get(pk=poll_id)
        total = p.vote_set.aggregate(Sum('choice'))
        return render(request, 'data.xml', {
            'project': p,
            'vote_total': total['choice__sum'],
        }, content_type="text/xml")
    
    @csrf_exempt
    def vote(request, poll_id):
        p = get_object_or_404(Project, pk=poll_id)
        if request.POST['data'] == "0":
            value = -1
        else:
            value = 1
        v = p.vote_set.create(choice = value)
        v.save()
        return HttpResponse(status=200)
    
    def crossdomain(request):
        return HttpResponse('<?xml version=\"1.0\"?><cross-domain-policy><allow-access-from domain=\"*\" /></cross-domain-policy>', mimetype="text/xml")

Create a "templates" folder in the base of your project and create an index.html file in there. Add the following.

.. code-block:: html+django

    {% if projects %}
        <ul>
        {% for project in projects %}
            <li><a href="/polls/{{ project.id }}/">{{ project.title }}</a></li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No projects are available.</p>
    {% endif %}

Add a data.xml template.

.. code-block:: xml+django

    <?xml version="1.0" encoding="UTF-8"?>
    <results>
    <project>{{ project }}</project>
    <totals>{{ vote_total }}</totals>
    </results>

Add a detail.html template where it all comes together.

.. code-block:: html+django

    <div align="center" class="left">
    <object type="application/x-shockwave-flash" data="http://{{ request.get_host }}/local-media/voteinator.swf"
            width="592" height="333">
        <param name="movie" value="http://{{ request.get_host }}/local-media/voteinator.swf"/>
        <param name="FlashVars"
               value="xml_path=http://{{ request.get_host }}/polls/{{ project.id }}/data.xml&post_path=http://{{ request.get_host }}/polls/{{ project.id }}/vote/"/>
        <param name="bgcolor" value="#FFFFFF"/>
        <param name="allowScriptAccess" value="always"/>
        <param name="allowFullScreen" value="true"/>
        <param name="wmode" value="opaque"/>
        <embed src="http://{{ request.get_host }}/local-media/voteinator.swf"
               FlashVars="xml_path=http://{{ request.get_host }}/polls/{{ project.id }}/data.xml&post_path=http://{{ request.get_host }}/polls/{{ project.id }}/vote/"
               bgcolor="#FFFFFF" width="592" height="333" wmode="opaque"
               allowScriptAccess="always" allowFullScreen="true"
               type="application/x-shockwave-flash"></embed>
    </object>
    </div>

Finally, download `votinator.swf <https://github.com/downloads/ireapps/first-news-app/voteinator.swf>`_ and put in a new folder called
"media" is your project's base directory.

Now fire up the runserver and watch it fly in your browser at http://localhost:8000.

.. code-block:: bash

    $ python manage.py runserver


