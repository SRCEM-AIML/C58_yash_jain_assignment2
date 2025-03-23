pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('Docker_creds')
        IMAGE_NAME = "yash36638/multi_app_django:latest"
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/YASH36638/Multi_app_django.git', branch: 'main'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${env.jenkins-python}", "-f Dockerfile .")
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', DOCKERHUB_CREDENTIALS) {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}
