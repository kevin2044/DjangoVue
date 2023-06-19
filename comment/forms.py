from django.forms import ModelForm, Textarea
from .models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': Textarea(attrs = {'class': 'form-input'})
        }
        
    """ def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class':'form-input'}) """
        
    def save(self,commit=True, text=""):
        instance = super(CommentForm, self).save(commit=commit)
        
        if(text == ""):
            instance.text = text
        
        if(commit):
            instance.save()
            
from django import forms
from django.core.validators import MinLengthValidator

class ContactForm(forms.Form):
    """ name = forms.CharField(label='Nombre',initial='Pepe', required=True, disabled=False, help_text="Aqui va tu nombre y no el de tu tia", max_length=10, min_length=3) """
    name = forms.CharField(label='Nombre',validators=[MinLengthValidator(2)])
    """ surname = forms.CharField(label='Apellido', required=False, max_length=10, min_length=3)
    phone = forms.RegexField(label='Telefono',regex='\(\w{3}\)\w{3}-\w{4}',max_length=13, min_length=13)
    date_birth = forms.DateField(label='Fecha de nacimiento') """