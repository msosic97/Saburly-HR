function showDiv1() {
    document.getElementById('second-container').style.display = "none";
    document.getElementById('first-container').style.display = "block";
}

function showDiv2() {
    document.getElementById('card').style.display = "block";
}

function showDiv3() {
    document.getElementById('first-container').style.display = "none";
    document.getElementById('second-container').style.display = "block";
    document.getElementById('second-container').innerHTML= "Biti ce bolje aBd, ali ne vjerujem. Provjerite je li placena vezifa!";
}
