import sqlite3

c = sqlite3.connect("data.db")

cur = c.cursor()
cur.execute("CREATE TABLE Bateau(id_bateau, position);")
cur.execute("CREATE TABLE Mesures(id_bateau, temperature, Ph, date, heure);")
cur.execute("CREATE TABLE Utilisateur(id_bateau, id_utilisateur);")