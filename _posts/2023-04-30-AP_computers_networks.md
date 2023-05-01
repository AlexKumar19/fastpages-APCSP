---
toc: true
comments: true
layout: post
title: Computers and Networks (Unit 4)
description: Add Definitions from Unit 4 Computer Systems and Networks
image: /images/apcsp.png
categories: []
type: ap
week: 29
---

## Requirements
> Work through College Board Unit 4... blog, add definitions, and pictures.  Be creative, for instance make a story of Computing and Networks that is related to your PBL experiences this year.


### How a Computer Works
> As we have learned, a computer needs aa program to do something smart.  The sequence of a program initiates a series of actions with the computers Central Processing Unit (CPU). This component is essentially a binary machine focussing on program instructions provided.  The CPU retrieives and stores the data it acts upon in Random Access Memory (RAM). Between the CPU, RAM, and Storage Devices a computer can work with many programs and large amounts of data.

List specification of your Computer, or Computers if working as Pair/Trio
- Processor GHz: Intel Core i7
- Memory in GB: 32 gigs
- Storage in GB: 1 terabyte
- OS: Windows 10

Define or describe usage of Computer using Computer Programs. Pictures are preferred over a lot of text.  Use your experience.
- Input devices: lets a user interact with the computer- mouse, microphone, keyboard
Output devices: computer communicate with the user- speaker, headphones, monitor
Program File: file that the computer can execute to run a program- games, media player, website
Program Code: instructions for the computer when a program file is run- stuff behind the game, website, and stuff
Processes: program is executed in multiple threads- searching, debugging, sorting, etc
Ports: endpoint that lets a server handle requests from devices over the internet
Data File: has information in the file, or data in a specific format, can be CRUDed, and tells program what to do
Inspect Running Code: the inspect element on browser, shows what is happening behind what we see normally, cherry tomatoes when we debug in VS code
Inspect Variables: see the values on the variables to debug and see what is happening

## how does a computer work

The basic parts of a computer are:
Input devices: These devices allow users to input data into the computer, such as the keyboard, mouse, and microphone.
Output devices: These devices allow users to see or hear the results of the computer's processing, such as the monitor, printer, and speakers.
Storage devices: These devices store data that is not currently being used by the computer, such as the hard drive, CD-ROM, and DVD-ROM.
Central processing unit (CPU): The CPU is the "brain" of the computer. It is responsible for carrying out the instructions that are given to it by the computer's software.
Memory: Memory is used to store data that is currently being used by the computer, such as the operating system, applications, and data files.

![Computer Hardware]({{site.baseurl}}/images/cpu.jpeg)


### The Internet
> Watch/review College Board Daily Video for 4.1.1

- Essential Knowledge
    - A computing device is a physical artifact that can run a program. Some examples include computers, tablets, servers, routers, and smart sensors.
    - A computing system is a group of computing devices and programs working together for a common purpose.
    - A computer network is a group of interconnected computing devices capable of sending or receiving data.
    - A computer network is a type of computing system. 
    - A path between two computing devices on a computer network (a sender and a receiver) is a sequence of directly connected computing devices that begins at the sender and ends at the receiver.
    - Routing is the process of finding a path from sender to receiver.
    - The bandwidth of a computer network is the maximum amount of data that can be sent in a fixed amount of time.
    - Bandwidth is usually measured in bits per second

- Complete Vocabulary Matching Activity.  Incorporate this into your learnings from year.  To analyze measure path and latency use `traceroute` and `ping` commands from Linux Terminal.  
    - Path –> A path between two computing devices on a computer network (a sender and a receiver) is a sequence of directly connected computing devices that begins at the sender and ends at the receiver.
