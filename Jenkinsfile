// Docker file
// FROM jenkins/jenkins:lts

// USER root
// RUN apt-get update && apt-get install -y python3 python3-venv

// USER jenkins
pipeline {
    agent { docker { image 'jenkins/jenkins:lts' } }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/YASH36638/Multi_app_django.git'
            }
        }

        stage('Build') {
            steps {
                sh 'echo "Building the application..."'
            }
        }

        stage('Test') {
            steps {
                sh 'echo "Running tests..."'
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo "Deploying application..."'
            }
        }
    }
}
