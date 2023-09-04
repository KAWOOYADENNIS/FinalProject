//assign all elements
const demoId = document.getElementById('demo');
const demoClass = document.getElementsByClassName('demo');
const demoTag = document.getElementsByTagName('article');
const demoQuery = document.querySelector('#demo-query');
const demoQueryAll = document.querySelectorAll('.demo-query-all');


//change border of id demo to purple
demoId.style.border = '3px solid purple';


//change border of class demo to orange
for (i = 0; i < demoClass.length; i++){
    demoClass[i].style.border ='3px solid orange'
}

//change border of tag demo to red
for (i = 0; i < demoTag.length; i++){
    demoTag[i].style.border ='3px solid red'
}