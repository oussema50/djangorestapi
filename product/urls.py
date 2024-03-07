from django.urls import path
from . import views
urlpatterns = [
    path('all/', views.products, name='allProducts' ),
    path('<int:id>', views.getProductById, name='getProductById' ),
]