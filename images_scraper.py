import requests
from bs4 import BeautifulSoup
import os

def imagedown(url, folder):
    num = 1
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder))
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')
    for image in images:
        name = image['alt']
        link = image['src']
        with open(name.replace(str(name), str(num)).replace('/', '') + '.jpg', 'wb') as f:  #when file name is too long
        # with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print('Downloading : ', name)
            num += 1

url = input('Enter URL: ')
imagedown(url, '/home/marco/Assignment_2/images_input')