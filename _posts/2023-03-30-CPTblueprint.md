---
toc: true
layout: post
description: CPT practice
title: CPT project blueprint
categories: [markdown, csp]
permalink: /csp/CPTprojectblueprint/
---


<html>
<style>
  .table {
    border: #795db3 solid;
    border-radius: 10px;
    border-collapse:separate;
  }
  .cell {
    border: 1px solid;
    text-align: center;
  }
  .container {
  }
  input {
    padding: 10px;
    background-color: #4a4a48;
    border: 0px;
    color: #b89cf0;
    border-radius: 15px;
  }
  input:focus, textarea:focus, select:focus{
    outline: none;
  }
  h3 {
    color: #A881F7;
    padding: 10px;
    padding-left: 0px;
    font-size: 25px;
  }
  .title {
    color: #A881F7;
    padding: 10px;
    font-size: 30px;
    text-align: center;
  }
  .button {
    border-radius: 10px;
    width: 50px;
    height: 30px;
    background: #A881F7;
    font-size: 15px;
    color: #1E1E1E;
    border-color: #795db3;
  }
  .timerButton {
    border-radius: 10px;
    background: #A881F7;
    font-size: 15px;
    color: #1E1E1E;
    border-color: #795db3;
  }
</style>

<div class='container'>
    

<h3> Add Activity </h3>
    <input id='newTask' type='text'>
<h3> Set Expected Time (hh:mm:ss)</h3>
    <input id='ExpectedTime' type='text'>

<br>
<h3> Time Passed </h3>
      <p id='TimePassed'>00:00:00</p>
      <br>
      <button class='timerButton' onclick='start()'> Start </button>
      <button class='timerButton' onclick='stop()'> Stop </button>
      <button class='timerButton' onclick='reset()'> Reset </button>
<br>
<br>
<button class='button' id='addTaskButton' onclick="addTask()">Add</button>
<!-- <br>
<br> -->
<!-- <h3> Real Time </h3>
<p id='Time' type='text'> -->
<!-- <h3 class="title"> To-Do </h3>
        <table class="table" id="toDo" style="width: 100%; margin-left: auto; margin-right: auto;">
          <tr>
            <th class="cell">Task</th>
            <th class="cell">Expected Time</th>
            <th class="cell">Actual Time</th>
            <th class="cell">Timer Controls</th>
          </tr>
        </table> -->
<h3 class="title"> Completed Tasks </h3>
        <table class="table" id="Completed" style="width: 100%; margin-left: auto; margin-right: auto;">
        <tr>
            <th class="cell">Task</th>
            <th class="cell">Expected Time</th>
            <th class="cell">Actual Time</th>
            <th class="cell">Decrease Time</th>
          </tr>
        </table>
<!-- </div> -->

<script>








const started = {}
const newtime = JSON.parse(localStorage.getItem('time')) || 0;
var taskInput = document.getElementById('newTask');
var addTaskButton = document.getElementById('addTaskButton');
var timeInput = document.getElementById('ExpectedTime');
// var addTimeButton = document.getElementById('addTimeButton');
var completedTask = document.getElementById('completedTasks');
var incompleteTasks = document.getElementById('Completed');
var timeBox = document.getElementById('Time')
var TimePassed = document.getElementById('TimePassed');

var tasks = []
var timeExpected = []
var storedtimes = []
function addTask() {
    var text = taskInput.value;
    tasks.push(taskInput.value)
    var timeExp = timeInput.value;
    timeExpected.push(timeInput.value)
    var ActualTime = 0;
    let temptime3 = JSON.parse(localStorage.getItem('time'));
    storedtimes.push(temptime3)
    localStorage.setItem('tasks', JSON.stringify(tasks));
    localStorage.setItem('TimeExpected', JSON.stringify(timeExpected));
    localStorage.setItem('storedtime', JSON.stringify(storedtimes));
    localStorage.setItem('ActualTime', JSON.stringify(ActualTime));
    var zero = 0
    localStorage.setItem('time', JSON.stringify(zero))
    TimePassed.innerHTML = "00:00:00"
    maketable(text, timeExp, temptime3)
    addtoLocal(text, timeExp, temptime3)
}


