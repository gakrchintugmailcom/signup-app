#!/bin/bash
echo "Running Docker Build and Container..."

export PATH=/usr/bin:/usr/local/bin:$PATH

docker build -t signup-app .

docker rm -f signup || true

docker run -d -p 5000:5000 --name signup signup-app
