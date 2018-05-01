from django import forms

from .models import Post, Comment

from pagedown.widgets import PagedownWidget



class PostForm(forms.ModelForm):
    body = forms.CharField(widget=PagedownWidget())
    publish = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Post
        fields = ('title', 'slug', 'author' ,'body','publish', 'status', )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
