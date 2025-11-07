function somma(a, b) {
    console.log(a + b);
}

function sottrazione(a, b) {
    console.log(a - b);
}

function moltiplicazione(a, b) {
    console.log(a * b);
}

function divisione(a, b) {
    console.log(a / b);
}

while (true) {
    let numero1 = prompt('inserisci il primo numero: ');

    if (numero1 === 'exit') {
        console.log('esco dalla calcolatrice...');
        break;
    }

    let numero2 = prompt('inserisci il secondo numero: ');
    const operatore = prompt('inserisci l\' operatore: ');

    numero1 = parseFloat(numero1);
    numero2 = parseFloat(numero2);

    if (numero1 === NaN || numero2 === NaN) {
        console.log('inserisci un numero valido');
        continue;
    }

    if (operatore === '/' && numero2 === 0) {
        console.log('il dividendo non può essere 0');
        continue;
    }

    if (operatore === '+') {
        somma(numero1, numero2);
    } else if (operatore === '-') {
        sottrazione(numero1, numero2)
    } else if (operatore === '*') {
        moltiplicazione(numero1, numero2);
    } else if (operatore === '/') {
        divisione(numero1, numero2);
    } else {
        console.log('operatore non valido');
    }
}
