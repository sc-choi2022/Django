from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = 'Title:',
        widget = forms.TextInput(
            attrs = {
                'class' : 'title',
                'placeholder' : 'Enter the title',
            }
        ),
        error_messages={
        'required' : 'Please enter the title'
        }
    )
    content = forms.CharField(
        label = 'Contents:',
        widget = forms.Textarea(
            attrs = {
                'class' : 'content',
                'placeholder' : 'Enter the contents',
                'rows' : 10,
                'cols' : 50,
            }
        ),
        error_messages={
            'required' : 'Please enter the content'
        }
    )

    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title,)