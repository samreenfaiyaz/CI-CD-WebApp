# CI-CD-WebApp

Project Overview:
This project is a basic web application developed with FastAPI, designed to display a "Hello, World!" message. It includes a Continuous Integration/Continuous Deployment (CI/CD) pipeline to automate the build, test, and deployment processes.

Editor used: VS code

Project repository Structure: 
1. main.py : The main application code that serves the "Hello, World!" message using FastAPI.
2. .github/workflows/main.yml: The GitHub Actions workflow configuration for CI/CD.
3. test_app.py: Test file for the main application to check the presence of "hello world".

Installation:
1. installed dependendendcies using integrated terminal - FastAPI, Uvicorn, JSON (to work with json responses) .
2. Ran the application locally :
       -navigated to the project directory locally.
       -started the API application.
       - Accessed the application at http://127.0.0.1:8000.
3. Runs test locally:
       -'requests' module installed.
       -Ran tests by command "pytest".
   
CI/CD Pipeline:
       -A GitHub Actions workflow is set up to automate the CI/CD process.
       -On every push to the main branch, the workflow does the following:
             1. Builds the application.
             2. Runs automated tests to check for the presence of "Hello, World!" in the response.

testing Result: successful
refer : 
![image](https://github.com/samreenfaiyaz/CI-CD-WebApp/assets/149583056/648d48dd-255f-4c5b-b96d-eb332fd35bad)


