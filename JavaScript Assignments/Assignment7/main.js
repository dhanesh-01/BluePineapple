// Task:
// 1.	Create a form with the following fields:
// - Name (required)
// - Email (required, should be a valid email)
// - Age (optional, should be a number greater than 18)
// 2.	On form submission, validate the following:
// - The Name field should not be empty.
// - The Email field should contain a valid email format.
// - If the Age field is provided, it should be greater than 18.
// 3.	Display error messages for each invalid field.
// 4.	Prevent form submission if any of the fields are invalid.

document.getElementById('myform').addEventListener('submit', function(e) {
    e.preventDefault();

    if(document.getElementById('name').value === " "){
        document.getElementById("invalid_name").innerHTML = "Name should not be empty";
    }
    if(document.getElementById('age').value<18){
        document.getElementById("invalid_age").innerHTML = "Age should be greater than 18";
    }

    const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if(!pattern.test(document.getElementById('email').value)){
        document.getElementById("invalid_email").innerHTML ="Invalid Email";
    }
})