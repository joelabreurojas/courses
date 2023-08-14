localStorage.setItem('name', 'Pablo');
sessionStorage.setItem('name', 'Pablo');

const item = localStorage.getItem('name');

localStorage.removeItem('name');

console.log(item);