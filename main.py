import requests

headers = {
    'authorization':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NDM3Nzk1ODIsInByaW5jaXBhbCI6eyJpZCI6Mjc2NDA1NzA2NTkwMjA0OTEwNSwibmFtZSI6IkNDMiIsImVtYWlsX2FkZHJlc3MiOiJlbmdpbmVlcmluZysyMDIyMDIwMUByZXZlYWxtb2JpbGUuY29tIiwib3JnYW5pemF0aW9uIjoyMTg1MjkxNzQ3NTc4MzQ4ODMxLCJhZG1pbmlzdHJhdG9yIjpmYWxzZSwicm9sZSI6IkNvbnRyaWJ1dG9yIn19.DtzbDnciP_CDU9vJYvCWEjat6c_dJSHaK_fRIXiSjos',
}

params = (
    ('format', 'json'),
)

def main():

  response = requests.get('https://gateway-service.revealmobile.com/report/campaign/3544/conversion/daily', headers=headers, params=params)
  res = response.json()
  rows = res['data']['rows']
  total_conversions = 0
  total_conversions_primary = 0
  total_conversions_household = 0
  unique_dates = set()

  for row in rows:
    conversions = row['metrics']['Conversion Count']
    total_conversions += conversions
    if 'primary' in row['dimensions']['Device Type']:
        total_conversions_primary += conversions
    elif 'household' in row['dimensions']['Device Type']:
        total_conversions_household += conversions
    unique_dates.add(row['dimensions']['Date']

  # print(total_conversions)
  # print(total_conversions_primary)
  # print(total_conversions_household)
  # print(unique_dates)

if __name__ == "__main__":
    main()