Route –> Routing is the process of finding a path from sender to receiver.
Computer System –> A computing system is a group of computing devices and programs working together for a common purpose.
Computer Device –> A computing device is a physical artifact that can run a program. Some examples include computers, tablets, servers, routers, and smart sensors.
Bandwidth –> Bandwidth is usually measured in bits per second.
Computer Network –> A computer network is a group of interconnected computing devices capable of sending or receiving data.
![image](https://user-images.githubusercontent.com/110933283/235528117-d53a7d91-fd4f-45ef-bf4b-2e98d9b371a6.png)

The OSI model is a conceptual model that describes the seven layers of a network architecture. The network layer is responsible for routing data between differnt networks, and the application layer is responsible for providing services to the user, such as web browsing or email.

The network layer works by breaking down data into smaller units called packets. Each packet contains the source and destination addresses, as well as the data itself. The network layer then uses routing protocols to determine the best path for each packet to take. Once the packets reach their destination, they are reassembled into the original data.

The application layer is responsible for providing services to the user. For example, the web browser application uses the application layer to request web pages from a web server. The web server then uses the application layer to send the web pages back to the web browser.

The OSI model is a helpful tool for understanding how networks work. It can also be used to troubleshoot network problems. For example, if a user is unable to access a web page, a network administrator can use the OSI model to identify the layer at which the problem is occurring.

Here is a brief overview of the seven layers of the OSI model:

Physical layer: The physical layer is responsible for the transmission of raw data bits over a physical medium, such as a copper wire or an optical fiber.
Data link layer: The data link layer is responsible for error detection and correction, as well as flow control.
Network layer: The network layer is responsible for routing data between different networks.
Transport layer: The transport layer is responsible for ensuring that data is delivered in the correct order and that it is not corrupted.
Session layer: The session layer is responsible for managing the communication between two applications.
Presentation layer: The presentation layer is responsible for converting data into a format that can be understood by the application.
Application layer: The application layer is responsible for providing services to the user.
> Watch/review College Board Daily Video 4.1.2

- Complete True of False Questions
- T
- F
- F
- T
- F
- F
- T

- Essential Knowledge
    - The internet is a computer network consisting of interconnected networks that use standardized, open (nonproprierary) communication protocols.
    - Access to the internet depends on the ability to connect a computing device to an internet connected device.
    - A protocol is an agreed-upon set of rules that specify the behavior of a system.
    - The protocols used in the internet are open, which allows users to easily connect additional computing devices to the internet.
    - Routing on the internet is usually dynamic; it is not specified in advance
    - The scalability of a system is the capacity for the system to change in size and scale to meet new demands.
    - The internet was designed to be scalable
    - Information is passed through the internet as a data stream. Data streams contain chunks of data, which are encapsulated in packets. 
    - Packets contain a chunk of data and metadata used for routing the packet between the origin and the destination on the internet, as well as for data reassembly.
    - Packets may arrive at the destination in order, out of order, or not at all
    - IP, TCP and UDP are common protocols used on the internet.
    - The world wide web is a system of linked pages, programs, and files.
    - HTTP is a protocol used by the world wide web
    - The world wide web uses the internet

- Go over AP videos, vocabulary, and essential knowledge.  Draw a diagram showing the internet and its many levels. A preferred diagram would using your knowledge of frontend, backend, deployment, etc.  Picture would highligh vocabulary by illustration. The below illustration have some ideas


![Full Stack](https://user-images.githubusercontent.com/110933283/233200691-8d1fe68c-7b4a-410d-9343-76102d3c5cae.png)

- Often we draw pictures of machines communicating over the Internet with arrows.  However, the real communication goes through protocol layers and the machine and then is trasported of the network.   For College Board and future Computer Knowledge you should become familiar with the following ...

```
     User Machine  <---> Frontend Server <---> Backend Server
    +-----------+         +-----------+         +-----------+
    |  Browser  |         |  GH Page  |         |   Flask   |
    +-----------+    ^    +-----------+    ^    +-----------+
    |    HTTP   |    |    |    HTTP   |    |    |    HTTP   |
    +-----------+    |    +-----------+    |    +-----------+
    |    TCP    |    |    |    TCP    |    |    |    TCP    |   
    +-----------+    |    +-----------+    |    +-----------+
    |     IP    |    V    |     IP    |    V    |     IP    |
    +-----------+         +-----------+         +-----------+
    |  Network  |  <--->  |  Network  |  <--->  |  Network  |
    +-----------+         +-----------+         +-----------+
```

The "http" layer is an application layer protocol in the TCP/IP stack, used for ***communication between web browsers and web servers***. It is the protocol used for transmitting data over the World Wide Web.

The "transport" layer (TCP) is responsible for providing reliable data transfer between applications running on different hosts.  The TCP protocol segments the data into smaller ***chunks called "segments"***. Each segment contains a sequence number that identifies its position in the original stream of data, as well as other control information such as source and destination port numbers, and checksums for error detection.

The "ip" layer is responsible for packetizing data received from the TCP layer of the protocol stack, and then ***encapsulating the data into IP packets***. The IP packets are then sent to the lower layers of the protocol stack for transmission over the network.

The "network" layer is responsible for ***routing data packets between networks*** using the Internet Protocol (IP). This layer handles tasks such as packet addressing and routing, fragmentation and reassembly, and ***network congestion*** control.


### Fault Tolerance
> Watch both Daily videos for 4.2

- Complete the network activity, summarize your understanding of fault tolerance.
Fault tolerance is a process that lets an OS respond to failure in the hardware or software. So the system won’t break down completely due to an error or failure.

### Parallel and Distributed Computing
> Review previous lecture on Parallel Computing and watch Daily vidoe 4.3.  Think of ways to make something in you team project to utilize Cores more effectively.  Here are some thoughts to add to your story of Computers and Networks...

- What is naturally Distributed in Frontend/Backend archeticture?  
  - The frontend and backend of a web application are naturally distributed. The frontend is typically hosted on a web server, which is a single machine. The backend, on the other hand, can be distributed across multiple machines. This is because the backend typically consists of different components, such as a database, a web server, and an application server. Each of these components can be hosted on its own machine.

- Analyze this command in Docker: ```ENV GUNICORN_CMD_ARGS="--workers=1 --bind=0.0.0.0:8086"```.   Determine if there is options are options in this command for parallel computing within the server that runs python/gunicorn.  Here is an [article](https://medium.com/building-the-system/gunicorn-3-means-of-concurrency-efbb547674b7)
  - The command ENV GUNICORN_CMD_ARGS="--workers=1 --bind=0.0.0.0:8086" sets the environment variable GUNICORN_CMD_ARGS to the value "--workers=1 --bind=0.0.0.0:8086". The GUNICORN_CMD_ARGS environment variable is used to pass additional command line arguments to Gunicorn.


> Last week we discussed parallel computing on local machine.  There are many options.  Here is something to get parallel computing work with a tool called Ray.
- Review this [article](https://www.anyscale.com/blog/writing-your-first-distributed-python-application-with-ray)...  Can you get parallel code on images to work more effectively?  I have not tried Ray.

- Code example from ChatGPT using squares.  This might be more interesting if nums we generated to be a lot bigger.

```python
import ray

# define a simple function that takes a number and returns its square
def square(x):
    return x * x

# initialize Ray
ray.init()

# create a remote function that squares a list of numbers in parallel
@ray.remote
def square_list(nums):
    return [square(num) for num in nums]

# define a list of numbers to square
nums = [1, 2, 3, 4, 5]

# split the list into two parts
split_idx = len(nums) // 2
part1, part2 = nums[:split_idx], nums[split_idx:]

# call the remote function in parallel on the two parts
part1_result = square_list.remote(part1)
part2_result = square_list.remote(part2)

# get the results and combine them
result = ray.get(part1_result) + ray.get(part2_result)

# print the result
print(result)

```



### personal example

```python

import time

def factorial(n):
  # Calculate the factorial of n.
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

if __name__ == "__main__":
  # Start the timer.
  start_time = time.time()

  # Calculate the factorial of 100 in parallel.
  results = []
  for i in range(10):
    results.append(factorial(100))

  # Stop the timer.
  end_time = time.time()

  # Print the results.
  print(results)

  # Print the elapsed time.
  print("Elapsed time:", end_time - start_time)
  ```
  This code calculates the factorial of 100 in parallel. It starts by creating a list of 10 worker processes. It then submits the factorial function to each worker process. The worker processes calculate the factorial of 100 in parallel. The results of the calculation are then collected and printed.