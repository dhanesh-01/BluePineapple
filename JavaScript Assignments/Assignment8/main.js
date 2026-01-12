// Objective:
// 
// Task:
// 1.	Create an HTML page with a `<div>` that has a class `box` (with a default background color like lightblue).
// 2.	Create a button labeled "Toggle Color".
// 3.	When the button is clicked, toggle the class `highlight` on the `<div>`, changing its background color (e.g., change to red when the class is added and back to lightblue when removed).
// 4.	Use JavaScript to manipulate the class of the `<div>`.
function change(){
    // console.log(document.getElementById('myDiv').className);
    if(document.getElementById('myDiv').className==='box'){
        document.getElementById('myDiv').className='highlight';
    }else{
        document.getElementById('myDiv').className='box';
    }
    


}