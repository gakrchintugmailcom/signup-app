pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'bash -c "docker build -t signup-app ."'
            }
        }

        stage('Run Container') {
            steps {
                sh 'bash -c "docker rm -f signup || true"'
                sh 'bash -c "docker run -d -p 5000:5000 --name signup signup-app"'
            }
        }
    }
}

