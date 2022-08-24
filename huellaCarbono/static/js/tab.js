let tabHeader = document.getElementsByClassName("tab-header")[0];
let tabIndicator = document.getElementsByClassName("tab-indicator")[0];
let tabBody = document.getElementsByClassName("tab-body")[0];

let tabsPane = tabHeader.getElementsByTagName("div");
for(let i = 0;i < tabsPane.length; i++){
    tabsPane[i].addEventListener("click", function(){
        tabHeader.getElementsByClassName("active")[0].classList.remove("active");
        tabsPane[i].classList.add("active");

        tabBody.getElementsByClassName("row-categoria active")[0].classList.remove("active");
        //tabBody.getElementsByTagName("div")[i].classList.add("active");
        tabBody.getElementsByClassName("row-categoria")[i].classList.add("active");
        tabIndicator.style.left = `calc( calc(100%/5) * ${i})`;
   
    });
}

function _class(name){
    return document.getElementsByClassName(name);
}

let tabPanes = _class("tabs-vertical-header alimentacion")[0].getElementsByTagName("div");
for(let i=0 ; i <tabPanes.length ; i++){
    tabPanes[i].addEventListener("click", function(){
        _class("tabs-vertical-header alimentacion")[0].getElementsByClassName("active")[0].classList.remove("active");
        tabPanes[i].classList.add("active");

        _class("tabs-vertical-indicator alimentacion")[0].style.top = `calc(50px + ${i*50}px)`;

        _class("tabs-vertical-content alimentacion")[0].getElementsByClassName("active")[0].classList.remove("active");
        _class("tabs-vertical-content alimentacion")[0].getElementsByTagName("div")[i].classList.add("active");
    });
}