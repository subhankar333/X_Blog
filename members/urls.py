from django.urls import path
from . views import UserRegisterView, UserEditView, ShowProfileView, EditProfileView, CreateProfilePageview
from django.contrib.auth import views as auth_views 
from .import views


urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    path('edit_profile/',UserEditView.as_view(),name='edit_profile'),
    path('password_success/',views.password_success,name='password_success'),
    path('<int:pk>/profile/',ShowProfileView.as_view(),name='view_profile'),
    path('<int:pk>/profile/edit_profile_page',EditProfileView.as_view(),name='edit_profile_page'),
    path('create_profile_page/',CreateProfilePageview.as_view(),name='create_profile_page'),
]
