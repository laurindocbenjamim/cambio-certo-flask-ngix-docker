# Use a python base image
FROM python:3.12

# Creating a work directory
WORKDIR /big-data-sparkml

# Copy the requirements and install the libraries 
COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip

RUN python -m pip install -r requirements.txt

# copy the entire application code 
COPY . .

# Expose port 5000 to access out application from browser
EXPOSE 5000

# The command to run the Python application 
# On Windows
#CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]
CMD ["python", "app.py"]