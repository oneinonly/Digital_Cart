from django.shortcuts import get_object_or_404, render
from .models import Product
from category.models import Category



# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None
    
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.all().filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
    # all_categories = Category.objects.all()
    context = {
        'products': products,
        'product_count': product_count,
        # 'categories': all_categories,
    }
    return render(request, "store/store.html", context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Product.DoesNotExist:
        from django.http import Http404
        raise Http404("Product matching query does not exist.")
    except Exception as e:
        raise e
    
    context = {
        'single_product': single_product,
    }
    return render(request, "store/product_detail.html", context)
