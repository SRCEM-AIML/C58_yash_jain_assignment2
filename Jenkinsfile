pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/YASH36638/Multi_app_django.git' 
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t jainym/jenkins .'
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
