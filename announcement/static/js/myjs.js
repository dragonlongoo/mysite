var tables = document.getElementsByTagName("table");

for (var i=0; i<tables.length; i++) {

    var rows = tables[i].getElementsByTagName("tr");
    for (var j=0; j<rows.length; j++){
        if(j==0){
            rows[j].style.backgroundColor = "lightblue";
        }
        else if(j%2==0){
            rows[j].style.backgroundColor = "lightgreen";
        }
        else{
            rows[j].style.backgroundColor = "lightgrey";
        }
    }
}