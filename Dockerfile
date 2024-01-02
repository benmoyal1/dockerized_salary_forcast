# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --deploy --ignore-pipfile

# Install additional dependencies using pipenv (example: scikit-learn)
RUN pipenv install scikit-learn

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the command to run your application
CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
