from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.


# Create your models here.
class Famous(models.Model):
    like = models.ManyToManyField(User, related_name= 'famous' )
    famous_title = models.CharField(default='', max_length=255)  # tên tiêu đề và người nổi tiếng
    time1 = models.DateTimeField(default=timezone.datetime.now())
    famous_img = models.ImageField(upload_to='images/')  # hình ảnh giới thiệu về người nổi tiếng ở trang chủ
    def __str__(self):
        return self.famous_title
    def total_like(self):
        return self.like.count()


class PropertyImage(models.Model):
        product = models.ForeignKey(Famous,on_delete=models.CASCADE)
        product_img_detail = models.ImageField(upload_to='images/')
        def __str__(self):
            return "%s - %s " %(self.product.famous_title, self.product_img_detail)


class PropertyContent(models.Model):
    product = models.ForeignKey(Famous, on_delete=models.CASCADE)
    content_detail= models.TextField(blank=True, null=True)
    def __str__(self):
        return "%s - %s " % (self.product.famous_title,self.product)


class PropertyTitle(models.Model):
    name_title = models.ForeignKey(Famous, on_delete=models.CASCADE)
    TitleName_detail= models.CharField(default='', max_length=255)
    def __str__(self):
        return "%s - %s " % (self.name_title.famous_title,self.TitleName_detail)


class PropertyTime(models.Model):
    time1= models.ForeignKey(Famous, on_delete=models.CASCADE)
    timeDetail = models.DateTimeField(default=timezone.datetime.now())
    def __str__(self):
        return "%s - %s " % (self.time1.famous_title,self.timeDetail)


class CommentFaMous(models.Model):
    postFamous = models.ForeignKey(Famous, on_delete=models.CASCADE, related_name='commentsFamous')
    authorFamous = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bodyFamous = models.TextField(blank=True, null=True)
    dateFamous = models.DateTimeField(default=timezone.datetime.now())
    replyFamous = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='repliesFamous')

    def __str__(self):
        return "%s - %s " % (self.postFamous.famous_title, self.bodyFamous)

    class Meta:
        # sắp xếp thứ tự commment theo ngày
        ordering = ('dateFamous',)

    def children(self):
        return CommentFaMous.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True