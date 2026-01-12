function show(){
    document.getElementById("inner").style.display="block";
}
document.getElementById("close").addEventListener("click",function(){
    document.getElementById("inner").style.display="none";
})