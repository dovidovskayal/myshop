from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from .models import Category, Product, Brand
from .forms import NewsLetterForm, CommentForm
from django.shortcuts import render, get_object_or_404


# def index(request: HttpRequest):
#     categories = Category.objects.all().order_by('name')
#     products = Product.objects.filter(is_published=1).order_by('title')
#     return render(request, 'shop/index.html', {'categories': categories, 'products': products}, status=200)


def error404(request, exception):
    return HttpResponse('<b>404</b>')


def index(request: HttpRequest):
    products = Product.objects.filter().order_by('title')
    error = None
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Ошибка'
    form = NewsLetterForm()
    return render(request,
                  'shop/index.html',
                  {
                      'products': products,
                      'news_letter_form': form,
                      'news_letter_error': error
                  })



def about(request: HttpRequest):
    brands = Brand.objects.all().order_by('name')

    return render(request,
                  'shop/about_us.html',
                  {'brands': brands}
                  )



def product(request: HttpRequest):
    products = Product.objects.all().order_by('title')
    categories = Category.objects.all().order_by('name')
    return render(request,
                  'shop/product.html',
                  {'products': products,
                   'categories': categories}
                  )


class ProductDetailsView(DetailView):
    model = Product
    template_name = 'shop/product_details.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    def post(self, request):
        content = self.get_context_data()
        form = CommentForm(request.POST)
        content['comment_error'] = None
        if form.is_valid():
            form.save()
        else:
            content['comment_error'] = 'Error'
        return self.get(request=request)
