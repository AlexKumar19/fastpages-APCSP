---
toc: true
layout: post
description: Deploying our AWS server to become accesible through https web traffic!
title: AWS Deployment
categories: [markdown, csp]
permalink: /AWSDeploymentpublic/
---
# Docker!

Me and my group was able to create four different containers that are each bound to 8080 inside the container with a unique port outside the container for each site. Each website also has a unique image!
![]({{site.baseurl}}/images/BENLEE.png)

<br>

Next we tested to see if we were able to display the websites inside of the container that we made!
![]({{site.baseurl}}/images/curl.png)

<br>

This is the process of pulling from my flask and then updating the website on AWS!
![]({{site.baseurl}}/images/pull.png)

<br>

Here is me using curl command to show the website inside of the AWS terminal!
![]({{site.baseurl}}/images/curl2.png)



Here is my docker-compose.yml file Here I changed the image to become unique for my flask and I changed the port to have 8089 to differentiate from my container vs my teamates conatainers
```yaml
version: '3'
services:
        web:
                image: flask_alex_v1
                build: .
                ports:
                        - "8089:8080"
                volumes:
                        - persistent_volume:/app/volumes
volumes:
  persistent_volume:
    driver: local
    driver_opts:
      o: bind
      type: none
      device: /home/ubuntu/alex-flask/volumes
```
Here is my dockerfile! It is basically original except for the COPY ..
``` dockerfile
FROM docker.io/python:3.9

WORKDIR /app

# --- [Install python and pip] ---
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y python3 python3-pip git
COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip3 install gunicorn

ENV GUNICORN_CMD_ARGS="--workers=1 --bind=0.0.0.0:8080"

EXPOSE 8080

CMD [ "gunicorn", "main:app" ]
```
Here is my nginx file for my flask! Here you can see my personal ports and the public ip that we put.
``` nginx
server {
        listen 8083;
        listen [::]:8083;
        server_name 18.216.138.52;

        location / {
                proxy_pass http://localhost:8089;
                add_header "Access-Control-Allow-Origin" *;
        }
}
```