from django import forms
from django.forms import fields
from .models import BlogPost
class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)

class BlogPostModelForm(forms.ModelForm):   # defines subset of BlogPost
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content', 'description']

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title__icontains=title) #__icontains is case insensitive, __iexact is case insensitive
        if qs.exists():
            raise forms.ValidationError("This is not a valid title, It has already been used! Try again.")
        return title
