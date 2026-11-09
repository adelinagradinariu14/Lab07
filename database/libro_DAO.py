from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO
    # Funzione incaricata di leggere tutti i generi dal database con SQL
    def leggi_generi(self):
        cnx = DBConnect.get_connection()
        # CONNESSIONE: get_connection è un metodo di classe (@classmethod), quindi si chiama
        # direttamente su DBConnect (senza creare un'istanza)
        # Restituisce una connessione presa in prestito dal pool (insieme di connessioni riutilizzabili),
        # oppure None se fallisce
        if cnx is not None:
            print("Connessione database eseguita")

            query ="""SELECT DISTINCT `genere` FROM libro"""
            cursor = cnx.cursor() # cursore è l'oggetto che esegue la query e permette di leggere le righe
            cursor.execute(query)
            # Leggo tutto dal cursore in una variabile (poi da restituire)
            generi_tot = []
            for row in cursor: #ogni row è una tupla di un elemento qui, ad esempio ('Fantasy', )
                genere = row[0]
                generi_tot.append(genere)

            # chiudo prima il cursore, poi la connessione.

            cursor.close()
            cnx.close()
            print("Generi letti dal database")
            return generi_tot #lista di generi per il Model

    def filtra_libri(self, biblioteca, genere):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            print("Connessione database eseguita")

            query = """ SELECT l.`id`, l.`titolo`, l.`autore`, l.`genere`, l.`anno_pubblicazione`, l.`id_biblioteca` 
                        FROM libro l, biblioteca b
                        WHERE b.`nome` = COALESCE(%s, b.nome)
                        AND l.`genere` = COALESCE(%s, l.genere)
                        AND l.`id_biblioteca` = b.`id` """

            cursor = cnx.cursor()
            cursor.execute(query, (biblioteca, genere))

            libri_filtrati = []
            for row in cursor:
                libro = Libro(*row)
                libri_filtrati.append(libro)

            cursor.close()
            cnx.close()
            print("Ho filtrato i libri dal database")
            return libri_filtrati


