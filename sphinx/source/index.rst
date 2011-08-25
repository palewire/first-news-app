.. Build your first news app with Django documentation master file, created by
   sphinx-quickstart on Wed Aug 24 20:43:20 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Your first news app
===================

A step-by-step guide to building a news application with Django

Resources
---------

 * `Source code <https://github.com/ireapps/first-news-app>`_

Instructions
------------

Create your Django project::

$ django-admin.py startproject interactive_poll

Start it up for the first time::

$ cd nicar2011
$ python manage.py runserver

Set your database connection and syncdb

In settings.py...::

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'database.db'
        }
    }

Then back on the shell::

    $ python manage.py syncdb

Create an application, call it polls::

    $ python manage.py startapp polls

Define two models in models.py::

    class Project(models.Model):
        title = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')
        active_flag = models.BooleanField()

    class Vote(models.Model):
        project = models.ForeignKey(Project)
        choice = models.IntegerField()

Add line to settings.py as an installed app::

    'polls',

Sync your db again::

    $ python manage.py syncdb

Add a string representation of your object to the model Project in models.py::

    def __unicode__(self):
        return self.title

Add your app to settings.py in INSTALLED_APPS::

    'django.contrib.admin',

Sync db to create admin tables::

    $ python manage.py syncdb

Enable admin. in urls.py by uncommenting the following::

    from django.contrib import admin
    admin.autodiscover()

and::

    (r'^admin/', include(admin.site.urls)),

Fire up the server, and log in at http://localhost:8000/admin/::

    $ python manage.py runserver

Add your app to the admin. create a file called admin.py in your project (make joke about conventions), and add::

    from polls.models import Project
    from django.contrib import admin

    admin.site.register(Project)

Add vote to the admin.py file so we can see associations::

    from polls.models import Vote
    admin.site.register(Vote)

Configure your templates and dump the urls for our app into urls.py

First add this to settings.py::

    import os
    settings_dir = os.path.dirname(__file__)
    STATIC_DOC_ROOT = os.path.join(settings_dir, 'media')
    TEMPLATE_DIRS = (
        os.path.join(settings_dir, 'templates'),
    )

Then replace all of urls.py with the following::

    from django.conf.urls.defaults import 
    from django.conf import settings
    from django.contrib import admin
    admin.autodiscover()

    urlpatterns = patterns('',
        (r'^admin/', include(admin.site.urls)),
        (r'^polls/$', 'polls.views.index'),
        (r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
        (r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
        (r'^polls/(?P<poll_id>\d+)/data.xml$', 'polls.views.data'),
        (r'^crossdomain.xml$', 'polls.views.crossdomain'),
        (r'^local-media/(?P<path>.)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT }),
    )

Create a view. in views.py::

    from django.http import HttpResponse

    def index(request):
        return HttpResponse("Hello, world. You're at the poll index.")

Add a new method to your views.py, to see how django passes parameters::

    def detail(request, poll_id):
        return HttpResponse("You're looking at poll %s." % poll_id)

Add a bunch of stuff up at the top of views.py we will need later::

    from django.shortcuts import get_object_or_404, render_to_response
    from polls.models import Project, Vote
    from django.http import HttpResponseRedirect, HttpResponse
    from django.core.urlresolvers import reverse
    from django.db.models import Sum
    from django.views.decorators.csrf import csrf_exempt

In our views.py, let's change our index view to pull some real data::

    def index(request):
        projects = Project.objects.all().order_by('-pub_date')[:5]
        return render_to_response('polls/index.html', {'projects': projects})

Create an index.html file::

    {% if projects %}
        <ul>
        {% for project in projects %}
            <li><a href="/polls/{{ project.id }}/">{{ project.title }}</a></li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No projects are available.</p>
    {% endif %}

Tweak our details method in views.py::

    def detail(request, poll_id):
        p = Project.objects.get(pk=poll_id)
        total = p.vote_set.count()
        return render_to_response('polls/detail.html', {'project': p, 'vote_total': total, })

Add a votes method to views.py::

    def vote(request, poll_id):
        p = get_object_or_404(Project, pk=poll_id)
        v = p.vote_set.create(choice = request.POST['data'])
        v.save()
        return HttpResponse(status=200)

Add a data method to views.py::

    def data(request, poll_id):
        p = Project.objects.get(pk=poll_id)
        total = p.vote_set.aggregate(Sum('choice'))
        return render_to_response('polls/data.xml', {'project': p, 'vote_total': total['choice__sum'], }, mimetype="text/xml")

Create a data.xml file::

    <?xml version="1.0" encoding="UTF-8"?>
    <results>
    <project>{{ project }}</project>
    <totals>{{ vote_total }}</totals>
    </results>

Create a crossdomain.xml method::

    def crossdomain(request):
        return HttpResponse('<?xml version=\"1.0\"?><cross-domain-policy><allow-access-from domain=\"\" /></cross-domain-policy>', mimetype="text/xml")

Create a detail.html template where it all comes together::

    <div align="center" class="left">
        <object type="application/x-shockwave-flash" data="/local-media/voteinator.swf" width="592" height="333">
            <param name="movie" value="/local-media/voteinator.swf"/>
            <param name="FlashVars" value="xml_path=/polls/{{ project.id }}/data.xml&post_path=/polls/{{ project.id }}/vote/"/>
            <param name="bgcolor" value="#FFFFFF"/>
            <param name="allowScriptAccess" value="always"/>
            <param name="allowFullScreen" value="true"/>
            <param name="wmode" value="opaque"/>
            <embed src="/local-media/voteinator.swf" FlashVars="xml_path=/polls/{{ project.id }}/data.xml&post_path=/polls/{{ project.id }}/vote/" bgcolor="#FFFFFF" width="592" height="333" wmode="opaque" allowScriptAccess="always" allowFullScreen="true" type="application/x-shockwave-flash"></embed>
        </object>
    </div>

Download votinator.swf and put in in the "media" directory::

    https://github.com/palewire/nicar2011/blob/master/nicar2011/media/voteinator.swf

Extra credit... it votes up, but not down. how to fix?::

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
