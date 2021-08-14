from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='blog.home_view'),
    path('p/<str:slug>/', views.PostDetailView.as_view(), name='blog.post_view'),
    path('random/', views.random_post, name='blog.random_post'),
    path('all', views.AllPostsView.as_view(), name='blog.all_posts'),
]


