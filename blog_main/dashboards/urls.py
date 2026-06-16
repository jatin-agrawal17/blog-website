from django.urls import path
from dashboards import views
from dashboards.views import dashboard

urlpatterns = [
    path("", views.dashboard, name = 'dashboard'),
    path("categories/", views.categories, name = 'categories'),
    path("categories/add/", views.add_category, name = 'add_category'),
]