from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from accounts.forms import ChildVisitorCreationForm, ChildVisitorChangeForm
from accounts.models import ChildVisitor


class ChildVisitorAdmin(UserAdmin):
    add_form = ChildVisitorCreationForm
    form = ChildVisitorChangeForm
    model = ChildVisitor
    list_display = ['email', 'username',]


admin.site.register(ChildVisitor, ChildVisitorAdmin)
