from .models import Category, Brands, About

def index_processor(request):
    about = About.objects.first()
    kategoriyalar=Category.objects.filter(is_active=True).all()
    brand = Brands.objects.filter(is_active=True).all()

    context={

        'kategoriyalar': kategoriyalar,
        'brand': brand,
        'about': about,
    }
    return context