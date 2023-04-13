from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.Home.as_view(),name="chat"),
    path('',views.Signup.as_view(),name="signup"),
    path('login/',views.LoginView.as_view(),name="login"),
    path('logout/',views.logoutView,name="logout")
]