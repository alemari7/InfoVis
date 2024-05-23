# Visualizzazione delle Informazioni - Progetto

## Descrizione del Progetto

Questo progetto è stato sviluppato per il corso di Visualizzazione delle Informazioni. Il task consiste nel creare una visualizzazione interattiva utilizzando D3.js. I dettagli del task sono i seguenti:

- Crea un file JSON con dei dati multivariati: ci sono 8 data-cases e ogni data-case ha sei variabili quantitative i cui valori sono tutti positivi.
- In base a questi dati, disegna 8 foglie (è sufficiente la silhouette) distribuite nell'area di disegno come se galleggiassero sull'acqua.
- Ogni foglia corrisponde a un data-case e utilizza la variabile 1 e la variabile 2 per determinare la sua coordinata x e la sua coordinata y.
- Sotto ogni foglia c'è un pesciolino (è sufficiente la silhouette) che però all'inizio non si vede perché è coperto dalla foglia.
- Cliccando con il pulsante sinistro del mouse su una foglia, tutte le foglie si spostano nelle posizioni determinate dalle variabili 3 e 4 dei rispettivi data-cases.
- Solo dopo che le foglie sono arrivate nella loro posizione finale, anche i pesciolini si muovono e si posizionano sotto le loro foglie.
- Al click successivo vengono utilizzate le variabili 5 e 6 per le coordinate e al click ancora successivo si torna alla configurazione iniziale.
- I cambi di posizione delle foglie e dei pesciolini avvengono con un'animazione fluida.
- Usa le scale D3.js per mappare l'intervallo dei valori delle variabili (che deve poter essere arbitrario) sull'intervallo dei valori delle coordinate, che dipende dalla tua interfaccia.

## Struttura dei File

Nella cartella del progetto sono presenti i seguenti file:

- `progetto.html`: Contiene il codice HTML e JavaScript per la visualizzazione.
- `data.json`: Contiene i dati multivariati necessari per la visualizzazione.
- `README.md`: Questo file, che descrive il progetto e come eseguire il server locale.

## Esecuzione del Progetto

Per lanciare il programma e abilitare un server locale, esegui il seguente comando dal terminale nella directory del progetto:

```sh
python3 -m http.server 8000
