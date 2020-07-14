from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template.backends import django
from django.views import View
from product.models import Product,CommentMV
from famous_people.models import Famous
from famous_people.models import CommentFaMous
from product.forms import CommentProduct
from famous_people.forms import CommentFamoursFom
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain
from django.urls import reverse


# Create your views here.
def product_like(request,pk):
    product = get_object_or_404(Product, id=request.POST.get('product_id'))
    user = request.user
    if user not in product.like.all():
        product.like.add(user)
    else:
        product.like.remove(user)
    return HttpResponseRedirect(reverse('polls:detail', args=[str(pk)]))





def famous_like(request, pk):
    famous = get_object_or_404(Famous, id=request.POST.get('famous_id'))
    user= request.user
    if user not in famous.like.all():
        famous.like.add(user)
    else:
        famous.like.remove(user)
    return HttpResponseRedirect(reverse('polls:detail_famous', args =[str(pk)]))





class TrangChu(View):
    def get(self, request):
        List_Product_ReView = Product.objects.all()[::-1]  # lấy tất cả các object ra (lấy tất cả phần tử)
        List_Famous = Famous.objects.all()[::-1]

        List_TOP_MV = Product.objects.filter(
            Check_Attribute_top='TOP')  # lọc ra những phần tử có Check_Attribute_top='TOP' trong list Product
        Reverse_List_TOP_MV = List_TOP_MV[::-1]  # đảo ngược lại toàn bộ phần tử vừa lấy ra bên trên

        context = {"reverse_list_top": Reverse_List_TOP_MV, "listProDuct_review": List_Product_ReView,
                   "ListFamous": List_Famous, "list_data_search": list_data_search}
        return render(request, "polls/trangchu.html", context)


class detail(View):
    def get(self, request, product_id):
        listDetail_Product = Product.objects.get(pk=product_id)
        comments = CommentMV.objects.filter(post=listDetail_Product, reply=None).order_by('-id')
        formComentProduct = CommentProduct()
        total_like = listDetail_Product.total_like
        user = request.user
        like =0
        if user.is_authenticated:
            like = 0
            if user not in listDetail_Product.like.all():
                like = 1
            else:
                like = 0


        context = {'comments':comments,'list_detail_product': listDetail_Product, "list_data_search": list_data_search,'like':like, 'total_like':total_like,'formComentProduct': formComentProduct}
        return render(request, "polls/detail.html", context)

    def post(self, request, product_id):
        post = get_object_or_404(Product, pk=product_id)
        formComentProduct = CommentProduct(request.POST, author=request.user, post=post)
        if formComentProduct.is_valid():
                body=request.POST.get('body')
                parent_id = request.POST.get('parent_id')# lấy được id của thằng cmt cha
                print("parent:",  parent_id )
                comment_qs = None
                if parent_id :
                    comment_qs = CommentMV.objects.get(id=parent_id)
                comment=CommentMV.objects.create(post=post,author=request.user,body=body, reply=comment_qs)
                comment.save()

        return HttpResponseRedirect(request.path)

def delete_comment(request,list_detail_product_id,comment_id): # chức năng xóa bình luận
    cmt = get_object_or_404(CommentMV, pk=comment_id)
    cmt.delete() # xóa đi bài viết có id đã lấy được
    b= str(list_detail_product_id) # ép kiểu id của bình luận từ int sang string
    a= '/detail/'+b  # '/detail/'+ b sẽ ra link bài viết hiên tại
    return HttpResponseRedirect(a)


class Edit_coment(View):
    def get(self, request, comment_id, list_detail_product_id):
        list_detail_product_id = Product.objects.get(pk=list_detail_product_id)
        post = CommentMV.objects.get(pk=comment_id)
        formComentProduct = CommentProduct(instance=post)
        context = {'post': post, 'formComentProduct': formComentProduct,
                   'list_detail_product_id': list_detail_product_id, "list_data_search": list_data_search}
        return render(request, "polls/edit_comment.html", context)

    def post(self, request, comment_id, list_detail_product_id):
        post = CommentMV.objects.get(pk=comment_id)
        b = str(list_detail_product_id)  # ép kiểu id của bình luận từ int sang string
        a = '/detail/' + b  # '/detail/'+ b sẽ ra link bài viết hiên tại

        if request.method == 'POST':
            formComentProduct = CommentProduct(request.POST, author=request.user, instance=post.post)
            if formComentProduct.is_valid():
                formComentProduct.save()

                post.body = request.POST.get('body')
                post.save()
                print("sdsdsd:", request.POST.get('body'))

                return HttpResponseRedirect(a)

