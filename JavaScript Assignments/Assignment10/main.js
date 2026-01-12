// Task:
// 1.	Create an image element on the page.
// 2.	Create a button labeled "Change Image".
// 3.	When the button is clicked, change the `src` attribute of the image to a different image URL.
// 4.	Bonus : Change the button's text to "Image Changed" after the click.
function change(){
    document.getElementById('image').src='img/i2.avif';
    document.getElementById('img-button').innerHTML="Image Chnaged";
}