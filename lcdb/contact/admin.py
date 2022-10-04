from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = []