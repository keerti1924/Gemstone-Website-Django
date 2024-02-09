"""
URL configuration for sarvatobhadragems project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from .import views,user_login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gems.urls')),
    path('base', views.BASE, name='base'),
    path('', views.Home, name='home'),
    path('about', views.About, name='about'),
    path('accounts/register',user_login.Register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login',user_login.Login, name='login'),
    path('logout', user_login.logout_view, name='logout'),

    path('product', views.products, name='product'),
    path('beads-jewellery', views.beads_jewellery, name='beads_jewellery'),
    path('cabochon', views.cabochon, name='cabochon'),
    path('diamond-products', views.diamond_products, name='diamond_products'),
    path('emerald-gemstone', views.emerald_gemstone, name='emerald_gemstone'),
    path('faceted-stone', views.faceted_stone, name='faceted_stone'),
    path('handicraft-products', views.handicraft_products, name='handicraft_products'),
    path('jewellery', views.jewellery, name='jewellery'),
    path('natural-rough-gemstone', views.natural_rough_gemstone, name='natural_rough_gemstone'),
    path('rashi-ratan', views.rashi_ratan, name='rashi_ratan'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 