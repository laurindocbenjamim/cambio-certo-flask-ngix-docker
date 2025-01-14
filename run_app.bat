@echo off

::echo ======== Building the App Docker Image =========

docker build -t big-data-sparkml .
timeout /t 4

::echo ======== Run the application =========

docker run -p 5000:5000 big-data-sparkml