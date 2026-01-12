let timeleft=10;
setInterval(function(){
    if(timeleft<0){
        document.getElementById("timer").textContent="";
        document.getElementById("end").textContent="Time's up!"

    }else{
        document.getElementById("timer").textContent=timeleft +" Seconds Left";
        timeleft-=1;
    }

},1000)