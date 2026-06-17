from django.urls import path
from account import views

urlpatterns = [
    path('profile/', views.profile_dashboard, name='profile_dashboard'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/add-blog/', views.add_blog, name='add_blog'),
    path('profile/edit-blog/<int:pk>/', views.edit_blog, name='edit_blog'),
    path('profile/delete-blog/<int:pk>/', views.delete_blog, name='delete_blog'),
]