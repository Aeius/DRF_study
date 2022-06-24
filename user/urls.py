from django.urls import path
from user import views

urlpatterns = [
    # user/
    path('', views.UserAPIView.as_view()),
    path('sign', views.UserSignAPIView.as_view()),
]