function calculatetime(time) {
  const hours = Math.floor(time / 3600)
  const hours2 = String(hours).padStart(2,'0')
  const minutes = Math.floor(time / 60);
  const minutes2 =  String(minutes).padStart(2,'0')
  const seconds = time % 60;
  const seconds2 =  String(seconds).padStart(2,'0')
  return hours + ":" + minutes + ":" + seconds
}



function Change(id2) {
    getList().then(function(items) {
    // console.log(items);


    let result = null;
    items.forEach(obj => {
    if (obj.id === id2) {
      result = obj;
    }
});
    const storedtimeValue = result.storedtime;
    console.log(storedtimeValue)
    var storedtimeValue2 = storedtimeValue -1;
    let data = {"id": id2, "storedtime": storedtimeValue2 };
    fetch(api+ '/timer', {
      method:'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
      .then((response) => {response.json()
      })
      
  })
}


// const started = {};
function maketable(text, timeExp, time, id) {
  // let seconds = newtime || 0;
  // let secondsFormatted = calculatetime(seconds)
  // let temptime2 = JSON.parse(localStorage.getItem('time'));
  var table = document.createElement('tr');
    table.innerHTML = "<th id=task class='cell'>" + text + "</th>" + 
                      "<th id=timeExp"  + "' class='cell'>" + timeExp + "</th>" + 
                      "<th id='Time" + "' class='cell'>" + calculatetime(time) + "</th>" + 
                      "<th class='cell'>" + 
                      "<button class='timerButton' onclick='Change(" + (id) + ")'>" + "Decrease" + "</button>"
                      "</th>";
    incompleteTasks.appendChild(table);
}


// for (let i = 0; i < task2.length; i++) {
//   tasks.push(task2[i])
//   timeExpected.push(timeExp[i])
//   maketable(task2[i], timeExp[i], i+1)
// }


function stop(i) {
  clearInterval(started[i].interval)
  started[i].yes = false
}
function start(i) {
  let temptime = JSON.parse(localStorage.getItem('time'));
  started[i] = {yes: true,date: new Date()};
  started[i].interval = setInterval(() => {
  let now = new Date()
  now.setSeconds(now.getSeconds() + (temptime || 0))
  let time = Math.round((now - started[i].date) / 1000);

  // setting the local storage time
  localtime = time || 0
  if (time === 30){
    alert("30 seconds passed!")
  }
  // }

  localStorage.setItem('time', JSON.stringify(localtime));
  const hours = Math.floor(time / 3600)
  const hours2 = String(hours).padStart(2,'0')
  const minutes = Math.floor(time / 60);
  const minutes2 =  String(minutes).padStart(2,'0')
  const seconds = time % 60;
  const seconds2 =  String(seconds).padStart(2,'0')
  TimePassed.innerHTML = `${hours2}:${minutes2}:${seconds2}`;
  }, 1000);
}

function reset() {
  // getList().then(console.log)
  // let zerotime = 0
  // started[i].date = new Date()
  // localStorage.setItem('time', JSON.stringify(zerotime));
  //  TimePassed.innerHTML = `00:00:00`
  // delete2()
  delete2()
}

const timeExp = JSON.parse(localStorage.getItem('TimeExpected'));
// const Realtime = JSON.parse(localStorage.getItem('ActualTime'));
const task2 = JSON.parse(localStorage.getItem('tasks'));
const storedtimes2 = JSON.parse(localStorage.getItem('storedtime'));

getList().then(function(items) {
  // console.log(items);
  let array = items
  for (let i = 0; i < array.length; i++) {
  const task = array[i];
  maketable(task.tasks, task.TimeExpected, task.storedtime, task.id);
  console.log(task.id)
  tasks.push(task.tasks)
  timeExpected.push(task.TimeExpected)
  storedtimes.push(task.storedtime)
}

});

