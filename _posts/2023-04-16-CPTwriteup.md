---
toc: true
layout: post
description: CPt Write
title: CPT Writeup for weather
categories: [markdown, csp]
permalink: /csp/CPTwriteupWeather/
---

Write-Up (Air Quality Analyzer)

video
3a.
3.a.i.
This program provides air quality information to citizens and potential travelers so that they can make informed decisions about whether or not to be cautious of air quality in a given city.
3.a.ii.
This program utilizes the requests module to establish a connection with a public API that provides air quality information for various cities. It enables the user to input a city name and retrieve data on either PM2.5 or PM10 concentrations. Additionally, the user can view a list of previously retrieved concentrations. To store the concentration values, the program employs a dictionary called 'data.' This dictionary comprises two keys, 'pm25' and 'pm10,' each with a dictionary containing city names and concentration values.When the user selects option 1 or 2, the program sends a request to the API to obtain concentration data for the specified city. If the data is accessible, the program outputs the concentration along with a safety message based on the concentration value. Afterward, it adds the city and concentration to the 'data' dictionary. Upon selecting option 3, the program produces a list of city names and their respective PM2.5 and PM10 concentration values saved in the 'data' dictionary. Finally, the program executes a while loop to continue running until the user selects option 4 to exit.


3.a.iii.
The name of the variable is pm25 which is a dictionary that stores the stored conectration of pm25 

3b.
3.b.i.
![image](https://user-images.githubusercontent.com/110933283/232341325-8853b448-ede1-42f9-8946-a4bc9fe9e34a.png)

3.b.ii.

![image](https://user-images.githubusercontent.com/110933283/232341334-a86fa7bf-7360-40e2-a3f1-3b4c37a0d444.png)    


3.b.iii.
The name of the variable representing the collection type is “stored data”, which is a list of dictionaries consisting of the stored concentration values of pm25 and pm10 in the inputted cities by the user.
3.b.iv.
As previously mentioned, the second image illustrates how the program uses the collection type "pm25" as a dictionary. This enables the program not only to output the respective PM2.5 concentration value for a given city, but also to store user inputs if the menu option 3 is selected. In essence, "pm25" is a collection type that functions as a dictionary, storing PM2.5 concentrations for various cities. Each key in the "pm25" dictionary corresponds to a city, and its value represents the corresponding PM2.5 concentration.
3.b.v.
The PM2.5 concentration data collected is stored in a data dictionary, where the key "pm25" points to a sub-dictionary that contains data for different cities. Using a dictionary as a storage mechanism enables easy access and manipulation of the data. This allows the program to retrieve PM2.5 concentration data for a specific city by accessing the corresponding key in the data dictionary. The collection type "pm25" is essential because it enables the program to store and retrieve PM2.5 concentration data for various cities across multiple program runs. This also avoids making unnecessary API requests and saves time and resources as the program can access previously collected data when the user requests PM2.5 concentration data for a previously searched city.
3.c.
3.c.i.
![image](https://user-images.githubusercontent.com/110933283/232341353-d65766a7-307b-4415-bb77-997632aae84e.png)


3.c.ii.
![image](https://user-images.githubusercontent.com/110933283/232341365-33e1aa5a-ca36-49cf-a62c-187f33be944b.png)
3.c.iii.
The two functions available here are named "find_pm25" and "find_pm10," and their respective purposes are indicated by their names. They are capable of providing the numerical integer value representing the concentration of either pm25 or pm10 for any city within the United States. These functions are invoked within a while loop to accomplish the menu's objectives. Upon selecting either option, the user will be prompted to enter a city name, and the corresponding concentration value will be returned by the program.
3.c.iv.
The provided code implements sequencing, selection, and iteration to offer an intuitive interface for accessing air quality information for various cities. Specifically, sequencing is employed to present a menu of options for the user to select from, including: obtaining PM2.5 concentration for a given city, obtaining PM10 concentration for a given city, viewing stored concentration values for PM2.5 and PM10 for various cities, and exiting the program. Selection is utilized to discern the user's preferred action based on their choice. For instance, if the user chooses option 1, they will be prompted to input a city name, and the find_pm25 function will be invoked to retrieve and display the PM2.5 concentration for that city. Similarly, if option 2 is selected, the user will be asked to input a city name, and the find_pm10 function will be invoked to retrieve and display the PM10 concentration. Iteration is employed to display the stored concentration values for all cities when the user selects option 3. Finally, if the user chooses option 4, the program will terminate.
3.d
3.d.i.
Call One
The initial invocation occurs within the function designed to retrieve and yield the PM2.5 concentration value for the specified city. Upon successful execution of the function, a message should be printed out that displays the PM2.5 concentration level for the city as well as whether the air quality is safe or hazardous. If the function fails to find data for the specified city, a message should be printed out informing the user that there is no PM2.5 concentration data available for the city.
Call Two
The second instance of calling a function occurs within the code block responsible for retrieving and returning the PM10 concentration level for the given city. Upon a successful query, the program should output a message displaying the PM10 concentration value for the city and indicating whether the corresponding air quality level is safe or hazardous. If the function is unable to find data for the city, a message should be printed out notifying the user that there is no PM10 concentration data available for the specified city.
3.d.ii.
Condition(s) tested by Call One
Here, the condition being tested is whether there is any data available for the PM2.5 concentration in the given city. If the data is available, the code segment that prints the PM2.5 concentration for the city is executed, followed by a nested selection statement that checks whether the PM2.5 concentration is less than 25. If the concentration is less than 25, the message “This is a safe level of air quality.” is printed. Otherwise, the message “This is unsafe air quality. Be cautious!” is printed. The PM2.5 concentration value is then stored in the data dictionary. If the data is not available for the given city, the message “Sorry, there is no PM2.5 data available for {city}.” is printed.
Condition(s) tested by Call Two
Call two is testing the condition pm10_concentration[“concentration”] < 25 in the find_pm10 function. If the condition is true, the program will execute the code block that prints “This is a safe level of air quality. Enjoy!” and stores the PM10 concentration value in the data dictionary under the key pm10. If the condition is false, the program will execute the code block that prints “This is unsafe air quality” and stores the PM10 concentration value in the data dictionary under the key pm10.
3.d.iii.
Results of Call One
The output of the first function call is dependent on the city input argument. If the PM2.5 API response provides a valid concentration value for the given city, then the function will display the PM2.5 concentration value and a corresponding message that indicates if the air quality is safe, based on the concentration level. Additionally, the PM2.5 concentration value will be added to the data dictionary. However, if the API response does not contain any PM2.5 data for the specified city, the function will print a message indicating that. In the event of an error during the request processing, the function will display an error message.
Results of Call Two
The code checks for the availability of PM10 concentration data for the provided city argument. If the data exists, the PM10 concentration value is fetched and compared against the safety threshold of 25. If the concentration value is lower than 25, the function will display a message indicating safe air quality and save the value in the data dictionary. Otherwise, a message indicating unsafe air quality is printed. In case the concentration value is lower than 25, it will be stored in the data dictionary using the pm10 key and the provided city. If the PM10 concentration data is not available for the specified city, the function will print a message stating the unavailability of data.

