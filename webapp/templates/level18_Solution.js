var buttons = document.getElementsByTagName('button');

for (i=0;i<buttons.length;i=i+1) {
    if (buttons[i].innerText != 'Home'){
        buttons[i].click()
    }
}