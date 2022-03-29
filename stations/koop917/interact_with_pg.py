import psycopg2
import os
from dotenv import load_dotenv
import uuid




def write_to_pg(song_entry):
  load_dotenv()
  DATABASE_URL = os.environ['DATABASE_URL']
  con = psycopg2.connect(DATABASE_URL, sslmode='require')
  cur = con.cursor()
    # Defining insert statement
  sql_insert_query = """ INSERT INTO playlists (playlist_song_id, station, show, date, artist, track) VALUES (%s, %s, %s, %s, %s, %s) """
  tuple = (uuid.uuid4().hex, song_entry['station'], song_entry['show'], song_entry['date'], song_entry['artist'], song_entry['track'])
  cur.execute(sql_insert_query, tuple)
  con.commit()
  cur.close()


