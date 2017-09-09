from .choices import *

class CViewerForm(forms.Form):

    curso = forms.ChoiceField(choices = MY_CHOICES, label="", initial='', widget=forms.Select(), required=True)
