# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

# Copy only the Pipfile and Pipfile.lock into the container
COPY Pipfile Pipfile.lock /app/

# Install any needed packages specified in Pipfile.lock
RUN pip install --upgrade pip && pip install pipenv && pipenv install --deploy --ignore-pipfile

# Copy the rest of the application code into the container
COPY . /app/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the command to run your application
CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
