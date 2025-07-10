pipeline {
    agent any

    environment {
        DOCKER_PATH = "/usr/bin"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    sh '''
                        export PATH=$DOCKER_PATH:$PATH
                        echo "Building Docker image..."
                        docker build -t signup-app .
                    '''
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh '''
                        export PATH=$DOCKER_PATH:$PATH
                        echo "Stopping existing container if any..."
                        docker rm -f signup || true
                        echo "Running new container..."
                        docker run -d -p 5000:5000 --name signup signup-app
                    '''
                }
            }
        }
    }
}
