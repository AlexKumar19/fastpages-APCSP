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