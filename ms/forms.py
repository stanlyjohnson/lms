from django import forms
from .models import *

auth = list(author.objects.all())
choice = tuple(map(lambda x : x.name,auth))


class auth_form(forms.ModelForm):
    name = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'author','height':'100','width':'100'}))
    age = forms.IntegerField(label="",widget=forms.NumberInput(attrs={'placeholder':'No of Halfdays'}))
    country = forms.DateField(label="",widget=forms.TextInput(attrs={'placeholder':'country'}))
    des = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'About author','height':'100','width':'100'}))
    class Meta:
        model = author
        fields = '__all__'

class book_form(forms.ModelForm):
    name = forms.ChoiceField(label="Author",widget=forms.Select(attrs={}),choices = choice)
    title = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Title','height':'100','width':'100'}))
    isbn = forms.SlugField(label="",widget=forms.TextInput(attrs={'placeholder':'ISBN'}))
    des = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'About book','height':'100','width':'100'}))
    class Meta:
        model = author
        fields = '__all__'
