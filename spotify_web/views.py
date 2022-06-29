from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import savify

spotify_secret_data = {'CLIENT_ID': 'c5739c2b9f3949d7ada667c549671810', 'CLIENT_SECRET': '3d6ad9b8286b49bd9ea3f11b6ede08b0'}


@csrf_exempt
def search(request):
    global spotify_secret_data
    if request.method == 'GET':
        return render(request, 'spotify_web/search.html')
    elif request.method == 'POST':
        print(target_song := request.POST.get('song'))
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=spotify_secret_data["CLIENT_ID"], client_secret=spotify_secret_data["CLIENT_SECRET"]))

        results = sp.search(q=target_song, limit=20)

        songs_list = enumerate(results['tracks']['items'])

        return render(request, 'spotify_web/search.html', context={'songs_list': songs_list})


def download(requests, type, id):
    global spotify_secret_data
    s = savify.Savify(api_credentials=(spotify_secret_data["CLIENT_ID"], spotify_secret_data["CLIENT_SECRET"]))
    # Spotify URL
    print(URL1 := f"https://open.spotify.com/{type}/{id}")
    URL2 = 'https://open.spotify.com/track/2MLHyLy5z5l5YRp7momlgw'
    try:
        x=s.download(URL1)
        print(x)
    except:
        x=s.download(URL2)
        print(x)
    return HttpResponse('ok')
