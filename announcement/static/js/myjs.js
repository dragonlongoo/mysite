var tables = document.getElementsByTagName("table");

for (var index in tables) {
    var rows = tables[index].getElementsByTagName("tr")
    {
        for (var index in rows) {
            if (index == 0) {
                rows[index].style.backgroundColor = "lightblue";
            }
            else if (index % 2 == 0) {
                rows[index].style.backgroundColor = "lightgreen";
            }
            else {
                rows[index].style.backgroundColor = "lightgrey";
            }
        }
    }
}
