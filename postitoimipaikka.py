import urllib.request
import json

def hae_postinumerot():
    # https://docs.python.org/3/howto/urllib2.html
    with urllib.request.urlopen('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as response:
        # https://docs.python.org/3/library/json.html
        return json.loads(response.read())

def main():
    postinumerot = hae_postinumerot()

    postinumero = input('Kirjoita postinumero: ').strip()

    if postinumero in postinumerot:
        postitoimipaikka = postinumerot[postinumero]
        print(postitoimipaikka.title())
    else:
        print('Postitoimipaikkaa ei löytynyt :(')

# main-funktio suoritetaan vain, jos tämä moduuli on "pääohjelma"
if __name__ == '__main__':
    main()