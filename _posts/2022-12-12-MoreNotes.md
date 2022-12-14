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

# Period 4 Lesson 17-18

Undecidability: sometetimes we cannot tell if a certain number will follow the program guidlines
for example the number example where you divide by 2 or times by 3 and add one. We have to ensure that all the numbers we put in are predictable

```python
def collatz(i):
    while i > 1:
        print(i, end=' ')
        if (i % 2):
            # i is odd
            i = 3*i + 1
        else:
            # i is even
            i = i//2
    print(1, end='')
 
 
i = int(input('Enter i: '))
print('Sequence: ', end='')
collatz(i)
```
This code print sout the hialstone numbers

```python
def collatz(i):
    while i != 1:
        if i % 2 > 0:
             i =((3 * i) + 1)
             list_.append(i)
        else:
            i = (i / 2)
            list_.append(i)
    return list_


print('Please enter a number: ', end='')
while True:
    try:
        i = int(input())
        list_ = [i]
        break
    except ValueError:
        print('Invaid selection, try again: ', end='')


l = collatz(i)

print('')
print('Number of iterations:', len(l) - 1)
```
Collatz- The Collatz conjecture is one of the most famous unsolved problems in mathematics. The conjecture asks whether repeating two simple arithmetic operations will eventually transform every positive integer into 1.
Undecidable problems gives yes or no but there is no code that can solve it on all inputs
unsolvable problems, no algorithm can solve the problem
Hailstone numbers are the output of the Collatz code.

Unit 3, Section 17: 

- Algorithm efficieny is how many steps you have to use to solve a certain problem
- by being very efficient you would use less points that this is very helpful because now the code will run more efficiently
- 