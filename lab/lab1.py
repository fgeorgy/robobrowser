import re
from requests import Session
from robobrowser import RoboBrowser

session = Session()
session.verify = False  # Skip SSL verification
session.proxies = {'http': 'http://localhost:8081/'}
browser = RoboBrowser(session=session, parser='lxml')

# Browse to Genius
# browser = RoboBrowser(history=True)
browser.open('http://www.petitesannonces.ch/')

# Search for Porcupine Tree
form = browser.get_form(action='/recherche/')
form                # <RoboForm q=>
form['q'].value = 'jardinage'
browser.submit_form(form)

# Look up the first song
songs = browser.select('.ele a.title')

for p in songs:
    print(p.text)

# browser.follow_link(songs[0])
# lyrics = browser.select('.lyrics')
# lyrics[0].text      # \nHear the sound of music ...
#
# # Back to results page
# browser.back()
#
# # Look up my favorite song
# song_link = browser.get_link('trains')
# browser.follow_link(song_link)
#
# # Can also search HTML using regex patterns
# lyrics = browser.find(class_=re.compile(r'\blyrics\b'))
# lyrics.text         # \nTrain set and match spied under the blind...
