import psycopg2
from dateparser import parse
import os
import time
import uuid
from datetime import datetime
from dotenv import load_dotenv

def pg(song):
	con = psycopg2.connect('postgres://hnewxezrserycc:fa7730d9660660f7dc0292e1282e327c0a93ff49d062cf25f270d30bc27747e3@ec2-3-209-61-239.compute-1.amazonaws.com:5432/d26q7d7nbt04qe')
	cur = con.cursor()
	insert_query = """ INSERT INTO playlists (playlist_song_id, station, show, date, artist, track) VALUES (%s, %s, %s, %s, %s, %s); """
	insert_tuple = (uuid.uuid4().hex), str(song["station"]), str(song["show"]), song["date"], str(song["artist"]), str(song["track"])
	cur.execute(insert_query, insert_tuple)
	con.commit()
	cur.close()
