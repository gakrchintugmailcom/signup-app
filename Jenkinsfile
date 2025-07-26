pipeline {
    agent any

    environment {
        IMAGE_NAME = "devops-app"
        TAG = "latest"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git credentialsId: 'github-creds', url: 'https://github.com/gakrchintugmailcom/signup-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$TAG .'
            }
        }

        stage('Push to Local Docker Registry (Optional)') {
            when {
                expression { return false } // Skip if no registry
            }
            steps {
                sh 'docker tag $IMAGE_NAME:$TAG localhost:5000/$IMAGE_NAME:$TAG'
                sh 'docker push localhost:5000/$IMAGE_NAME:$TAG'
            }
        }

        stage('Deploy to Minikube') {
            steps {
                sh '''
                kubectl delete deployment devops-deployment --ignore-not-found
                kubectl apply -f k8s/deployment.yaml
                kubectl apply -f k8s/service.yaml
                '''
        }
stage('Build and Push Docker Image') {
    steps {
        sh 'docker build -t anilsfdcgmailcom/signup-app:latest .'
        sh 'docker login -u anilsfdcgmailcom -p <your-dockerhub-password>'
        sh 'docker push anilsfdcgmailcom/signup-app:latest'
    }
}

        
        }
        
    }
}
