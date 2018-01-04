from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .models import author,book
# Register your models here.
admin.site.unregister(Group)

class authadmin(admin.ModelAdmin):
    list_display = ['__unicode__','age'
    ]
    class Meta:
        model = author

admin.site.register(author,authadmin)

class bookadmin(admin.ModelAdmin):
    list_display = ['title','__unicode__'
    ]
    class Meta:
        model = book
admin.site.register(book,bookadmin)
