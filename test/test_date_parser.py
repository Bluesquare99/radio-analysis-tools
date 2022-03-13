import psycopg2
from dateparser import parse

print(parse('Sunday', settings={'PREFER_DATES_FROM': 'past'}).strftime('%m %d %Y'))
print(parse('Sunday'))
print(parse('Today'))
