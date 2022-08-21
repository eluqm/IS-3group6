let tabHeader = document.getElementsByClassName("tab-header")[0];

let tabIndicator = document.getElementsByClassName("tab-indicator")[0];

let tabBody = document.getElementsByClassName("tab-body")[0];

let tabsPane = tabHeader.getElementsByTagName("div");

for (let index = 0; index < tabsPane.length; index++) {
    tabsPane[index].addEventListener("click", function() {
        tabHeader.getElementsByClassName("active")[0].classList.remove('active');
        tabsPane[index].classList.add("active");
        tabBody.getElementsByClassName("active")[0].classList.remove("active");
        tabBody.getElementsByTagName("div")[index].classList.add("active")
    });
}

