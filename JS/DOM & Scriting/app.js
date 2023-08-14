// Lesson 1
let element;

element = document;
element = document.all;
element = document.all[10];
element = document.head;
element = document.body;
element = document.domain;
element = document.URL;
element = document.characterSet;
element = document.forms;
element = document.className;
element = document.classList;

element = document.scripts;
element = document.images;

let images = document.images;
let imagesArr = Array.from(images)

imagesArr.forEach(function(image) {
    console.log(image);
});

console.log(imagesArr);

// Lesson 2 - getElementById
element = document.getElementById('app');
element.style.background = '#333';
element.style.color = '#fff';
element.style.padding = '20px';

element.innerText = 'Text';

console.log(element.innerText);

//Lesson 3 - Query Selector
const header = document.querySelector('#app'); //First element 'app'

header.style.background = '#ff1';
header.style.color = '#333';
header.style.padding = '50px';
header.textContent = 'Hi world!';

console.log(header);

const title = document.getElementsByTagName('h1')

console.log(title)

//Lesson 4 - Query Selector All

// const a = document.querySelectorAll('#app');             #id .clss

//Lesson 5 - Traversing   (Travel Father-Child)

/*
const navegate = document.querySelector('#principal') --> nav
console.log(navegate.childNodes)  --> You can see the spaces...
console.log(navegate.children)  --> Only see the elements...

console.log(navegate.children.nodeName) --> A
console.log(navegate.nodeName)          --> NAV

console.log(navegate.children.nodeType)

1 = Elments HTML
2 = Atributtes
3 = Text Node
8 = Comments
9 = Documments
10 = DocType
*/

//Lesson 5 - Traversing   (Travel Child-Father)

/*
const links = document.querySelectorAll('.link');

console.log(links[0].parentNode); --> main Navigate
console.log(links[0].parentElement); --> most recommended

Example:
console.log(links[0].parentElement.children[0].textContent = 'New Text');

console.log(links[1].previousELementSibling); --> to link[0]
*/

//Lesson 6 - Create Element

/*
const link = document.createElement('a');

link.className = 'link';
link.id = 'new-id';
link.setAttribute('href','#');
link.textContent = 'New Link';

document.querySelector('Secondary').appendChild(link);
console.log(link);
*/

//Lesson 7 - Modificate element

const father = document.createElement('h1');
father.id='header';
father.appendChild(document.createTextNode('First Node'));

const oldHeader = document.createElement('h2');
oldHeader.id='lowheader';
oldHeader.appendChild(document.createTextNode('Old Text'));

//Relation Father-Son
document.querySelector('#header');
father.appendChild(oldHeader);

const newHeader = document.createElement('h2');
newHeader.id='lowheader';
newHeader.appendChild(document.createTextNode('New Text'));

//Replace son
father.replaceChild(newHeader, oldHeader);

//Lesson 8 Eliminate element
father.removeChild(newHeader) //or newHeader.remove();
console.log(father);

// .removeAttribute('data-id');