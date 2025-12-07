const attack = document.getElementById('id_attack')
attack.setAttribute('max', '255')
const div = document.createElement('div');
const nextNode = attack.nextSibling;

attack.parentElement.insertBefore(div, nextNode);

attack.addEventListener('input', () => {
    const procentage = parseInt((attack.value / 255) * 100);
    console.log(procentage + '%')
    div.style.width = procentage + '%';
    div.style.height = 10 + 'px';
    div.style.marginTop = '5px';

    if (procentage > 50) {
       div.style.backgroundColor = 'green';
  
    } else {
        div.style.backgroundColor = 'red';
    }
})