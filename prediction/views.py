import pickle
from django.shortcuts import render
from django.views import View
from .forms import LinearRegressionModelForm
import numpy as np
import locale
PICKLE_FILE = 'dataprocessing/pickle_data_models.pkl'

def format_number(y: float) -> str:
    locale.setlocale(locale.LC_ALL, '')
    formatted_float = locale.format_string("%d", y, grouping=True)
    formatted_number_str = f"${formatted_float}"
    return formatted_number_str


def load_models():
    with open(PICKLE_FILE,'rb') as pkl:
        binary_data = pickle.load(pkl)
    decision_tree = binary_data["DecisionTreeRegressor"]
    le_countries = binary_data["le_country"]
    le_educations = binary_data["le_education"]
    return decision_tree, le_educations, le_countries


class SalaryPredictionView(View):
    template_name = 'prediction/salary_predict.html'

    def get(self, request):
        form = LinearRegressionModelForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LinearRegressionModelForm(request.POST)
        if form.is_valid():
            # # Load the linear regression model
            random_forest_reg, le_education, le_country = load_models()

            # Get parameters from the form
            param1 = form.cleaned_data['country']
            param2 = form.cleaned_data['education']
            param3 = form.cleaned_data['years_of_education']

            X = np.array([[param1, param2, param3]])
            X[:, 0] = le_country.transform(X[:, 0])
            X[:, 1] = le_education.transform(X[:, 1])
            X = X.astype(np.float32)

            y_pred = random_forest_reg.predict(X,check_input=False)
            y_pred_str = format_number(y_pred)

            return render(request, self.template_name, {'form': form, 'result': y_pred_str})

        return render(request, self.template_name, {'form': form})
