import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import bs4 as bs

url = 'http://vizier.u-strasbg.fr/viz-bin/votable/-A?-out.all&-source=I%2F337%2Fgaia&'

fonte = requests.get(url).content
soup = bs.BeautifulSoup(fonte, 'lxml')
print(soup.prettify())

