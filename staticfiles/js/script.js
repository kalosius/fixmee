let sidenave = document.querySelector('.sidenav');
let sidedisplay = document.querySelector('#sidedisplay');
let sideclose = document.createElement('button');
sideclose.textContent = 'X';
sideclose.style.position = 'absolute';
sideclose.style.top = '10px';
sideclose.style.right = '10px';
sideclose.style.padding = '30px';
sideclose.style.background = 'transparent';
sideclose.style.border = 'none';
sideclose.style.fontSize = '20px';
sideclose.style.cursor = 'pointer';
sideclose.style.color = '#fff';

sidenave.appendChild(sideclose);

sidedisplay.addEventListener('click', function() {
    sidenave.style.display = 'block';
});

sideclose.addEventListener('click', function() {
    sidenave.style.display = 'none';
});
