from .models import Category, Testimonals

def index_processor(request):
    # about = About.objects.first()
    kategoriyalar=Category.objects.filter(is_active=True).all()
    testimonal = Testimonals.objects.filter(is_active=True).order_by('?')

    context={

        'kategoriyalar': kategoriyalar,
        'testimonal': testimonal,
        # 'about': about,
    }
    return context