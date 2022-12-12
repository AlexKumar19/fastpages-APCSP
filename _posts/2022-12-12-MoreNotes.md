---
toc: true
layout: post
description: More Teaching notes
title: Extended blog for notes after Unit 3 section 14
categories: [markdown, csp]
permalink: /Moreteachcingnotes/
---
# Unit 3 Sections 14 and 15

Section 3.14.1 - Libraries
- Software library contains procedures
- segments of code come from sources
- libraries simplify complex algorithms
- APIs or application program interfaces specify how a librarycan be used
- For librarys, you can call to them in order to addfunctions
- libraries have a period that tells the program to look for the library

```python
import math
math.sqrt(64)
```
This is an example of a library
```python
import random
random.randrange()
```
This allows to import random numbers easily using a library

Lesson 3.15.1
```python
import random

answer1 = random.randint(0,3)
answer2 = random.randint(1,8)
answer3 = answer1 + answer2
print(answer3)
```
This code goes over the libraries mentioned before and can generate random numbers using the library

```python
import random
sum = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
print(sum)
```
This is a great example on how randomcan be used to get random numbers 

- Random is a library with many functions that can generate random nums

3.15.2 Lesson

```python
import random
flip = random.randint(1,2)
 
if flip == 1:
    print("Heads")
else:
    print("Tails")
```
- This code flips a coin