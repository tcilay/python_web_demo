from django.contrib import admin
from . import models


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'login_name', 'password', 'age', 'create_time']

    list_filter = ['name', 'login_name']

    search_fields = ['name', 'login_name']

    list_per_page = 10

    fieldsets = [
        ('base', {'fields': ['id', 'name', 'login_name', 'password', 'age']}),
        ('super', {'fields': ['create_time']})
    ]


admin.sites.site.register(models.User, UserAdmin)
admin.sites.site.register(models.Article)
