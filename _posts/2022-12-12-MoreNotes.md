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

# Simulations- Unit 3 Section 16

3.16 Intro to Simulations
- Many simulations are used, for example testing a car safety
- ensuring new technology works
- simulating a train
- Simulations are different than an experiment because it is less accurate as its not real
- Simulations are cheaper and more efficent however it is not as accurate as an experiment
- It also cannot account for real life factors or outside facters

Real examples
- You can use a simulation to imitate a game, for example the four corners game.
- This game can be recreated with this python script

```python
import random

status = "in"
while status != "out":
    chooseCorner = input("What corner do you choose?")

    corner = random.randint(1,4)

    if int(chooseCorner) == corner:
        status = "out"
        print("You chose corner number " + chooseCorner + " and you're OUT")
    else:
        print("You chose corner number " + chooseCorner + " and are still in!")
```
- This game basically assigns you a corner randomly and allows you to pick a corner
  

Rolling a Dice Example
```python
def parse_input(input_string):
    if input_string.strip() in {"1", "2", "3","4", "5", "6"}:
        return int(input_string)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)

import random

def roll_dice(num_dice):
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results


num_dice_input = input("How many dice do you want to roll? [1-6] ")
num_dice = parse_input(num_dice_input)
roll_results = roll_dice(num_dice)

print("you rolled:", roll_results) 
```
- This code allows us to replicate rolling a dice three times because it usesrandom
- This is very useful because now we do not have to actually roll the dice three times
- This has some flaws because it is assuming that the roll is going to be perfect and that it will truly be equal for all sides however becauseof outside factors this may not be true

Game of Life
- This code is random and uses the library random to pick random boxes creating random patterns
- this is another example of how a simulation can be used to represent cellular automaton