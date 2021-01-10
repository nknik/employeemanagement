from django.contrib import admin
from .models import Manager
from profilee.models import Employee
# Register your models here.
admin.site.register(Manager)
admin.site.register(Employee)