---
toc: true
layout: post
description: Binary Calculator
title: Binary Calculator
categories: [markdown, csp]
permalink: /BinaryCalculator/
---

<html>
 <body>
 
<table>
  <tr>
    <td colspan="4"> <input class="display-box" type="text" id="output"/> </td>
  </tr>
  <tr>
    <td> <input type="button" value="1" onclick="input('1')" /> </td>
    <td> <input type="button" value="2" onclick="input('2')" /> </td>
    <td> <input type="button" value="3" onclick="input('3')" /> </td>
    <td> <input type="button" value="/" onclick="input('/')" /> </td>
  </tr>
  <tr>
    <td> <input type="button" value="4" onclick="input('4')" /> </td>
    <td> <input type="button" value="5" onclick="input('5')" /> </td>
    <td> <input type="button" value="6" onclick="input('6')" /> </td>
    <td> <input type="button" value="-" onclick="input('-')" /> </td>
  </tr>
  <tr>
    <td> <input type="button" value="7" onclick="input('7')" /> </td>
    <td> <input type="button" value="8" onclick="input('8')" /> </td>
    <td> <input type="button" value="9" onclick="input('9')" /> </td>
    <td> <input type="button" value="+" onclick="input('+')" /> </td>
  </tr>
  <tr>
    <td> <input type="button" value="C" onclick="empty()" /> </td>
    <td> <input type="button" value="0" onclick="input('0')" /> </td>
    <td> <input type="button" value="=" onclick="input('calculate')" id="btn" /> </td>
    <td> <input type="button" value="*" onclick="input('*')" /> </td>
  </tr>
</table>
</body>
</html>
<script>  
function empty() {
  inputs = ""
  document.getElementById("output").value = ""
}
let inputs = ""
let oldinput = ""
function input(data) {
  const parsed = Number.parseInt(data)
  let input = ""
  if (!isNaN(parsed)){
    inputs += parsed.toString()
    document.getElementById("output").value = inputs
  }else if (data ==='calculate') {
    console.log(oldinput)
  } else{    
    console.log(data)
    console.log("applying " + data + " to " + inputs)
    document.getElementById("output").value = inputs + data
     oldinput = inputs
    inputs = ""
  } 
}
</script>