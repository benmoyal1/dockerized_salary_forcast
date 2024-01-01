from django.db import models
import pickle

PICKLE_FILE = 'dataprocessing/pickle_data_models.pkl'


def load_parameters():
    with open(PICKLE_FILE, 'rb') as pkl:
        binary_data = pickle.load(pkl)
    countries = binary_data["countries"]
    years = binary_data["years"]
    educations = binary_data["educations"]
    return countries, educations, years


class LinearRegressionModel(models.Model):
    countries, educations, years = load_parameters()
    COUNTRY_CHOICES = [(country, country) for country in countries]
    EDUCATION_CHOICES = [(edu, edu) for edu in educations]
    YEARS_OF_EXPERIENCE_CHOICES = [(year, year) for year in years]
    country = models.CharField(
        max_length=150,
        choices=COUNTRY_CHOICES,
        default='Israel',
        verbose_name='Country'
    )
    education = models.CharField(
        max_length=150,
        choices=EDUCATION_CHOICES,
        default='BCs',
        verbose_name='Education'
    )
    years_of_education = models.IntegerField(
        choices=YEARS_OF_EXPERIENCE_CHOICES,
        default=0,
        verbose_name='Years of Experience'
    )
