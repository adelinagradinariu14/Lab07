import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    """Riempie i due dropdown con i dati letti dal database tramite il Model.
        Va chiamato DOPO che la View ha creato i controlli (cioè dopo load_interface),
        altrimenti self._view.dd_biblioteca e self._view.dd_genere non esistono ancora."""
    # TODO
    def popola_dropdown(self):

        # --- Biblioteche ---
        # Prima voce: permette all'utente di non filtrare per biblioteca.
        # È solo un testo: sarà il callback a tradurlo in None per il DAO.
        self._view.dd_biblioteca.options.append(ft.dropdown.Option("Nessun filtro"))

        # Poi una voce per ogni biblioteca letta dal database (tramite il Model)
        # get_biblioteche() restituisce oggetti Biblioteca: si legge il campo con il punto.
        # Si usa il nome perché la query del DAO filtra su b.nome.
        for biblioteca in self._model.get_biblioteche():
            self._view.dd_biblioteca.options.append(ft.dropdown.Option(biblioteca.nome))

        # --- Generi ---
        # Prima voce: permette all'utente di non filtrare per genere
        self._view.dd_genere.options.append(ft.dropdown.Option("Nessun filtro"))

        # Poi una voce per ogni genere letto dal database (tramite il Model)
        # get_generi() restituisce già stringhe, quindi si passano direttamente
        for genere in self._model.get_generi():
            self._view.dd_genere.options.append(ft.dropdown.Option(genere))

        # --- Aggiornamento ---
        # Le opzioni sono state aggiunte in memoria: senza update() la pagina non le mostra
        self._view.update()

    # CALLBACKS DROPDOWN
    # TODO
    def handle_dd_biblioteca(self, e):
        # e è l'evento; il valore scelto dall'utente sta in e.control.value
        scelta = e.control.value

        # "Nessun filtro" è un testo dell'interfaccia: il Model/DAO vogliono None
        if scelta == "Nessun filtro":
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = scelta

    def handle_dd_genere(self, e):
        scelta = e.control.value

        if scelta == "Nessun filtro":
            self.genere_selezionato = None
        else:
            self.genere_selezionato = scelta


    # AZIONE: MOSTRA LIBRI
    # TODO
    def handle_mostra_libri(self, e):
        # SVUOTO LA LISTA: se l'utente preme il bottone più volte, senza questo i nuovi risultati
        # si accumulerebbero sopra quelli vecchi
        self._view.lv_filtrati.controls.clear()

        # CHIEDO I LIBRI AL MODEL: passo le due scelte memorizzate dai callback, nell'ordine che il DAO si aspetta
        # (prima biblioteca, poi genere)
        # Valgono None se l'utente ha scelto "Nessun filtro" o non ha toccato il dropdown.
        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)

        # CASO "NESSUN RISULTATO": una lista vuota vale False in un if
        # Mostro l'alert richiesto dalla consegna e mi fermo con return, così non provo a riempire una lista
        # senza elementi
        if not libri:
            self._view.show_alert("Nessun libro trovato con i filtri selezionati.")
            self._view.update()
            return

        # RIEMPIO LA LISTA: per ogni libro creo un Text e lo aggiungo ai controlli
        # => str(libro) usa il __str__ del DTO, che stampa tutti i campi del libro
        for libro in libri:
            self._view.lv_filtrati.controls.append(ft.Text(str(libro)))

        # AGGIORNO LO SCHERMO
        self._view.update()
