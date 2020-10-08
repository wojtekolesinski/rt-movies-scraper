import requests
from bs4 import BeautifulSoup
from random import choices
from time import sleep




site = requests.get('https://editorial.rottentomatoes.com/guide/essential-movies-to-watch-now/')
site2 = requests.get('https://editorial.rottentomatoes.com/guide/essential-movies-to-watch-now/2/')
soup = BeautifulSoup(site.content, 'html.parser')
soup2 = BeautifulSoup(site2.content, 'html.parser')
movies = soup.find_all('div', 'article_movie_title')
movies += soup2.find_all('div', 'article_movie_title')

for counter, movie in enumerate(movies, start=1):

    title = movie.get_text().strip()
    link = movie.div.h2.a['href']
    movie_site = requests.get(link)
    movie_soup = BeautifulSoup(movie_site.content, 'html.parser')
    tag_list = movie_soup.find('ul', 'content-meta info')
    my_dict = {label.string.strip(' :'): value.get_text().strip().replace('\n', '') for label, value in zip(tag_list.find_all('div', 'meta-label subtle'), tag_list.find_all('div', 'meta-value'))}

    for key in ['Genre', 'Written By', 'Directed By']:
        if key in my_dict:
            my_dict[key] = ' '.join(my_dict[key].replace(',', ' ').split())

    print(f'''{counter}. {title}''')
    for key, value in my_dict.items():
        print(f'{key}: {value}')
    print('\n\n')



whattodo = input()
while True:
    if whattodo:
        break
    print('Generating 3 random titles')
    print('...')
    sleep(2)
    for movie in choices(movies, k=3):
        print(movie.get_text().strip())
    whattodo = input()
