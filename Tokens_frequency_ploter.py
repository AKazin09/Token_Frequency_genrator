import urllib.request
from bs4 import BeautifulSoup
import nltk
nltk.download('stopwords') 
from nltk.corpus import stopwords
 
response = urllib.request.urlopen("https://en.wikipedia.org/wiki/Tesla")
html = response.read()

soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip = True)

tokens = [t for t in text.split()]
sr = stopwords.words("english")
clean_tokens = tokens[:]

for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)

freq = nltk.FreqDist(clean_tokens)
for key, val in freq.items():
    print(str(key) + ':' + str(val))
freq.plot(10, cumulative = False)


