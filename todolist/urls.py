"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework import routers

from user.views import LoginView, RegisterView, TaskView, CategoryListView, CategoryView, TaskDetailView, TaskViewSet, \
    UserViewSet, StateViewSet, CategoryViewSet, logout_view, delete_task

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'users', UserViewSet)
router.register(r'states', StateViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', RedirectView.as_view(url='login/')),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('logout/', logout_view),
    path('register/', RegisterView.as_view()),
    path('dashboard/', login_required(CategoryListView.as_view())),
    path('new_task/', login_required(TaskView.as_view())),
    path('new_category/', login_required(CategoryView.as_view())),
    path('task/<slug:pk>/', login_required(TaskDetailView.as_view())),
    path('task/delete/<int:id>/', login_required(delete_task)),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
