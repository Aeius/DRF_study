from django.urls import path
from product import views

urlpatterns = [
    # product/
    path('', views.ProductAPIView.as_view()),
    path('<product_id>/', views.ProductAPIView.as_view())
]