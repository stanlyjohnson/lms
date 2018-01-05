from django import forms
from .models import *




class auth_form(forms.ModelForm):
    name = forms.CharField(label="Name",widget=forms.TextInput(attrs={'placeholder':'author','height':'100','width':'100'}))
    age = forms.IntegerField(label="Age",widget=forms.NumberInput(attrs={'placeholder':'Age'}))
    country = forms.CharField(label="Country",widget=forms.TextInput(attrs={'placeholder':'country'}))
    about = forms.CharField(label="About",widget=forms.TextInput(attrs={'placeholder':'About author','height':'100','width':'100'}))
    class Meta:
        model = author
        fields = ('name','age','country','about')

class book_form(forms.ModelForm):
    writtenby = forms.ModelChoiceField(queryset=author.objects.all(), empty_label="Nothing")
    title = forms.CharField(label="title",widget=forms.TextInput(attrs={'placeholder':'Title','height':'100','width':'100'}))
    isbn = forms.SlugField(label="ISBN",widget=forms.TextInput(attrs={'placeholder':'ISBN'}))
    prologue = forms.CharField(label="Prologue",widget=forms.TextInput(attrs={'placeholder':'prologue','height':'100','width':'100'}))
    class Meta:
        model = book
        fields = '__all__'
