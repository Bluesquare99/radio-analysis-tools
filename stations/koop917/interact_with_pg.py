import psycopg2
from dateparser import parse

print(parse('Saturday', settings={'PREFER_DATES_FROM': 'past'}).strftime('%m %d %Y'))
print(parse('Saturday').strftime('%m %d %Y'))

def write_to_pg():
  pass
