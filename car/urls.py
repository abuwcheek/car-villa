from django.urls import path
from .views import IndexView, brandView, categoryView, detailView, ContactView


urlpatterns = [
     path('', IndexView, name='index'),
     path('brand/<uuid:uuid>/', brandView, name='brandview'),
     path('category/<uuid:uuid>/', categoryView, name='categoryview'),
     path('car/<uuid:uuid>/', detailView, name='detailview'),
     path('contact/', ContactView.as_view(), name='contactview')
]