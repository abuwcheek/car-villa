from .models import Category, Brands, About

def index_processor(request):
    about = About.objects.first()
    kategoriyalar=Category.objects.filter(is_active=True).all()
    brand = Brands.objects.filter(is_active=True).all()
    sevimlilar = 0
    shopcartproduct_count = 0

    if request.user.is_authenticated:
        sevimlilar = request.user.author_sevimlilar.all().count()
        shopcartproduct_count = request.user.author_shopcart.filter(status=False).all().count()


    context={

        'kategoriyalar': kategoriyalar,
        'brand': brand,
        'about': about,
        'sevimlilar': sevimlilar,
        'shopcartproduct_count': shopcartproduct_count
    }
    return context