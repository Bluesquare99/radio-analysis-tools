# Linked to https://app.airplane.dev/t/kutx_98_9_scrape [do not edit this line]

# Put the main logic of the task in the main function.
def main(params):
    response = requests.get('https://api.composer.nprstations.org/v1/widget/50ef24ebe1c8a1369593d032/day', headers=headers, params=params)
  
    soup = bs4(response.text,'lxml')
    print(soup)
    p_tags = soup.select('body p')[0]

    # print(p_tags.contents[0].string[0:2000])
    split_by_curly = p_tags.contents[0].string.split('{')


    date = []

    songs = {
        'date': {
            '00':[],
            '01':[],
            '02':[],
            '03':[],
            '04':[],
            '05':[],
            '06':[],
            '07':[],
            '08':[],
            '09':[],
            '10':[],
            '11':[],
            '12':[],
            '13':[],
            '14':[],
            '15':[],
            '16':[],
            '17':[],
            '18':[],
            '19':[],
            '20':[],
            '21':[],
            '22':[],
            '23':[]
            }
        }

    for x in split_by_curly:
        if 'trackName' in x and not 'itunes' in x:
        split_by_comma = x.split(',')
        # print(split_by_comma)

        hour = ''
        track = ''
        artist = ''

        for i in split_by_comma:
            if 'start_time' in i:
            hour = i.split(' ')[1][0:2]
            if 'trackName' in i:
            track = i.split(':')[1].strip('"')
            if 'artistName' in i:
            artist = i.split(':')[1].strip('"')
            

        songs['date'][str(hour)].append([track, artist])  
        # print(f'{hour}, {track}, {artist}')

    # print(songs['date'])
    print(songs['date'])
    return 

    # You can return data to show outputs to users.
    # Outputs documentation: https://docs.airplane.dev/tasks/outputs
    return [
        {"songs": songs['date']}
    ]
