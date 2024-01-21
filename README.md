# Dockerized Salary Forecast

A web application for forecasting the salary of software developers based on their country, education, and experience.

Check it out at [Salary Forecast App](http://ec2-51-20-4-204.eu-north-1.compute.amazonaws.com).

## Django-Salary-Forecast

This project forecasts the salary of a software engineer using a linear regression model based on three parameters: country, education, and experience. The model is trained on data from the [Stack Overflow Developer Survey](https://insights.stackoverflow.com/survey).

The trained model is saved in the `dataprocessing/pickle` directory and is based on the 2020 survey data. You can use data from any other year by running the Jupyter notebook located in the `SalaryPrediction/DataProcessing` directory.


### Building and Running Docker Containers

 1.Open a terminal and navigate to the project directory:
 ```
   cd /path/to/your/project
 ```

 2.Build the docker image
 ```
   docker-compose build
 ```
 3.Run the container
 ```
   docker-compose up
 ```
dont forget to change the host to 127.0.0.1:8000 when choosing to run locally
# dont feel like docker? no prob
just install the requirements.txt with 
```
pip install -r requirements.txt
```
amd then 
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 
``
and enter to localhost:8000 on your machine 


   
