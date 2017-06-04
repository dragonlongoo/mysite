var tables = document.getElementsByTagName("table");
for (var i in tables) {
    var rows = tables[i].getElementsByTagName("tr");
    for (var j in rows) {
        if (j == 0) {
            rows[j].style.backgroundColor = "lightblue";
        }
        else if (j % 2 == 0) {
            rows[j].style.backgroundColor = "lightgreen";
        }
        else {
            rows[j].style.backgroundColor = "lightgrey";
        }
    }
}