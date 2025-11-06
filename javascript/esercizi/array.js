// esercizio 1
// creare una lista come questa: const punteggi = [80, 95, 70, 100]; poi aggiungere un punteggio di 85 alla lista, poi fare il console.log del primo e dell'ultimo elemento e infine fare il console.log della media dei punteggi
const punteggi = [80, 95, 70, 100];
punteggi.push(85);
console.log('primo elemento', punteggi[0]);
console.log('ultimo elemento', punteggi[punteggi.length - 1]);
const somma = punteggi[0] + punteggi[1] + punteggi[2] + punteggi[3] + punteggi[4];
//const somma = punteggi.reduce((acc, curr) => acc + curr, 0);
const media = somma / punteggi.length;
console.log('media', media);

// esercizio 2
// data una lista come questa: const colori = ['rosso', 'verde', 'blu', 'giallo']; controllare se il blu esiste nella lista e in caso positivo fare il console.log di 'blu trovato!' poi sostituire il verde con il viola e infine fare il console.log della lista aggiornta
const colori = ['rosso', 'verde', 'blu', 'giallo'];

// Controllo se 'blu' esiste nella lista
if (colori.includes('blu')) {
    console.log('blu trovato!');
}

// Sostituisco 'verde' con 'viola'
const indiceVerde = colori.indexOf('verde');
if (indiceVerde !== -1) {
    colori[indiceVerde] = 'viola';
}

// Stampo la lista aggiornata
console.log(colori);