class detail_famous(View):
    def get(self, request, famous_id):
        list_detail_famous = Famous.objects.get(pk=famous_id)  # lấy tất cả các object ra (lấy tất cả phần tử)
        comments = CommentFaMous.objects.filter(postFamous=list_detail_famous, replyFamous=None).order_by('-id')
        formComentFamous = CommentFamoursFom()
        total_like = list_detail_famous.total_like
        user = request.user
        like=0
        if user. is_authenticated:
            like =0
            if user not in list_detail_famous.like.all():
                like = 1
            else:
                like = 0

        context = { 'comments': comments,"List_Detail_Famous": list_detail_famous, "list_data_search": list_data_search, "total_like": total_like, 'like':like,'formComentFamous': formComentFamous}
        return render(request, "polls/detail_famous.html", context)

    def post(self, request, famous_id):
        post = get_object_or_404(Famous, pk=famous_id)
        formComentFamous = CommentFamoursFom(request.POST, authorFamous=request.user, postFamous=post)
        if formComentFamous.is_valid():
            body = request.POST.get('bodyFamous')
            parent_id = request.POST.get('parent_id')  # lấy được id của thằng cmt cha
            print("parent:", parent_id)
            comment_qs = None
            if parent_id:
                comment_qs = CommentFaMous.objects.get(id=parent_id)
            comment = CommentFaMous.objects.create(postFamous=post, authorFamous=request.user, bodyFamous=body,
                                                   replyFamous=comment_qs)
            comment.save()

        return HttpResponseRedirect(request.path)

def delete_comment_famous(request, list_detail_famous_id, comment_id):  # chức năng xóa bình luận
    cmt = get_object_or_404(CommentFaMous, pk=comment_id)
    cmt.delete()  # xóa đi bài viết có id đã lấy được
    b = str(list_detail_famous_id)  # ép kiểu id của bình luận từ int sang string
    print("b",b)
    a = '/detail_famous/' + b  # '/detail_famous/'+ b sẽ ra link bài viết hiên tại
    return HttpResponseRedirect(a)


class Edit_coment_Famous(View):
    def get(self, request, comment_id, list_detail_famous_id):
        list_detail_famous_id = Famous.objects.get(pk=list_detail_famous_id)
        post = CommentFaMous.objects.get(pk=comment_id)
        formComentFamous = CommentFamoursFom(instance=post)
        context = {'post':post,'formComentFamous':formComentFamous,'list_detail_famous_id':list_detail_famous_id,"list_data_search": list_data_search}
        return render(request, "polls/edit_comment_famous.html", context)

    def post(self, request, comment_id, list_detail_famous_id):
        post = CommentFaMous.objects.get(pk=comment_id)
        b = str(list_detail_famous_id)  # ép kiểu id của bình luận từ int sang string
        a = '/detail_famous/' + b  # '/detail/'+ b sẽ ra link bài viết hiên tại

        if request.method == 'POST':
            formComentFamous = CommentFamoursFom(request.POST, authorFamous=request.user, instance=post.postFamous)
            if formComentFamous.is_valid():
                formComentFamous.save()

                post.bodyFamous = request.POST.get('bodyFamous')
                post.save()
                print("sdsdsd:", request.POST.get('bodyFamous'))
                return HttpResponseRedirect(a)


class famous_people(View):
    def get(self, request):
        List_Famous = Famous.objects.all()
        Reverse_List_Famous = List_Famous[::-1]  # đẩo ngược list
        a = Reverse_List_Famous[6:]  # loại bỏ 6 phần tử đầu tiên khỏi list, chính là 6 phần nổi nổi bật
        h = len(List_Famous)  # chiều dài của list  List_Famous
        last_element = Famous.objects.all()[h - 1]  # tìm ra phần tử cuối cùng
        next_last_element1 = Famous.objects.all()[h - 2]  # tìm ra phần tử kề cuối cùng
        next_last_element2 = Famous.objects.all()[h - 3]  # tìm ra phần tử kề next_last_element1
        next_last_element3 = Famous.objects.all()[h - 4]  # tìm ra phần tử kề next_last_element3
        next_last_element4 = Famous.objects.all()[h - 5]  # tìm ra phần tử kề next_last_element3
        next_last_element5 = Famous.objects.all()[h - 6]  # tìm ra phần tử kề next_last_element3
        n = 0
        listTime = []
        for i in a:  # tính ra time delay của từng phần tử
            n = n + 0.2
            listTime.append(n)
        b = list(zip(a, listTime))  # gom 2 list a và Listime
        paginator = Paginator(b, 9)  # một trang chỉ xuất hiện 9 phần tử
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)

        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context = {'page': page, 'items': posts, "b": b, "n": listTime, "ListFamous": a, "last": last_element,
                   "last1": next_last_element1, "last2": next_last_element2, "last3": next_last_element3,
                   "last4": next_last_element4, "last5": next_last_element5, "list_data_search": list_data_search}
        return render(request, "polls/famous_people.html", context)


