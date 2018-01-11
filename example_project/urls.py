from django.urls import path
from app.views import View
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    path('', View.as_view()),
]
