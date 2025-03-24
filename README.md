# StudentProject
This is a Dockerized Django project, built and deployed using Jenkins.
It demonstrates basic functionality using static views and templates.

## 📂 Project Structure
C58_yash_jain_assignment2: The main project directory.

home/: Contains views and templates for the first app.

feedback/: Contains views and templates for the second app.

Dockerfile: Configuration for containerizing the application.

Jenkinsfile: CI/CD pipeline configuration for Jenkins.

requirements.txt: Lists the dependencies required for the project.


# How to Run This Project

1. Clone the Repository

    git clone https://github.com/SRCEM-AIML/C58_yash_jain_assignment2.git

    cd C58_yash_jain_assignment2

2. Build the Docker Image

    docker build -t C58_yash_jain_assignment2 .

3. Run the Docker Container
 
    docker run -p 8000:8000 C58_yash_jain_assignment2

4. Access the Application
    Open in your browser: http://127.0.0.1:8000/


