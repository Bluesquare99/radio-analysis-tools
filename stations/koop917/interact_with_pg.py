import psycopg2
import os
from dotenv import load_dotenv
import uuid


# DATABASE_URL = os.environ['DATABASE_URL']

def write_to_pg(song_entry):
  load_dotenv()
  con = psycopg2.connect(
    host=os.environ['HOST'], 
    database=os.environ['DATABASE'], 
    user=os.environ['USER'], 
    password=os.environ['PASSWORD'],
    sslmode='require')
  cur = con.cursor()
    # Defining insert statement
  sql_insert_query = """ INSERT INTO playlists (playlist_song_id, station, show, date, artist, track) VALUES (%s, %s, %s, %s, %s, %s) """
  tuple = (uuid.uuid4().hex, song_entry['station'], song_entry['show'], song_entry['date'], song_entry['artist'], song_entry['track'])
  cur.execute(sql_insert_query, tuple)
  con.commit()
  cur.close()


