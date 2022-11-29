---
toc: true
layout: post
description: Notes from lessons
title: Lesson Notes
categories: [markdown, csp]
permalink: /Lessonnotes/
---
# Unit 3, Section 1.1: Data Types and Variables
- variable is an abstraction that holds a value
- variables have meaningful names to help organize
- each different language has a specific way to store variables
- variables hold variable
- makes code more organized, variables can be compared to containers
- it is important to choose a name that correlates to the function
- integers for numbers
- strings stores text
- boolean true or false
- input function recieves input
- document.querySelector is a javascript code that you can use the query the code to find a certain class in order to find the button
### 3.2.2 Data Absraction with lists
- lists bundle together multiple elements under one name
- you can have different types of variables whithin one list
- the function list in python splits a string into a list of characters
- .join can join the characters together
## Unit 3.1-3.3 Hacks
```python
name = "alex"
age = 16
print("name is", name)
print("age is", age)
```
In your own words, briefly explain by writing down what an assignment operator is
- an equal sign is an assignment operator as it assigns a variable to a value
In Collegeboard pseudocode, what symbol is used to assign values to variables?
- the arrow is used to assign values
A variable, x, is initially given a value of 15. Later on, the value for x is changed to 22. If you print x, would the command display 15 or 22?
- it would output 22

What is a list?
- a bundle of multiple elements
What is an element
- an element could be a number or integer, string, or a boolean expression
What is an easy way to reference the elements in a list or string?
- use index to find the elements in a list
What is an example of a string?
- "amay" this is an example of a string
``` python
foods = ["pizza", "chicken", "steak", "pasta", "lasagna", "salad", "burger"]
print(foods[3])
print(foods[-4])
```
``` python
num1=input("Input a number. ")
num2=input("Input a number. ")
num3=input("Input a number. ")
add=input("How much would you like to add? ")

# Add code in the space below

numlist = [num1,num2,num3]

# The following is the code that adds the inputted addend to the other numbers. It is hidden from the user.

for i in [int(a) for a in numlist]:
    numlist[i -1] += int(add)

print(numlist)
```
![]({{site.baseurl}}/images/123.png)

```python
foods = ["pizza", "hot dog", "sushi", "strawberry", "sandwhich"] #simplified foods list
# it is better to use lists because it is more simple
sports1 = "basketball"
sports2= "tennis"
sports3 = "soccer"
sports= ["basketball","tennis","soccer"]
```

# lesson 3.3 and 3.4
- Algorithms are a finite set of instructions that can help you accomplish a task
- an algorithm is made up of sequencing selection and iteration
- A sequence is the orders or the instructions
- selection is what allows algorithms to make decisions
- finally iteration is what repeats

- sequential statements specify how signals can be assigned
- sequencing is the order that the code explains these steps
- arithmetic operators, you can add and do basic operators by using + - / and *
- this operator % gives out the remainder
- len() gives the number of characters inside of a string
- concat("", "") combines two different strings
- subtstring() can return specific characters of a string

## HACKS for 3.3 and 3.4
1. sequencing
2. sequencing
3. selection, sequencing
4. iteration, sequencing
5. sequencing

```python
num1 = 5
num2 = num1 * 3
num3 = num2 / num1 * (9 % 2) * 4
result = (num3 % num1 + num2) % num3 * 3 / 5
```
this results in 3

hacks for 3.3
1. iteration
2. selection
3. sequence
![]({{site.baseurl}}/images/questions.png)