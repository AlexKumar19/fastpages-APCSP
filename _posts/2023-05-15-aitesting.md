---
toc: true
layout: post
description: Ai stuff
title: AI work
categories: [markdown, csp]
permalink: /csp/aiworktesting/
---



<!DOCTYPE html>
<html>

<head>
  <style>
    #ship-animation {
      font-family: monospace;
      font-size: 20px;
    }
  </style>
</head>
<body>
<h1>Favorite Foods</h1>
    <ul id="food-list"></ul>
    <input type="text" id="food-input">
    <button onclick="addFood()" id="add-button">Add Food</button>
    <button onclick="stopAdding()" id="stop-button">Stop</button>
    <br><br>
    <button onclick="callAPI(); ship()">Get Cuisine Recommendation</button>
    <p id="foods"></p>
  <pre id="ship-animation"></pre>

  <script>
    function shipPrint(position) {
      const animationElement = document.getElementById('ship-animation');
      const spaces = ' '.repeat(position);

      const frame = `${spaces} .   \n${spaces}  .   \n${spaces}    .\n\\~~~~~/\n \\   /\n  \\ /\n   V\n   |\n   |\n------`;

      animationElement.textContent = frame;
    }

    async function ship() {
      const start = 0;
      const distance = 3;
      const step = 2;
	
      for (let position = start; position < distance; position += step) {
        shipPrint(0);
        await sleep(1000);
        shipPrint(2);
        await sleep(1000);
      }
    }

    function sleep(ms) {
      return new Promise(resolve => setTimeout(resolve, ms));
    }
    function callAPI() {
            var api_key = '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';
            var endpoint = 'https://api.openai.com/v1/completions';
            var headers = {
                'Authorization': 'Bearer ' + api_key,
                'Content-Type': 'application/json'
            };
            var text = document.getElementById('foods').value;
            var data = {
                'model': 'text-davinci-003',
                'prompt': "Give me a specific cuisine that I would like based on the foods that I like. Here are the foods: " + text,
                'max_tokens': 100
            };
            fetch(endpoint, {
                method: 'POST',
                headers: headers,
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(result => {
                var completed_text = result.choices[0].text;
                console.log(completed_text);
                 			document.getElementById('foods').innerHTML = completed_text
                
            });
        }
        function addFood() {
            var foodInput = document.getElementById('food-input');
            var food = foodInput.value.trim();
            if (food !== '') {
                var foodList = document.getElementById('food-list');
                var foodItem = document.createElement('li');
                foodItem.textContent = food;
                foodList.appendChild(foodItem);
                foodInput.value = '';
            }
        }
        function stopAdding() {
            callAPI();
            document.getElementById('food-input').disabled = true;
            document.getElementById('add-button').disabled = true;
            document.getElementById('stop-button').disabled = true;
        }

    
  </script>
</body>
</html>
