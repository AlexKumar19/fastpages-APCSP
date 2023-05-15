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
    <title>Favorite Foods</title>
    <script>
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
</head>
<body>
    <h1>Favorite Foods</h1>
    <ul id="food-list"></ul>
    <input type="text" id="food-input">
    <button onclick="addFood()" id="add-button">Add Food</button>
    <button onclick="stopAdding()" id="stop-button">Stop</button>
    <br><br>
    <button onclick="callAPI()">Get Cuisine Recommendation</button>
    <input type="text" id="foods">
</body>
</html>
