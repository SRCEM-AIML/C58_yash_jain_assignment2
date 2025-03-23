pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('Docker_creds') 
        IMAGE_NAME = "jainym/jenkins:latest" 
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
                   def dockerImage = docker.build("${env.IMAGE_NAME}", "-f Dockerfile .") 
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'Docker_creds') {
                        dockerImage.push('latest')
                    }
                }
            }
        }
    }
}
