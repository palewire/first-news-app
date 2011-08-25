from polls.models import Project
from django.contrib import admin

admin.site.register(Project)

from polls.models import Vote
admin.site.register(Vote)
