---
toc: true
layout: post
description: Codorg quiz blog
title: Codeorg Blog
categories: [markdown, csp]
permalink: /csp/Codeorgblog
---

[Link](https://studio.code.org/projects/applab/q4hZDkGXBcYJunc7WLT1YmG3eCs6XlK45Kkq_73Y__M/edit)
# Design
The design that me and Safin chose was to design our own quiz and eventually come together to make one app that accesses both of our quizzes. The way that We planned this was storing all of our quiz data into one list of dictionary respectively called Basketball and Tennis and we uploaded the lists into the same app.

# Data abstraction
We created a huge list that contains dictionarys and whithin the dictionaries there were key and value pairs. Within the answer pair we put all of our answer choices which included pictures, names, and whether they were right or not. This list was easy to parse through and allowed us to use functions that went through these lists and created tests

# Managing Complexity
In order to manage the complexity of this quiz, we were able to input many comments and use many functions to ensure that the code is very easy to follow. The comments allow us to communicate what we are doing with each function and what the purpose of the variables are. And the repeated use of the functions allow us to easily call back to a known function that we make and it communicated the purpose of the funciton without having the reader have to understand the code.

# Procedural Abstraction
In order to apply the lists into the quiz, we used many functions. The overarching function was the function that called for the quiz and whithin the quiz function we were able to create many different functions. Some functions included changing the selected answer. Changing the pictures and labels as we the the quiz changes question. And another function we used was the finish function that changes the screen to the end and outputs score.

# Algorithm implementations
We used many algorithms or functions to make the code more straight forward and less repetitive. Some of them are next question or finish quiz. This was important to our code because it allowed us to call back to that algorithm very easily without having to recode the whole thing over and over again. These algorithms made our code easier to understand and made it more efficent.

# Testing
In order to test out our code, we used the console.log to test out what the code would output before implementing it into our code. This way we were able to see what input was given and how we can use that input to advance our quiz. The consol.log function was a very useful tool that went very well with the onEvent block because it allows us to easily detect for when input is given and it allows us to test new strategies and ideas without hurting out code
# Challenges
Some challenges was formatting the quiz into the right list and dictionary so we could call to it. This was very tedious and very hard because and syntax errors in the large array stopped the whole code all togther. Another problem that came up and that the variables were not resetting after each function use. In order to solve this we had to make a new function that resets all the variables.

# Successes
Some of our success came form the onEvent block because it was very easy to use and allowed us to save a lot of time without our code. This Onevent block led to us ultimately creating a working quiz that enabled me and safin to combine the quizes that we made.