from django.urls import path 
from django.urls.resolvers import URLPattern

from .views import ProfileUpdate

urlpatterns = [ 
    path("profile/", ProfileUpdate.as_view(),name= "profile"),
    path("profile/pqrs", ProfileUpdate.as_view(),name= "pqrs"),
    path("profile/respuesta", ProfileUpdate.as_view(),name= "respuesta"),
 ]