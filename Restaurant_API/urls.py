"""
URL configuration for Restaurant_API project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from Food_Items.views import *

router = routers.DefaultRouter()
router.register(r"customers", CustomerViewSet)
router.register(r"drivers", DriverViewSet)
router.register(r"orders", OrderViewSet)
router.register(r"foodItem", FoodItemViewSet)
router.register(r"order_details", Order_DetailsViewSet)
router.register(r"reviews", ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

