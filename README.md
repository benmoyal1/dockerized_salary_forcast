-# dockerized_salary_forcast
a website forcating software developes dalary accordint totheir countrie education and experience, come check for yourself!
# Django-Salary-Forcast
a web forcasting a salary of a software engineer by 3 parameters with linear regression model
you can download the database yourself here https://insights.stackoverflow.com/survey

the model saved in the dataprocessing/pickle in trained on 2020 but you can any other year by running the jupyther notebook in 
SalaryPrediction/DataProcessing 

make sure you have local mongo database (or any other one)
## Getting Started

To ensure a clean and isolated development environment, it's highly recommended to use a virtual environment.

### Prerequisites

Before you begin, make sure you have Python and pip installed on your system. You can download them from [python.org](https://www.python.org/downloads/).

### Setting up a Virtual Environment
1. Open a terminal and navigate to the project directory:
 ```
cd /path/to/your/project or just open you directory manually -> rightclick -> open with command terminal
 ```

then in order to install the virtual environment insert
```
python -m venv env
```
Activate the virtual environment:

On Windows:
.\env\Scripts\activate
On Unix or MacOS:
  source env/bin/activate
```
pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

in order to have the models in the db first run the jupyter notebook after you downloaded the survey into the dataahndling folder 

### have fun!

