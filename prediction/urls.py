from django.urls import path
from .views import SalaryPredictionView

urlpatterns = [
    path('prediction/', SalaryPredictionView.as_view(), name='salary-prediction'),
]
