from django import forms
from django.utils.translation import gettext as _


class Zipforms(forms.Form):
    file = forms.FileField(label=_("Select_file"))