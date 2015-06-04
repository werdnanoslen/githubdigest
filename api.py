import requests
from datetime import datetime

events = requests.get('https://api.github.com/users/werdnanoslen/events').json()

eventsYesterday = {}

dateformat = '%Y-%m-%dT%H:%M:%S'
now = datetime.strptime(datetime.utcnow().strftime(dateformat), dateformat)

for i in range(len(events)):
    event = events[i]
    then = datetime.strptime(event['created_at'].replace('Z', ''), dateformat)
    daysSince = (now - then).days
    if daysSince == 0:
        eventsYesterday.update(event)
    else:
        break

print(eventsYesterday)
