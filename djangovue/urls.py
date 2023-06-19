"""
URL configuration for djangovue project.

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
from django.urls import path, include
from listelement.urls import router_listelement, router_category, router_type, router_comment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_listelement.urls)),
    path('api/', include(router_category.urls)),
    path('api/', include(router_type.urls)),
    path('api/', include(router_comment.urls)),
    path('comment/', include('comment.urls'))
]
