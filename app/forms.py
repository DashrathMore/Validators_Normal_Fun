from typing import Any, Dict
from django import forms
from django.core import validators


def name_valid(value):
    if value[0].lower()=='a':
        raise forms.ValidationError('name starts with a')
    
def name_length(value):
    if len(value)<5:
        raise forms.ValidationError('name length is less than 5')
    
sub=[('python','python'),('java','java'),('web_tech','web_tech'),('django','django'),('sql','sql')]
gen=[('MALE','MALE'),('FEMALE','FEMALE'),('OTHERS','OTHERS')]
class studentlogin(forms.Form):
    sname=forms.CharField(max_length=100,validators=[name_valid, name_length])
    sid=forms.IntegerField()
    sage=forms.IntegerField()
    semail=forms.EmailField(validators=[validators.RegexValidator('^[a-zA-Z0-9]\w*[.]?\w+@gmail[.]com')])
    password=forms.CharField(max_length=12, widget=forms.PasswordInput)
    gender=forms.ChoiceField(choices=gen,widget=forms.RadioSelect)
    #gender=forms.ChoiceField(choices=gen)
    #subjects=forms.MultipleChoiceField(choices=sub)
    subjects=forms.MultipleChoiceField(choices=sub,widget=forms.CheckboxSelectMultiple)


    #phone_number=forms.CharField(max_length=10, validators=[validators.RegexValidator('[6-9]\d{9}')])
    #remail=forms.EmailField()
    botchecker=forms.CharField(max_length=100,widget=forms.HiddenInput, required=False)

    #def clean(self):
      #  se=self.cleaned_data['semail']
       # re=self.cleaned_data['remail']
        #if se != re:
         #   raise forms.ValidationError('email not matced')
    
    
    
    #clean_element method we cant use on normal input element it will give return as none
    # its used to as botchecker a humen entering data from frontend or a autometed softwares inserting data by using source code
    def  clean_botchecker(self):
        bot=self.cleaned_data['botchecker']
        if len(bot)>0:
            raise forms.ValidationError('its not human')
