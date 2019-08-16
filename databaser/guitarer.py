import sqlite3


#Her oprettes en forbindelse til databasefilen
#Hvis filen ikke findes, vil sqlite oprette en ny tom database.
con = sqlite3.connect('guitarer.db')
print('Database åbnet')

try:
    con.execute("""DROP TABLE IF EXISTS guitarmodeller;""")
    con.execute("""DROP TABLE IF EXISTS guitarister;""")
    con.execute("""DROP TABLE IF EXISTS guitaristmodeller;""")
    con.execute("""DROP TABLE IF EXISTS producenter;""")

    print('Tabel slettet')
except Exception as e:
    print('Fejl ved sletning af tabel')

try:
    con.execute("""CREATE TABLE guitarmodeller (
		id INTEGER PRIMARY KEY,
		navn TEXT,
        producent INT,
        årstal INTEGER);""")

    con.execute("""CREATE TABLE guitarister (
		id INTEGER PRIMARY KEY,
		navn TEXT);""")

    con.execute("""CREATE TABLE guitaristmodeller (
		id INTEGER PRIMARY KEY,
		guitarist_id INTEGER,
        model_id INTEGER);""")

    con.execute("""CREATE TABLE producenter (
		id INTEGER PRIMARY KEY,
		navn TEXT,
        lokation TEXT);""")



    print('Tabel oprettet')
except Exception as e:
    print('Tabellen findes allerede')

con.execute("""INSERT INTO guitarmodeller (navn, producent, årstal) VALUES ('Stratocaster', 1, '1954');""")
con.execute("""INSERT INTO guitarmodeller (navn, producent, årstal) VALUES ('ES-335', 3, '1954');""")
con.execute("""INSERT INTO guitarmodeller (navn, producent, årstal) VALUES ('N-20', 2, '1969');""")
con.execute("""INSERT INTO guitarmodeller (navn, producent, årstal) VALUES ('Telecaster', 1, '1950');""")

con.execute("""INSERT INTO guitarister (navn) VALUES ('Wes Montgomery');""")
con.execute("""INSERT INTO guitarister (navn) VALUES ('Willie Nelson');""")
con.execute("""INSERT INTO guitarister (navn) VALUES ('Tom Morello');""")

con.execute("""INSERT INTO guitaristmodeller (guitarist_id, model_id) VALUES (1,2);""")
con.execute("""INSERT INTO guitaristmodeller (guitarist_id, model_id) VALUES (2,3);""")
con.execute("""INSERT INTO guitaristmodeller (guitarist_id, model_id) VALUES (3,2);""")
con.execute("""INSERT INTO guitaristmodeller (guitarist_id, model_id) VALUES (3,4);""")

con.execute("""INSERT INTO producenter (navn, lokation) VALUES ('Fender','USA');""")
con.execute("""INSERT INTO producenter (navn, lokation) VALUES ('Martin','USA');""")
con.execute("""INSERT INTO producenter (navn, lokation) VALUES ('Gibson','USA');""")

#Efter at have ændret i databasen skal man kalde funktionen commit.
con.commit()

inp = ''


print('')
print('Kommandoer: ')
print('  vis - Viser en masse fra databasen')
print('  order - Brug order sammen med SELECT, til at sortere')
print('  ny  - Opret ny guitar')
print('  entilmange  - Brug JOIN til en en-til-mange relation')
print('  entilmange  - Brug JOIN til en mange-til-mange relation')
print('  q   - Afslut program')

while not inp.startswith('q'):
    inp = input('> ')

    if inp == 'vis':
        c = con.cursor()
        c.execute('SELECT * FROM guitarmodeller;')

        for p in c:
            print('guitar: {}'.format(p))

        c.execute('SELECT * FROM guitarister;')

        for p in c:
            print('guitarist: {}'.format(p))

        c.execute('SELECT * FROM producenter;')

        for p in c:
            print('producent: {}'.format(p))

    elif inp == 'order':
        c = con.cursor()
        c.execute('SELECT * FROM guitarmodeller ORDER BY årstal;')

        for p in c:
            print('guitar: {}'.format(p))

    elif inp == 'ny':
        n = input('Indtast navn: ')
        a = input('Indtast producent: ')
        c = con.cursor()
        c.execute('INSERT INTO guitarmodeller (navn,producent) VALUES (?,?)', (n, a))
        con.commit()

    elif inp == 'mangetilmange':
        #Mange-til-mange relation samlet i "guitaristmodeller".
        c = con.cursor()
        #c.execute('SELECT g.navn, m.navn FROM guitarmodeller m INNER JOIN guitaristmodeller gm ON gm.model_id = m.id INNER JOIN guitarister g ON gm.guitarist_id = g.id WHERE g.id = 3')
        #c.execute('SELECT g.navn, m.navn, p.navn FROM guitaristmodeller gm INNER JOIN guitarmodeller m ON gm.model_id = m.id INNER JOIN guitarister g ON gm.guitarist_id = g.id INNER JOIN producenter p ON m.producent = p.id WHERE g.id = 3')
        c.execute("""SELECT g.navn, m.navn, p.navn FROM guitaristmodeller gm
      INNER JOIN guitarister g ON gm.guitarist_id = g.id
      INNER JOIN guitarmodeller m ON gm.model_id = m.id
      INNER JOIN producenter p ON m.producent = p.id
      WHERE g.id = 3;""")

        for p in c:
            print('guitarist: {}'.format(p))

    elif inp == 'entilmange':
        #En-til-mange relation med reference fra guitarmodeller.producent til producenter.id
        c = con.cursor()
        c.execute('SELECT gm.navn, p.navn, gm.årstal, p.lokation FROM guitarmodeller gm INNER JOIN producenter p ON gm.producent = p.id;')
        #Ækvivalent, med implicit join:
        #c.execute('SELECT guitarmodeller.navn, producenter.navn, guitarmodeller.årstal, producenter.lokation FROM guitarmodeller, producenter WHERE guitarmodeller.producent = producenter.id;')

        for p in c:
            print('modeller: {}'.format(p))
