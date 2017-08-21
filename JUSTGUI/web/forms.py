from django import forms


class SettingsForm(forms.Form):

	config = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 80, 'cols': 20}))