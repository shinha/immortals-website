from django.contrib import admin

# Register your models here.
from .models import Application
from .models import MemberEntry

admin.site.register(Application)
admin.site.register(MemberEntry)