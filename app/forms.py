from django import forms


def name_valid(value):
    if value[0].lower()=='a':
        raise forms.ValidationError('name starts with a')
    
def name_length(value):
    if len(value)<5:
        raise forms.ValidationError('name length is less than 5')
    


class studentlogin(forms.Form):
    s_name=forms.CharField(max_length=100,validators=[name_valid, name_length])
    s_id=forms.IntegerField()
    s_age=forms.IntegerField()
    s_Email=forms.EmailField(validators=[name_valid])