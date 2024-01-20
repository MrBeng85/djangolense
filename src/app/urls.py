from django.urls import path
from .views import home, edit, article, delete, acceuil, profile
from blog import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', acceuil, name='app-acceuil'),
    path('home/', home, name='app-home'),
    path('<str:slug>/', article, name='app-article'),
    path('edit/<str:slug>/', edit, name='app-edit'),
    path('delet/<int:pk>/', delete, name='app-delete'),
    path('profile<int:user_id>', profile, name='app-profile'),
    path('profile<int:user_id>/image', profile, name='app-profile-image')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
