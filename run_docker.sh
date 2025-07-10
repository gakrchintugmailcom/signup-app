#!/bin/bash
echo "Running Docker Build and Container..."

# Use full path to Docker binary
/usr/bin/docker build -t signup-app .

/usr/bin/docker rm -f signup || true

/usr/bin/docker run -d -p 5000:5000 --name signup signup-app
