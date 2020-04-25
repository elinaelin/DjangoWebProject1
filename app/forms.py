"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class PoolForm(forms.Form):
    name = forms.CharField(label='Имя',min_length=2,max_length=100)
    city = forms.CharField(label='Город',min_length=2,max_length=100)
    gender = forms.ChoiceField(label='Пол',
                            choices=[('1','Мужской'),('2','Женский')],
                            widget=forms.RadioSelect,initial=1)
    notice = forms.BooleanField(label = 'Хотите получать интересные предложения по E-mail?',
                             required=False)
    email = forms.EmailField(label='Ваш E-mail',min_length=7)
    message = forms.CharField(label='Короткое резюме о себе',
                             widget=forms.Textarea(attrs={'rows':8,'cols':40}))

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text
        widgets = {
            'text':forms.Textarea(attrs={'rows': 10,'class': 'form-control'})
                }

class BlogForm (forms.ModelForm):
    class Meta:
        model = Blog #Используемая модель
        fields = ('title','description','content','posted','author','image',)
        labels = {'title':"Заголовок",'description':"Краткое описание",'content':"Содержание",'posted':"Дата",'author':"Автор",'image':"Изображение"}