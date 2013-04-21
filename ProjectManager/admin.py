
from ProjectManager.models import Project, Log, Strength, Weakness, JoinRequest, Question, Answer, Vote
from django.contrib import admin


admin.site.register(Project)
admin.site.register(Log)
admin.site.register(Strength)
admin.site.register(Weakness)
admin.site.register(JoinRequest)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Vote)