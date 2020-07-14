from django.urls import path
from . import views
from .views import TrangChu
from .views import detail
from .views import detail_famous
from .views import famous_people
from .views import review
from .views import top, famous_like, product_like
from .views import Edit_coment
from .views import Edit_coment_Famous
from django.conf.urls import url
from . import models

# from .views import SearchResult

app_name = 'polls'
urlpatterns = [
    path('', TrangChu.as_view(), name="index"),  # url trang chủ
    path('detail/<int:product_id>', detail.as_view(), name="detail"),  # url trang chi tiết
    path('detail_famous/<int:famous_id>', detail_famous.as_view(), name="detail_famous"),  # url trang chi tiết
    path('review', review.as_view(), name="review"),
    path('top', top.as_view(), name="top"),
    path('famous_people', famous_people.as_view(), name="famous_people"),
    path('search', views.search, name='search'),
    path('famous_like/<int:pk>', views.famous_like, name="famous_like"),
    path('product_like/<int:pk>', views.product_like, name="product_like"),
    path('delete/comment/<int:list_detail_product_id>/<int:comment_id>', views.delete_comment, name='post-delete'),
    path('delete/comment_famous/<int:list_detail_famous_id>/<int:comment_id>', views.delete_comment_famous,name='post-delete-famous'),
    path('edit_comment/<int:comment_id>/<int:list_detail_product_id>', Edit_coment.as_view(), name="edit_comment"),
    path('edit_comment_famous/<int:comment_id>/<int:list_detail_famous_id>', Edit_coment_Famous.as_view(),name="edit_comment_famous"),

]
