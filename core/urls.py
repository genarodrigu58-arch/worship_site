from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('songs/', views.song_list, name='songs'),
    path('announcements/', views.announcement_list, name='announcements'),

    path('posts/', views.posts, name='posts'),  # Vista unificada para ver y crear posts
    path('posts/edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('posts/delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('posts/<int:post_id>/comment/', views.add_comment, name='add_comment'),

    path('profile/edit/', views.edit_profile, name='edit_profile'),

    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', views.manual_logout, name='logout'),
]
