from django import forms


class SearchForm(forms.Form):
    search_text = forms.CharField(label='',max_length=256,widget=forms.TextInput(attrs={'placeholder': 'Search diseases here'}))
    
    