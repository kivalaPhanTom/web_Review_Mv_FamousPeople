from django import forms
from .models import CommentMV

class CommentProduct(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.post = kwargs.pop('post', None)
        self.author = kwargs.pop('author', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.author = self.author
        comment.post = self.post
        comment.save()  # lưu vào database

    body = forms.CharField(label="",widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Nhập bình luận của bạn tại đây !!!','rows':'4','cols':'50'}))
    class Meta:
        model =CommentMV
        fields= ["body"]