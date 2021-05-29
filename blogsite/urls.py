from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('postdetail/<int:id>/', views.postdetail, name='postdetail'),
    path('posts', views.allposts, name='allposts'),
    path('register', views.registerPage, name="register"),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    
]
