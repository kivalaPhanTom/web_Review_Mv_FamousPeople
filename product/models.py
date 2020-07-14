from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.

class Product(models.Model):
    NT = 'NOTTOP'
    T = 'TOP'
    TOP_CHOICES = [
        (NT, 'Not Top'),
        (T, 'TOP'),
    ]
    like = models.ManyToManyField(User, related_name='product')
    Name_MV = models.CharField(default='', max_length=255)  # tên MV
    content_intro = models.TextField(blank=True, null=True)  # nội dung tả sản phẩm ở trang chủ
    time = models.DateTimeField(default=timezone.datetime.now())
    product_img_intro = models.ImageField(upload_to='images/')  # hình ảnh giới thiệu ở trang chủ
    Check_Attribute_top= models.CharField(  # check trạng thái xem MV đó có ở trạng thái TOp hay không
        max_length=8,
        choices= TOP_CHOICES,
        default=NT,
    )
    def __str__(self):
        return self.Name_MV
    def total_like(self):
        return self.like.count()


class PropertyImage(models.Model):
        product = models.ForeignKey(Product,on_delete=models.CASCADE)
        product_img_detail = models.ImageField(upload_to='images/')
        def __str__(self):
            return "%s - %s " %(self.product.Name_MV, self.product_img_detail)


class PropertyContent(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content_detail= models.TextField(blank=True, null=True)
    def __str__(self):
        return "%s - %s " % (self.product.Name_MV,self.product)


class PropertyTitle(models.Model):
    name_title = models.ForeignKey(Product, on_delete=models.CASCADE)
    TitleName_detail= models.CharField(default='', max_length=255)
    def __str__(self):
        return "%s - %s " % (self.name_title.Name_MV,self.TitleName_detail)

class PropertySinger(models.Model):
    name_singer = models.ForeignKey(Product, on_delete=models.CASCADE)
    SingerName_detail= models.CharField(default='', max_length=255)
    def __str__(self):
        return "%s - %s " % (self.name_singer.Name_MV,self.SingerName_detail)

class PropertyTime(models.Model):
    time = models.ForeignKey(Product, on_delete=models.CASCADE)
    timeDetail = models.DateTimeField(default=timezone.datetime.now())
    def __str__(self):
        return "%s - %s " % (self.time.Name_MV,self.timeDetail)

class PropertyLinkYoutobe(models.Model):
    link = models.ForeignKey(Product, on_delete=models.CASCADE)
    linkSource = models.CharField(default='', max_length=255, blank=True, null=True)
    def __str__(self):
        return "%s - %s " % (self.link.Name_MV,self.linkSource)
class CommentMV(models.Model):
        post = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
        author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        body = models.TextField(blank=True, null=True)
        date = models.DateTimeField(default=timezone.datetime.now())
        reply = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

        def __str__(self):
            return "%s - %s " % (self.post.Name_MV, self.body)

        class Meta:
            # sắp xếp thứ tự commment theo ngày
            ordering = ('date',)

        def children(self):
            return CommentMV.objects.filter(parent=self)

        @property
        def is_parent(self):
            if self.parent is not None:
                return False
            return True