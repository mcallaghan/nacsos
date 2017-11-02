from django import forms
from .models import *

from tmv_app.models import *


class ProjectForm(forms.ModelForm):
    class Meta:
        model = (Project)
        fields = ('title', 'description',)

class ProjectRoleForm(forms.ModelForm):
    class Meta:
        model = (ProjectRoles)
        fields = ('user', 'role',)

class UpdateProjectRoleForm(forms.ModelForm):
    user = forms.CharField(disabled=True)
    class Meta:
        model = (ProjectRoles)
        fields = ('user', 'role',)
        #widgets = {'user': forms.HiddenInput()}



class TopicModelForm(forms.ModelForm):
    class Meta:
        model = (RunStats)
        fields = ('K','alpha','limit','ngram','max_features','max_iterations')
