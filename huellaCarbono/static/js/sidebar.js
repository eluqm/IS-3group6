//let sidebarToggle = document.querySelector(".sidebarToggle");
let sidebarToggle = document.querySelector(".sidebarToggle");
sidebarToggle.addEventListener("click",function(){
    document.querySelector("body").classList.toggle("active");
    document.getElementById("sidebarToggle").classList.toggle("active");
});



let sidebarInformation = document.querySelector(".sidebarInformation");
sidebarInformation.addEventListener("click",function(){
    document.querySelector("body").classList.toggle("active");
    document.getElementById("sidebarToggle").classList.toggle("active");
});