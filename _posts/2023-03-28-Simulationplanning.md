---
toc: true
layout: post
description: Simulation Ideas
title: Simulations
categories: [markdown, csp]
permalink: /csp/sikmulationideas/
---

# Simulation 1
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


  ![image](https://user-images.githubusercontent.com/110933283/227842200-68645d7c-db38-49b4-b701-7ed10f29e4e8.png)

