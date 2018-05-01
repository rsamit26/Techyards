from django.contrib import admin
from .models import PythonTutorial,GolangTutorial,ProjectEularSolution
# Register your models here.
admin.site.register(PythonTutorial)
admin.site.register(GolangTutorial)
admin.site.register(ProjectEularSolution)