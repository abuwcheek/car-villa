from .models import Category

def index_processor(request):
    # about = About.objects.first()
    kategoriyalar=Category.objects.filter(is_active=True).all()

    context={

        'kategoriyalar': kategoriyalar,
        # 'about': about,
    }
    return context