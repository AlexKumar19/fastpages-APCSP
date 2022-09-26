---
toc: true
layout: post
description: Generates random Basketball data
title: Basketball Data Generator
categories: [markdown, csp]
permalink: /Basketballdatagen/
---
# NBA generator
- This is a button that will randomly generate a name from a great player in the NBA

<button id="1">Click Me!</button>
<p id="random"></p>

<script> 
var players = ["Stephen Curry" , "LeBron James", "Michael Jordan", "Kareem Abdul-Jabbar", "Kobe Bryant", "Shaquille ONeal", "Larry Bird", "Wilt Chamberlain", "Magic Johnson"]
var random = players[Math.floor(Math.random()*players.length)];
var button = document.getElementById("1")
        var random2 = document.getElementById("random")
        button.onclick=function() {
            random2.innerHTML = random
        }
</script>

This is how it works:

```javascript

var players = ["Stephen Curry" , "LeBron James", "Michael Jordan", "Kareem Abdul-Jabbar", "Kobe Bryant", "Shaquille ONeal", "Larry Bird", "Wilt Chamberlain", "Magic Johnson"]
var random = players[Math.floor(Math.random()*players.length)];
var button = document.getElementById("1")
        var random2 = document.getElementById("random")
        button.onclick=function() {
            random2.innerHTML = random
        }
```