"""FuzzyMatch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
#impporting view methods for an app
from fuzzyStringMatch.views import fuzzySearch, fuzzyAutoComp, getResult

urlpatterns = [
    path('', fuzzySearch, name= 'fuzzySearch'),#Path for the HTML page, where the user enters for word
    path('search/', fuzzyAutoComp, name = 'fuzzyAutoComp'), #On Entering in text box, calls this method to retunautocomplete word suggestions
    path('getResult/', getResult, name='getResult'),#On Click of Submit button, calls this view to return json response
    path('admin/', admin.site.urls), #default admin site
]