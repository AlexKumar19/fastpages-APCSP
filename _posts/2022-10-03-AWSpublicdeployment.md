---
toc: true
layout: post
description: Deploying our AWS server to become accesible through https web traffic!
title: AWS Deployment
categories: [markdown, csp]
permalink: /AWSDeploymentpublic/
---
# Docker!

Me and my group was able to create four different containers that are each bound to 8080 with a unique port for each site. Each website also has a unique image!
![]({{site.baseurl}}/images/docker.png)

Next we tested to see if we were able to run the websites inside of the container that we made!
![]({{site.baseurl}}/images/curl.png)

This is the process of pulling from my flask and then updating the website on AWS
![]({{site.baseurl}}/images/pull.png)