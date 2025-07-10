pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    sh '/usr/bin/docker build -t signup-app .'
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh '/usr/bin/docker rm -f signup || true'
                    sh '/usr/bin/docker run -d -p 5000:5000 --name signup signup-app'
                }
            }
        }
    }
}
