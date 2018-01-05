from django import forms
from .models import *

auth = list(author.objects.all())
a = list(map(lambda x : (x.name),auth))
t =[]
choice =[]
for i in a:
    t =[]
    t.append(i)
    t.append(i)
    choice.append(t)


class auth_form(forms.ModelForm):
    name = forms.CharField(label="Name",widget=forms.TextInput(attrs={'placeholder':'author','height':'100','width':'100'}))
    age = forms.IntegerField(label="Age",widget=forms.NumberInput(attrs={'placeholder':'Age'}))
    country = forms.DateField(label="Country",widget=forms.TextInput(attrs={'placeholder':'country'}))
    about = forms.CharField(label="About",widget=forms.TextInput(attrs={'placeholder':'About author','height':'100','width':'100'}))
    class Meta:
        model = author
        fields = ('name','age','country','about')

class book_form(forms.ModelForm):
    writtenby = forms.ChoiceField(label="Author",widget=forms.Select(attrs={}),choices = choice)
    title = forms.CharField(label="title",widget=forms.TextInput(attrs={'placeholder':'Title','height':'100','width':'100'}))
    isbn = forms.SlugField(label="ISBN",widget=forms.TextInput(attrs={'placeholder':'ISBN'}))
    prologue = forms.CharField(label="Prologue",widget=forms.TextInput(attrs={'placeholder':'prologue','height':'100','width':'100'}))
    class Meta:
        model = book
        fields = '__all__'
