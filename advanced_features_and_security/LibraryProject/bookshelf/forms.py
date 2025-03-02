from django import forms

class BookSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False)

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)