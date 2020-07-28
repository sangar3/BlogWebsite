from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('author','title','text')
    # WIDGET CLASSES
        widget ={
          # Field: Widget name       class name
            'title': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }



class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author','text')
        # WIDGET CLASSES
        widget = {
            # Field: Widget name       class name
            'author': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }




