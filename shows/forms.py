from django import forms
from .models import Show

class ShowForm(forms.ModelForm):
	class Meta:
		model = Show
		fields = ['title', 'genre', 'rating', 'date_watched', 'notes']
