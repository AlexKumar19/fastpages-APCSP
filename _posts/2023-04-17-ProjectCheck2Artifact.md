---
toc: true
layout: post
description: Simulations and artifacts
title: Simulations for Project CHeck 2
categories: [markdown, csp]
permalink: /csp/artifactsandsimulations/
---

# Demonstration of List
- Adding text to a list
- This is a simulation where you can see the text getting added to the text box!

<html>
<button onclick="add()" id="my-button" class="primary-button">Click me!</button>
<input type="text" id="mytextbox" name="textbox" class="form-control" placeholder="Enter Text" size="30" maxlength="50" required>
<p id="output"></p>
</html>

<script>
let textList = [];
function add(){
    
    
    let inputElement = document.getElementById("mytextbox");
    let text = inputElement.value;
    textList.push(text);
    let outputElement = document.getElementById("output");
    outputElement.textContent = textList

}
</script>


## Dictionary Simulation

Welcome to the dictionary simulation! Below, you will find a list of words and their definitions. To view the definition of a word, simply click on the button next to it.

### Word List

- **Apple**  
  <button onclick="alert('A round fruit with a red, green, or yellow skin, and a white interior.')">View Definition</button>
  
- **Banana**  
  <button onclick="alert('A long, curved fruit with a yellow skin and a soft, sweet interior.')">View Definition</button>
  
- **Cactus**  
  <button onclick="alert('A plant with spiny stems and leaves that grow in arid regions.')">View Definition</button>
  
- **Dolphin**  
  <button onclick="alert('A marine mammal known for its intelligence, communication skills, and playful behavior.')">View Definition</button>
  
- **Elephant**  
  <button onclick="alert('A large, gray mammal with a long trunk and tusks, found in Africa and Asia.')">View Definition</button>


Dictionaries:

- A dictionary is a collection of key-value pairs that are unordered, mutable, and indexed.
- Dictionaries are defined using curly braces {} with key-value pairs separated by a colon (:).
- Keys in a dictionary should be unique and immutable (strings, numbers, and tuples), while values can be of any data type.
- Dictionaries can be accessed using the keys, using the squarebracket notation with the key name as the index.
- You can also use the .get() method to retrieve a value for a given key. If the key does not exist, the method returns None (or a default value if provided).
- Dictionaries have several built-in methods such as .keys(), .values(), and .items() to retrieve the keys, values, and key-value pairs respectively.
- You can add, update, and remove elements from a dictionary using various built-in methods.
## 2D Arrays:

- A 2D array, also known as a matrix, is a collection of elements arranged in rows and columns.
- A 2D array is defined using square brackets [] with each row separated by a comma, and each element within the row separated by a space.
- You can access individual elements within a 2D array using square brackets and the row and column indices (e.g. arr[row][column]).
- 2D arrays can be used to represent data that has two dimensions, such as an image or a spreadsheet.
- You can perform various operations on 2D arrays such as transposing (swapping rows and columns), adding and subtracting, and multiplying by a scalar or another matrix.
- There are several libraries available in Python, such as NumPy and Pandas, that provide more efficient and powerful tools for working with 2D arrays and matrices.


## Example Matrix / 2d array
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```
## Accessing Elements
To access an element in a 2D array, you need to specify the row and column indices. For example, to access the element in row 2, column 3 of the matrix array above (which contains the value 6), you would use the following syntax:

```python
element = matrix[1][2]   # row 2, column 3
```

### Modifying Elements
To modify an element in a 2D array, you can use the same syntax as for accessing elements. For example, to change the value of the element in row 2, column 3 of the matrix array above to 10, you would use the following syntax:

```python
matrix[1][2] = 10   # row 2, column 3
```

### Iterating and printing items
```python
for row in matrix:
    for element in row:
        print(element)
```



