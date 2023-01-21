from django.urls import path, include
from .views import *


urlpatterns=[path("message/", messages, name="messages"),
             path("correoPadre/",correoPadre, name="correoPadre" ),
             path("showMessage/",showMessages, name="showMessages" ),
             ]