from django.contrib import admin

# Register your models here.
from .models import UserProfile, Company, Attendance

admin.site.register(Company)
admin.site.register(UserProfile)
admin.site.register(Attendance)
