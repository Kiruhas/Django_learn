from django import forms
 
class UserForm(forms.Form):
    name = forms.CharField(label="Имя")
    age = forms.IntegerField(label="Возраст", min_value=18, max_value=100)
    gender = forms.ChoiceField(choices=((0, "не указан"), (1, "мужской"), (2, "женский")), label="Пол")
    email = forms.CharField(label="E-mail", required=False)