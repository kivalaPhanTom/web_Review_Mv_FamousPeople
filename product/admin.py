from django.contrib import admin

# Register your models here.
from .models import *


# #xử lý việc upload nhiều ảnh vào database Django admin
class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

# #xử lý việc upload nhiều content vào database Django admin
class PropertyContentline(admin.StackedInline):
    model = PropertyContent
    extra = 1

class PropertyTitleline(admin.TabularInline):
    model = PropertyTitle
    def get_max_num(self, request, obj=None):
        max_num = 1
        return max_num

class PropertySingerline(admin.TabularInline):
    model = PropertySinger
    def get_max_num(self, request, obj=None):
        max_num = 1
        return max_num

class PropertyTimeline(admin.TabularInline):
    model = PropertyTime
    def get_max_num(self, request, obj=None):
        max_num = 1
        return max_num

class PropertyLinkYoutobeline(admin.TabularInline):
        model = PropertyLinkYoutobe
        def get_max_num(self, request, obj=None):
            max_num = 1
            return max_num

class MyModelAdmin(admin.ModelAdmin):  #gộp 2 thằng trên lại để quản lý
    inlines = [PropertyTitleline,PropertySingerline,PropertyImageInline,PropertyContentline,PropertyTimeline,PropertyLinkYoutobeline]
    def save_model(self, request, obj, form, change):
        obj.save()
        for afile in request.FILES.getlist("photos_multiple"):
            obj.photos.create(image=afile)

admin.site.register(Product, MyModelAdmin)
admin.site.register(CommentMV)

