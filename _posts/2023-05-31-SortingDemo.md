

<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
    <div class="app">
        <h1>Simple Sorting App</h1>
        <form id="nameForm">
            <input type="text" id="nameInput" placeholder="Enter a name" required>
            <button type="submit">Add name</button>
        </form>
        <button id="sortAsc">Sort Ascending</button>
        <button id="sortDesc">Sort Descending</button>
        <ul id="nameList"></ul>
    </div>
    <script src="script.js"></script>
</body>

<style>
body {
    font-family: Arial, sans-serif;
    padding: 20px;
    background-color: #f9f9f9;
}

.app {
    max-width: 500px;
    margin: 0 auto;
}

button {
    margin: 10px 0;
}
</style>
</html>

<script>
document.addEventListener("DOMContentLoaded", function() {
    var nameForm = document.getElementById("nameForm");
    var nameInput = document.getElementById("nameInput");
    var nameList = document.getElementById("nameList");
    var sortAsc = document.getElementById("sortAsc");
    var sortDesc = document.getElementById("sortDesc");

    var names = [];

    nameForm.addEventListener("submit", function(e) {
        e.preventDefault();

        if(nameInput.value) {
            names.push(nameInput.value);
            renderList();
            nameInput.value = "";
        }
    });

    sortAsc.addEventListener("click", function() {
        names.sort();
        renderList();
    });

    sortDesc.addEventListener("click", function() {
        names.sort().reverse();
        renderList();
    });

    function renderList() {
        nameList.innerHTML = "";
        for(let name of names) {
            let li = document.createElement("li");
            li.textContent = name;
            nameList.appendChild(li);
        }
    }
});

</script>
