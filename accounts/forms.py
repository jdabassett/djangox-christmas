from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import ChildVisitor

class ChildVisitorCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = ChildVisitor
        fields = ('email', 'username',)

class ChildVisitorChangeForm(UserChangeForm):

    class Meta:
        model = ChildVisitor
        fields = ('email', 'username',)