class review(View):
    def get(self, request):

        List_reviewMV = Product.objects.all()  # lấy ra hết tất cả các phần tử trong model Product
        Reverse_List_ReView = List_reviewMV[::-1]  # đảo ngược lại toàn bộ phần tử vừa lấy ra bên trên
        a = Reverse_List_ReView[
            3:]  # loại bỏ 3 phần tử đầu tiên khỏi list Reverse_List_ReView, chính là 3 phần tử nổi nổi bật
        h = len(List_reviewMV)  # chiều dài của list  List_reviewMV
        last_element = Product.objects.all()[h - 1]  # tìm ra phần tử cuối cùng
        next_last_element1 = Product.objects.all()[h - 2]  # tìm ra phần tử kề cuối cùng
        next_last_element2 = Product.objects.all()[h - 3]  # tìm ra phần tử kề next_last_element1
        n = 0
        listTime = []
        for i in a:  # tính ra time delay của từng phần tử
            n = n + 0.2
            listTime.append(n)
        b = list(zip(a, listTime))  # gom 2 list a và Listime

        paginator = Paginator(b, 9)  # một trang chỉ xuất hiện 9 phần tử
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)

        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context = {'page': page, 'items': posts, "b": b, "reverse_list": Reverse_List_ReView, "last": last_element,
                   "last1": next_last_element1, "last2": next_last_element2, "list_data_search": list_data_search}
        return render(request, "polls/review.html", context)


class top(View):
    def get(self, request):

        List_TOP_MV = Product.objects.filter(
            Check_Attribute_top='TOP')  # lọc ra những phần tử có Check_Attribute_top='TOP' trong list Product
        print("top:", List_TOP_MV)
        Reverse_List_TOP_MV = List_TOP_MV[::-1]  # đảo ngược lại toàn bộ phần tử vừa lấy ra bên trên
        a = Reverse_List_TOP_MV[3:]  # loại bỏ 3 phần tử đầu tiên khỏi list, chính là 3 phần nổi nổi bật
        h = len(List_TOP_MV)  # chiều dài của list  List_Famous
        print("top:", h)
        last_element = Product.objects.filter(Check_Attribute_top='TOP')[h - 1]  # tìm ra phần tử cuối cùng
        print("last:", last_element)
        next_last_element1 = Product.objects.filter(Check_Attribute_top='TOP')[h - 2]  # tìm ra phần tử kề cuối cùng
        next_last_element2 = Product.objects.filter(Check_Attribute_top='TOP')[
            h - 3]  # tìm ra phần tử kề next_last_element1
        n = 0
        listTime = []
        for i in a:  # tính ra time delay của từng phần tử
            n = n + 0.2
            listTime.append(n)
        b = list(zip(a, listTime))  # gom 2 list a và Listime
        paginator = Paginator(b, 9)  # một trang chỉ xuất hiện 9 phần tử
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)

        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context = {'page': page, 'items': posts, "b": b, "a": List_TOP_MV, "reverse_list_top": Reverse_List_TOP_MV,
                   "last": last_element, "last1": next_last_element1, "last2": next_last_element2,
                   "list_data_search": list_data_search}
        return render(request, "polls/top.html", context)


def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')  # lấy dược những gì đã gõ trên ô search
        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(Name_MV__icontains=query) | Q(content_intro__icontains=query)
            lookups2 = Q(famous_title__icontains=query)

            results = Product.objects.filter(lookups).distinct()
            results2 = Famous.objects.filter(lookups2).distinct()

            b = list(chain(results, results2))

            paginator = Paginator(b, 9)  # một trang chỉ xuất hiện 9 phần tử
            page = request.GET.get('page')

            try:
                posts = paginator.page(page)
            except PageNotAnInteger:
                posts = paginator.page(1)

            except EmptyPage:
                posts = paginator.page(paginator.num_pages)

            context = {'page': page, 'items': posts, "b": b, 'results': results, 'results2': results2
                , 'submitbutton': submitbutton, "list_data_search": list_data_search,
                       "list_data_search": list_data_search}

            return render(request, 'polls/SearchView.html', context)

        else:
            return render(request, 'polls/SearchView.html')

    else:
        return render(request, 'polls/SearchView.html')


listProduct = []
ListFamous = []

for e in Product.objects.all():  # tìm tất cả tên MV trong model Product
    listProduct.append(e.Name_MV)
for e1 in Famous.objects.all():  # tìm tất cả tên bài viết của mục người nổi tiếng trong model Famous
    ListFamous.append(e1.famous_title)

list_data_search = listProduct + ListFamous  # gộp 2 thằng bên trên lại, ta có dữ liệu để search sugesstion khi nhập vào ô search, sau đó ta sẽ truyền biến này qua bên file JS
#print(list_data_search)
