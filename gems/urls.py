from django.urls import path,include
from . import views

urlpatterns = [
    path('contact', views.Contact_us, name='contact'),
    path('profile', views.Profile, name='profile'),
    path('profile_update', views.Profile_Update, name='profile_update'),
    path('review', views.Review_Page, name='review'),
    path('add_review/', views.add_review, name='add_review'),
    path('create_review', views.create_review, name='create_review'),
]