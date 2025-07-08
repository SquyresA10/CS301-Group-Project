from django.contrib import admin
from .models import Module, LearningMaterial, Quiz, Question, Progress

# Register your models here.
admin.site.register(Module)
admin.site.register(LearningMaterial)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Progress)
