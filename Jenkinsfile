// Docker file
// FROM jenkins/jenkins:lts

// USER root
// RUN apt-get update && apt-get install -y python3 python3-venv

// USER jenkins
pipeline {
    agent {
        docker {
            image 'jenkins/jenkins:lts' // Specify the Docker image to use
        }
    }

    stages {
        stage('Checkout') {
            steps {
                // Clone the repository
                git url: 'https://github.com/YASH36638/Multi_app_django.git'
            }
        }

        stage('Build') {
            steps {
                // Placeholder for build commands
                sh 'echo "Building the application..."'
            }
        }

        stage('Test') {
            steps {
                // Placeholder for test commands
                sh 'echo "Running tests..."'
            }
        }

        stage('Deploy') {
            steps {
                // Placeholder for deployment commands
                sh 'echo "Deploying application..."'
            }
        }
    }

    post {
        always {
            // Cleanup or notifications can go here
            sh 'echo "Pipeline completed!"'
        }
        success {
            echo 'Pipeline finished successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
