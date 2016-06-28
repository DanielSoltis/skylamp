#to fix - when you load with a different url, gets the same images as from the previous page

from bottle import get, post, run, static_file, route, template
import sys
from PIL import Image
import math
import json
import requests
from StringIO import StringIO

def scrape(username, items=[]):
    url = 'http://instagram.com/' + username + '/media'
    media = json.loads(requests.get(url).text)
    items.extend(media['items'])
    return items

def parseURLs(username, maxItems):
    items = scrape(username)
    urls = []

    for index,item in enumerate(items):
        if index < maxItems:
            item['url'] = item[item['type'] + 's']['standard_resolution']['url'].split('?')[0]
            suffix = item['url'].split('/')[-1].split('?')[0].split('.')[1]
            if suffix == "jpg":
                urls.append(item['url'] )
    return urls

def parseValues(urls):
    values = []
    
    for url in urls:
        response = requests.get(url)
        im = Image.open(StringIO(response.content))

        im.thumbnail((320,240))
        pixel_values = list(im.getdata())

        avgR = 0
        avgG = 0
        avgB = 0
        totalPixels = len(pixel_values)

        for value in pixel_values:
            RGB = value
            avgR += RGB[0]
            avgG += RGB[1]
            avgB += RGB[2]

        avgR/=totalPixels
        avgG/=totalPixels
        avgB/=totalPixels
        value = str(avgR) + ", " + str(avgG) + ", " + str(avgB)
        values.append(value)
        
    return values

def pageContents(urls, values):
    zipped = zip(urls, values)
    page = template('colors', zipped = zipped)
    return page

@route('/instacolor/<username>')
def instacolor(username):
    #bottle.TEMPLATES.clear()
    name = template("{{username}}", username = username)
    urls = parseURLs(name,20)
    values = parseValues(urls)
    page = pageContents(urls,values)
    return page

@route('/avgcolor/<username>')
def avgcolor(username):
    #bottle.TEMPLATES.clear()
    urls = parseURLs(username,3)
    values = parseValues(urls)
    returnedValues = ""
    for value in values:
        returnedValues = returnedValues + value + '\r'
    return returnedValues

run(host='localhost', port=8080)

