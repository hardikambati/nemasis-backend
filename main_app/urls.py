from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    # JWT AUTHENTICATION
    path('api/token/', jwt_views.TokenObtainPairView.as_view()),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view()),

    # USER 
    path('signup/', views.RegisterView.as_view()),
    path('user-details/', views.UserDetails.as_view()),
]   