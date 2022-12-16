---
toc: true
layout: post
description: Organized notes and hacks for all lessons with vocab
title: Final Blog for teaching
categories: [markdown, csp]
permalink: /TableAndTeachingNotes/
---

# Hacks + Notes

| Lesson               | Hacks       | Notes | Grades |
| -----------          | ----------- | ----- | ---- |
| Unit 3 Sections 1-2  | [Hacks](https://alexkumar19.github.io/fastpages-APCSP/3.1hacks/)   |  [Notes](https://alexkumar19.github.io/fastpages-APCSP/Lessonnotes/)      |   1     |
| Unit 3 Sections 3-4  | [Hacks](https://alexkumar19.github.io/fastpages-APCSP/33hacks/)   |  [Notes](https://alexkumar19.github.io/fastpages-APCSP/Lessonnotes/)      |   1     |
| Unit 3 Sections 5-7  | [Hacks](https://alexkumar19.github.io/fastpages-APCSP/3.53.8hacks/)   |  [Notes](https://alexkumar19.github.io/fastpages-APCSP/Lessonnotes/)      |   0.9     |
| Unit 3 Sections 8-10  | [Hacks](https://alexkumar19.github.io/fastpages-APCSP/csp/310hacks)   |  [Notes](https://alexkumar19.github.io/fastpages-APCSP/Lessonnotes/)      |   1     |
| Unit 3 Sections 9-11  | [Hacks](https://alexkumar19.github.io/fastpages-APCSP/csp/3111hacks)   |  [Notes](https://alexkumar19.github.io/fastpages-APCSP/Lessonnotes/)      |   0.93     |
| Unit 3 Sections 12-13  | N/A   |  [Notes](https://davidvasilev1.github.io/group-tri2/2022/12/04/lesson3.12_3.13.html)      |   N/A     |
| Unit 3 Sections 14-15  | [Hacks](https://alexkumar19.github.io/fastpages-APCSP/csp/39311hacks)   |  [Notes](https://alexkumar19.github.io/fastpages-APCSP/Moreteachcingnotes/)      |   0.9     |
| Unit 3 Sections 16  | [Hacks](https://alexkumar19.github.io/fastpages-APCSP/csp/316hacks)   |  [Notes](https://alexkumar19.github.io/fastpages-APCSP/Moreteachcingnotes/)      |   0.9     |
| Unit 3 Sections 17-18  | [Hacks](https://alexkumar19.github.io/fastpages-APCSP/csp/317hacks)   |  [Notes](https://alexkumar19.github.io/fastpages-APCSP/Moreteachcingnotes/)      |   N/A     |

# Vocab

- Bits, Bytes, Hexadecimal / Nibbles:

A bit is the smallest unit of data, representing either a 0 or a 1.
A byte is a unit of digital information that consists of 8 bits.
Hexadecimal is a numbering system that represents numbers using the base 16, with the digits 0-9 and A-F. Each hexadecimal digit represents 4 bits, so two hexadecimal digits make up 1 byte.
- Binary Numbers: Unsigned Integer, Signed Integer, Floating Point:

An unsigned integer is a binary number that can only represent positive numbers.
A signed integer is a binary number that can represent both positive and negative numbers using a sign bit.
A floating point number is a binary number that can represent real numbers with a decimal point.
- Binary Data Abstractions: Boolean, ASCII, Unicode, RGB:

A boolean is a data type that can only have two values: True or False.
ASCII (American Standard Code for Information Interchange) is a character encoding standard that represents text using numbers.
Unicode is a character encoding standard that represents a wide range of characters from various scripts.
RGB (Red Green Blue) is a color model that represents colors as a combination of red, green, and blue values.
- Data Compression: Lossy, Lossless (note discussed yet):

Lossy data compression is a method of reducing the size of a file by removing some of the data. This can result in a loss of quality, but the file size is smaller.
Lossless data compression is a method of reducing the size of a file without losing any data. The file size is smaller, but the quality is not compromised.
- Variables, Data Types, Assignment Operators:

A variable is a named location in memory that stores a value.
Data types define the type of value that a variable can store, such as an integer, a string, or a boolean.
Assignment operators are used to assign a value to a variable. In Python, the assignment operator is the equal sign (=).
- Managing Complexity with Variables: Lists, 2D Lists, Dictionaries, Class:

A list is an ordered collection of values that can be of any data type. Lists are created using square brackets and the values are separated by commas. For example: my_list = [1, 2, 3]
A 2D list is a list of lists, representing a table of values with rows and columns.
A dictionary is a collection of key-value pairs, where each key is mapped to a value. Dictionaries are created using curly braces and the key-value pairs are separated by commas. For example: my_dict = {'key': 'value'}
A class is a template for creating objects. It defines the properties and methods of the objects.
- Algorithms, Sequence, Selection, Iteration:

An algorithm is a set of steps for solving a problem.
Sequence is the order in which statements are executed in a program.
Selection is the decision-making process in a program, using control statements such as if-else statements.
Iteration is the repetition of a block of code using loops.
- Expressions, Comparison Operators, Booleans Expressions and Selection, Booleans Expressions and Iteration, Truth Tables:

An expression is a combination of values, variables, and operators that evaluates to a result.
Comparison operators are used

Variables: variables are storage
```python
var = 3
```
This is an example of a variabe

Data Types: Some datatypes are string lists

```python
list = []
```
This is a list

Assignment Operators: the arrow represents assignment operators
```python
varknow = 6
```
we are assigning a value to this

Managing Complexity with Variables: 
Lists: lists can be used to store many types of data
```python
sports = ["basketball","soccer"]
```

2D Lists,
```python
list = []
```
 Dictionaries: very good way to store keys and terms
 ```python
dict = {"car":"good", "cat":,"bad"}
 ```
 
 Class
Algorithms, 
Algorithms help smplify code
```python
def function():
    print("hi")
```
```python
def new():
    print("this is a function"):
```
Sequence: represents the order
```python
print("this is first")
print("this is after")
```
 Selection makes decision based on data
```python
if dog==True:
    print("there is a dog")
```
  Iteration
  this is aloop
```python
for i in range(5):
    print("hi")
```
this loops over 5 times

Expressions, 
Comparison Operators,some comparison terms are like < and >
```python
if num1 > num2:
    print("num1 is greater than num2")
```
 Booleans Expressions and Selection, selects if a value is true or not
 ```python 
boolean = True
falseboolean = False
 ```
 
  Booleans Expressions and Iteration,
   Truth Tables
```javascript
function truth(){
    var data = [[1,1], [1,0], [0,1], [0,0]];
    var text = ""
    for(let i =0; i < data.length; i++) {
        text += data[i][0] + "&" + data[i][1] + "-->" + (data[i][0] & data[i][1]).toString() + "<br>"
    }
    for(let i =0; i < data.length; i++) {
        text += data[i][0] + "|" + data[i][1] + "-->" + (data[i][0] | data[i][1]).toString() + "<br>"  
    }
    for(let i =0; i < data.length; i++) {
        text += data[i][0] + "^" + data[i][1] + "-->" + (data[i][0] ^ data[i][1]).toString() + "<br>"
    }
    let newdata = [1,0]
    for(let i =0; i < newdata.length; i++) {
        text += "~" + newdata[i] + "=" + ~newdata[i] + "<br>"
    }
    document.getElementById("text1").innerHTML = text
}
truth()
```
Characters,A word can be split into characters
```python
word = "hi"
split = word.split()
```
Strings, basic values held in a variable 
```python
string = "hi"
```

Length, There is a length function that can get the length of any string
```python
list = [1,2,3,4,5,6]
length = len(list)
```
This gets the length of the list

Concatenation, You can combine databases with this
```python
import pandas
pd = pd.concat()
```
Python If,  can check for certain conditions
```python
if boolean=True:
    print("any text here")
```

Elif, This can be used to check for a second function and this is very useful when choosing between certain conditions
```python
if boolean=True:
    print('good')
elif boolean=False:
    print("this is bad")
```


Else conditionals;

```python
if True:
    print("this is true")
else:
    print("not possible")
```
 Nested Selection Statements
 
```python
if True:
    if dogs==True:
        print("very good")
```
This can be used to checkfor many conditions whithin a certain condition, you can nest many conditions

Python For, 
```python
for i in range(5):
    print(i)
```

While loops with Range,
```python
while i<6:
    i+= 1
```
Combining loops with conditionals to Break,
 Continue
Procedural Abstraction, Python Def procedures, Parameters, Return Values