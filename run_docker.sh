#!/bin/bash
echo "Running Docker Build and Container..."

docker build -t signup-app .

docker rm -f signup || true

docker run -d -p 5000:5000 --name signup signup-app
