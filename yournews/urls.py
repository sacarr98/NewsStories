from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create_news/', views.create_news, name='create_news'),
    path('profile_list/', views.profile_list, name='profile_list'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('update_user/', views.update_user, name='update_user'),
    path('news_like/<int:pk>', views.news_like, name='news_like'),
    path('news_display/<int:pk>', views.news_display, name='news_display'),
    path('unfollow/<int:pk>', views.unfollow, name='unfollow'),
    path('delete_post/<int:pk>', views.delete_post, name='delete_post'),
    path('edit_post/<int:pk>', views.edit_post, name='edit_post'),
    path('delete_comment/<int:pk>', views.delete_comment, name='delete_comment'),
    path('search/', views.search, name='search'),
    path('search_user/', views.search_user, name='search_user'),
]