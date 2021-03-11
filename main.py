import requests

TOKEN = 2619421814940190
heroes = ['Hulk', 'Captain America', 'Thanos']
url = "https://superheroapi.com/api/2619421814940190/search"


def find_smartest():
    stats = {}
    for hero in heroes:
        stats[hero] = int(requests.get(url+'/'+hero).json()['results'][0]['powerstats']['intelligence'])
    print(f'Smartest is {max(stats, key=stats.get)} with {max(stats.values())} int')



find_smartest()