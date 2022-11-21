import sqlite3
from sqlite3 import Error
import pandas as pd

#Connectie starten
def start() -> sqlite3.Connection:
    try:
        return sqlite3.connect("chinook.db")
    except Error as ex:
        print(ex)
def vraag1(db_con: sqlite3.Connection):
    #drie " om over meerdere lijnen te schrijven
    query = """
    SELECT t.Name as name, a.Title as album, ar.Name as Artist, g.Name as Genre, i.UnitPrice as price_unit, i.Quantity as Quantity
    FROM tracks t left outer join invoice_items i on i.Trackid = t.Trackid
    join genres g on t.Genreid = g.Genreid
    join albums a on t.Albumid = a.Albumid
    join artists ar on a.Artistid = ar.Artistid
    """
    tracks = pd.read_sql_query(query, db_con)
    print(tracks)
    print(f"Total records: {len(tracks)}")

    return tracks
def vraag2(tracks):
    print(tracks.head(10)) #Eerste 10 weergeven
    #not_sold = tracks.loc[tracks["Quantity"].isna(), ["Name", "Artist"]]
    #print(not_sold)

    #OPLOSSINGEN VAN DOCENT NOG NOTEREN

def vraag3(tracks):
    tracks["Total"] = tracks["UnitPrice"] * tracks["Quantity"]
    print(tracks)
    #error oplossen
def vraag4(db_con: sqlite3.Connection):
    pass
def vraag5(db_con: sqlite3.Connection):
    pass
if __name__ == '__main__':
    dbConnectie = start()
    pd.set_option("display.max_columns", None) #tonen alle cols
    pd.set_option("expand_frame_repr", False) #Naast elkaar te zetten, "toont mooier"

    tracks = vraag1(dbConnectie)
    #vraag2(tracks)
    #vraag3(tracks)

    print(dbConnectie)
    dbConnectie.close()
