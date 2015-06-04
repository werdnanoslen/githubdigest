import feedparser
from datetime import datetime

feed = feedparser.parse('https://github.com/werdnanoslen.atom')

dateformat = '%Y-%m-%dT%H:%M:%S'
now = datetime.strptime(datetime.utcnow().strftime(dateformat), dateformat)
eventsYesterday = []

for i in range(len(feed.entries)):
    entry = feed.entries[i]
    then = datetime.strptime(entry.published.replace('Z', ''), dateformat)
    daysSince = (now - then).days
    if daysSince == 0:
        eventsYesterday.append(entry.title)
    else:
        break

numEventsYesterday = len(eventsYesterday)
if numEventsYesterday == 1:
    print('I did a thing')
elif numEventsYesterday > 1:
    print('I did some things')
