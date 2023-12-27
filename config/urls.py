from django.contrib import admin
from django.urls import path
from .views import HomeView
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('', include("prediction.urls")),

]
