from django import forms 
from posts.models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields=('title','body','image','status', 'category', 'tags')
