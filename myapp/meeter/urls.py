from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('register/', views.register_page, name='register_page'),
    path('main/', views.main_page, name='main_page'),
    path('about/<slug:user_slug>/', views.about_page, name='about_page'),
    path('create/', views.create_page, name='create_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
