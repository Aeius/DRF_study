from django.urls import path
from user import views

urlpatterns = [
    # user/
    path('', views.UserAPIView.as_view()),
]