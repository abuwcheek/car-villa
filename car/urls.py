from django.urls import path
from .views import IndexView, brandView, categorydetailView, detailView, ContactView, SearchView



urlpatterns = [
     path('', IndexView, name='index'),
     path('brand/<uuid:uuid>/', brandView, name='brandview'),
     path('category/<uuid:uuid>/', categorydetailView, name='categoryview'),
     path('car/<uuid:uuid>/', detailView, name='detailview'),
     path('contact/', ContactView.as_view(), name='contactview'),
     path('search/', SearchView.as_view(), name='searchview'),
]