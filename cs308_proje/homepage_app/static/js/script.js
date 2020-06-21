var searchBut = document.querySelector("#searchBut");
searchBut.addEventListener("keyup",function (e){
    var university = e.target.value.toLowerCase();
    var span_items = document.querySelectorAll({"university_table":table});

    span_items.forEach(function(item){
        if(item.textContent.toLowerCase().indexOf(university)!= -1){
            item.closest("li").style.display = "block";
        }
        else if(item.textContent.toLowerCase().indexOf(city)!= -1){
            item.closest("li").style.display = "block";
        }
        else if(item.textContent.toLowerCase().indexOf(faculty)!= -1){
            item.closest("li").style.display = "block";
        }

        else{
            item.closest("li").style.display = "none";
        }

    })

})