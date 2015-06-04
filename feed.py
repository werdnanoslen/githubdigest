import feedparser
import requests
import urllib
from datetime import datetime
from twitter import *

feed = feedparser.parse('https://github.com/werdnanoslen.atom')
bitlyToken = ''
bitlyApi = 'https://api-ssl.bitly.com/v3/shorten?access_token=' + bitlyToken + '&longUrl='

dateformat = '%Y-%m-%dT%H:%M:%S'
now = datetime.strptime(datetime.utcnow().strftime(dateformat), dateformat)
eventsYesterday = []

for i in range(len(feed.entries)):
    entry = feed.entries[i]
    then = datetime.strptime(entry.published.replace('Z', ''), dateformat)
    daysSince = (now - then).days
    if daysSince == 0:
        bitlyResponse = requests.get(bitlyApi + entry.link).json()
        if bitlyResponse['status_txt'] == "OK":
            entryTitle = entry.title.replace('werdnanoslen ', '')
            bitlyLink = bitlyResponse['data']['url'].replace('http://', '')
            event = entryTitle + ' ' + bitlyLink
            eventsYesterday.append(event)
        else:
            print('bitly api error: ' + bitlyResponse.status_txt)
    else:
        break

numEventsYesterday = len(eventsYesterday)
tweetContent = ''
if numEventsYesterday == 1:
    tweetContent = eventsYesterday
elif numEventsYesterday > 1:
    tweetContent = eventsYesterday

print(tweetContent)
