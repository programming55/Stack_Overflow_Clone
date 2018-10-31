
function panel1(){
    pid1 = document.getElementById("panel-but1")
    pid1.classList.toggle("active");
    var panel = pid1.nextElementSibling;
    if (panel.style.maxHeight){
    panel.style.maxHeight = null;
    } else {
    panel.style.maxHeight = panel.scrollHeight + "px";
    } 
}
function panel2(){
    pid2 = document.getElementById("panel-but2")
    pid2.classList.toggle("active");
    var panel = pid2.nextElementSibling;
    if (panel.style.maxHeight){
    panel.style.maxHeight = null;
    } else {
    panel.style.maxHeight = panel.scrollHeight + "px";
    } 
}
function panel3(){
    pid3 = document.getElementById("panel-but3")
    pid3.classList.toggle("active");
    var panel = pid3.nextElementSibling;
    if (panel.style.maxHeight){
    panel.style.maxHeight = null;
    } else {
    panel.style.maxHeight = panel.scrollHeight + "px";
    } 
}