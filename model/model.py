from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        # Il Model possiede un'istanza di ciascun DAO e li usa per leggere i dati
        # Non contiene query SQL: quelle stanno solo nei DAO
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        # Riceve già dati "puliti": il valore "Nessun filtro" è tradotto in None dal Controller,
        # che è l'unico a conoscere i testi dell'interfaccia.
        # Qui basta inoltrare i parametri al DAO, nello stesso ordine in cui li aspetta filtra_libri
        # (prima biblioteca, poi genere)!!!!
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        # TODO
        return self._libro_dao.filtra_libri(biblioteca, genere)

    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        # TODO
        # Delega a LibroDAO: restituisce una lista di stringhe (es. ["Fantasy", ...])
        return self._libro_dao.leggi_generi()

    # --- BIBLIOTECHE ---
    # legge le righe del dataase (fornite dal DAO)
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        # TODO
        # Delega a BibliotecaDAO: restituisce una lista di oggetti Biblioteca
        return self._biblioteca_dao.leggi_biblioteche()
        # NB return <oggetto che possiede il metodo>.<metodo>(parametri se ci sono) !!!!!!!!
