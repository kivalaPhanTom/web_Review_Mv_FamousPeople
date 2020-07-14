from django import forms
from .models import CommentFaMous

class CommentFamoursFom(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.postFamous = kwargs.pop('postFamous', None)
        self.authorFamous = kwargs.pop('authorFamous', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.authorFamous = self.authorFamous
        comment.postFamous = self.postFamous
        comment.save()  # lưu vào database

    bodyFamous = forms.CharField(label="",widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Nhập bình luận của bạn tại đây !!!','rows':'4','cols':'50'}))
    class Meta:
        model =CommentFaMous
        fields= ["bodyFamous"]