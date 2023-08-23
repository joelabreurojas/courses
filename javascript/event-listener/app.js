//Lesson 1 - Mouse

const element = document.getElementById('app');
element.style.background = '#333';
element.style.color = '#fff';
element.style.padding = '20px';
element.innerText = 'Text';

/*
document.querySelector('#app').addEventListener('mousemove', typeEvent);

//click ; dblclick ; mouseenter ; mouseleave ; mouseover ; mouseout
//mousedown ; mouseup ; mousemove ;


function sayHi(event) {
    event.preventDefault();
    let element = event.target.id;
    console.log(element);
}


function typeEvent(event) {
    console.log(`Event: ${event.type}` );
}

//Lesson 2 - Inputs

element.addEventListener('input', typeEvent)

//keydown, keyup, keypress, focus, blur, cut, copy, paste, input, change
*/

//Lesson 3 - Event Bubbling

/*
Example:
element.addEventListener('click', function(event) {
    e.stopPropagation();
});
*/