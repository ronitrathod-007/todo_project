from django import forms

class todo_forms(forms.Form):
	task = forms.CharField(max_length=40,
		widget = forms.TextInput(
		attrs = { 'class': 'form-control', 'placeholder':'Enter '
		}))
