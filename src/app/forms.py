from django import forms
from .models import Article, Commentaire, CustomUser

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'published']
        labels = {
            'title': '',
            'content': '',
            'published': 'Publier',
        }

class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_image'].required = False
        self.fields['profile_image'].widget = forms.FileInput()
        
class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['content', 'user', 'article']

