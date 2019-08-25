"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from api.credit_card.views import credit_card_view
from api.credit_card.views import generate_visa_view
from api.credit_card.views import generate_mastercard_view
from api.credit_card.views import generate_discover_view
from api.credit_card.views import generate_american_express_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', credit_card_view),
    path('', credit_card_view),
    path('api/visa/', generate_visa_view),
    path('api/mastercard/', generate_mastercard_view),
    path('api/discover/', generate_discover_view),
    path('api/americanexpress/', generate_american_express_view)
]
