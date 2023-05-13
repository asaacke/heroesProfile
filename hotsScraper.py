#!/usr/bin/python3

#win rate, pop, ban rate, games played, wins, losses
import requests
from bs4 import BeautifulSoup
import sys

heroes = {"Abathur", "Alarak", "Alexstrasza", "Ana", "Anduin", "Anub'arak", "Artanis", "Arthas", "Auriel", "Azmodan",
          "Blaze", "Brightwing", "Cassia", "Chen", "Cho", "Chromie", "D.Va", "Deathwing", "Deckard", "Dehaka", "Diablo",
          "E.T.C.", "Falstad", "Fenix", "Garrosh", "Gazlowe", "Genji", "Greymane", "Gul'dan", "Hanzo", "Hogger", "Illidan",
          "Imperius", "Jaina", "Johanna", "Junkrat", "Kael'thas", "Kel'Thuzad", "Kerrigan", "Kharazim", "Leoric", "Li Li", 
          "Li-Ming", "Lt. Morales", "Lúcio", "Lunara", "Maiev", "Mal'Ganis", "Malfurion", "Malthael", "Medivh", "Mei",
          "Mephisto", "Muradin", "Murky", "Nazeebo", "Nova", "Orphea", "Probius", "Qhira", "Ragnaros", "Raynor", "Rehgar",
          "Rexxar", "Samuro", "Sgt. Hammer", "Sonya", "Stitches", "Stukov", "Sylvanas", "Tassadar", "The Butcher", "The Lost Vikings",
          "Thrall", "Tracer", "Tychus", "Tyrael", "Tyrande", "Uther", "Valeera", "Valla", "Varian", "Whitemane", "Xul", "Yrel",
          "Zagara", "Zarya", "Zeratul", "Zul'jin"}

def getSoup(url):
    page = requests.get(url)
    return BeautifulSoup(page.content, "html.parser")

    
#best heroes on this map
def getMapHeroRates(_map):
    _map.replace(" ", "_") 
    _map.replace("'", "%27")
    url = "https://heroesprofile.com/Global/Hero/?map=" + _map + "&mirror=Exclude"
    soup = getSoup(url)
    out = open("getMapHeroRatesOut", "w")
    out.write(soup)
        
    
def getHeroRateByMap(_hero):
    url = "https://heroesprofile.com/Global/Hero/Maps/?hero=" + _hero.capitalize()

    page = requests.get(url)

    parsed = BeautifulSoup(page.content, "html.parser")


    outputFile = open("parsed", "w")
    outputFile.write(str(parsed))
    
    results = parsed.find(id = "hero-stat-data")

    map_rates = dict()

    for c in results.children:
        s = c.get_text("<td>")
        l = s.split("<td>")
        
        #print(l)

        winRates = l[:2]

        print(winRates)
        
        #nums = l[1:]
        #map_name = l[0].lower()
        #map_name2 = l[0].lower().split()
        #map_initials = ""
        #for i in map_name2:
        #    map_initials += i[0]
        #    if(i != "of" and i != "the"):
        #        map_rates[i] = nums          
#
        #map_rates[map_name] = nums
        #map_rates[map_initials] = nums


    #print("get_hero_rate(): " + _map + ": " + str(map_rates[_map]))
    
    #return map_rates[_map]


def main():
    hero = sys.argv[1]
    #_map = sys.argv[2]
    #getHeroRateByMap(hero)
    getMapHeroRates("Towers of Doom")
    
        

if __name__ == "__main__":
    main()