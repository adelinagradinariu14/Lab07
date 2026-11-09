from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # Funzione incaricata di leggere le biblioteche (tutte) dal database con SQL
    def leggi_biblioteche(self):
        cnx = DBConnect.get_connection()
        # CONNESSIONE: get_connection è un metodo di classe (@classmethod), quindi si chiama
        # direttamente su DBConnect (senza creare un'istanza)
        # Restituisce una connessione presa in prestito dal pool (insieme di connessioni riutilizzabili),
        # oppure None se fallisce
        if cnx is not None:
            print("Connessione database eseguita")

            query ="""SELECT `id`, `nome`, `indirizzo` FROM biblioteca"""
            cursor = cnx.cursor() # cursore è l'oggetto che esegue la query e permette di leggere le righe
            cursor.execute(query)
            # Leggo tutto dal cursore in una variabile (poi da restituire)
            biblioteche_tot = []
            for row in cursor: #ogni row è una tupla, ad esempio (1, 'Nome...', 'Indirizzo...')
                biblioteca = Biblioteca(*row) # *row spacchetta la tupla nei 3 argomenti del costruttore
                # => equivale a Biblioteca(row[0], row[1], row[2])
                biblioteche_tot.append(biblioteca)

            # chiudo prima il cursore, poi la connessione.

            cursor.close()
            cnx.close()
            print("Biblioteche lette dal database")
            return biblioteche_tot #lista di oggetti Biblioteca per il Model

