from resources.Day9_Auctions.auctions_art import logo
import os

dictCountryCapitals = { "Germany": "Berlin", "Russia": "Moscow", "Spain": "Madrid"}
dictCountryCapitals["Italy"] = "Rome"   # Add or update dict
#dictCountryCapitals = {}   # empty the dictionary
for country in dictCountryCapitals:
    print(country + ", " + dictCountryCapitals[country])

lsTravelLog = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "noOfTimes": 3
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "noOfTimes": 2
    }
]
def addTravelLog(country, cities, noOfTimes):
    log = {"country": country, "cities_visited": cities, "noOfTimes": noOfTimes}
    lsTravelLog.append(log)
addTravelLog("Japan", ["Tokyo", "Hiroshima", "Yokohama", "Osaka"], 4)
for log in lsTravelLog:
    print(log)
print(f"I've been to {lsTravelLog[2]['country']}'s {lsTravelLog[2]['cities_visited'][1]} city where nuclear bomb was dropped.")
# lsOfCities = eval(input())  # create list from input: ["Sao Paulo", "Rio de Janeiro"]

# Auctions project
print(logo)
dictBidders = {}
bMoreBidders = "yes"
while(bMoreBidders):
    sName = input("Enter bidder's name: ")
    nBidAmount = int(input("Enter the bid amount: $"))
    dictBidders[sName] = nBidAmount
    sMoreBidders = input("Are there any other bidders?: ")
    bMoreBidders = True if sMoreBidders == "yes" else False
    if not bMoreBidders:
        nMaxBidAmount = 0
        sMaxBidderName = ""
        for name in dictBidders:
            if dictBidders[name] > nMaxBidAmount:
                nMaxBidAmount, sMaxBidderName = dictBidders[name], name
        print(f"Max bid of ${nMaxBidAmount} is done by {sMaxBidderName}")
    else:
        os.system('cls')