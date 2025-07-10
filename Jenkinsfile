pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/gakrchintugmailcom/signup-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('signup-app')
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh 'docker rm -f signup || true'
                    sh 'docker run -d -p 5000:5000 --name signup signup-app'
                }
            }
        }
    }
}
