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
                   env.DOCKER_IMAGE_ID = dockerImage.id

                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'Docker_creds', url: 'https://index.docker.io/v1/']) {
                    sh 'docker tag jainym/jenkins jainym/jenkins:latest'
                    sh 'docker push jainym/jenkins:latest'
                }
            }
        }
    }
}
