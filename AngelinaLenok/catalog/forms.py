from django import forms

class Message(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    message = forms.CharField(widget = forms.Textarea, label='Сообщение', max_length=1000)
    widget = forms.Textarea
