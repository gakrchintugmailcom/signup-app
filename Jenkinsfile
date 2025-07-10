pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    sh '''
                        echo "Building Docker image..."
                        /usr/bin/docker build -t signup-app .
                    '''
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh '''
                        echo "Stopping existing container if any..."
                        /usr/bin/docker rm -f signup || true
                        echo "Running new container..."
                        /usr/bin/docker run -d -p 5000:5000 --name signup signup-app
                    '''
                }
            }
        }
    }
}

