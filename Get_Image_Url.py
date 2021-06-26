from requests import get
from json import loads
from random import choice


def get_image_url(url):
    image_page = get(url)
    page_html = ''
    image_links = []
    object = 'file_url="'
    for i in image_page:
        page_html += str(i)
    del(image_page)
    page_html = page_html.replace("'b'", '')
    while object in page_html:
        page_html = page_html[page_html.find(object)+len(object):]
        image_links += [page_html[:page_html.find('"')]]
    image_url = choice(image_links)
    while 'mp4' in image_url:
        image_url = choice(image_links)
    return image_url


def get_gif_url(term='', prefix='anime'):
    gif_url = []
    key = '3OOAW6J5MRV8'
    gif_image= get(f'https://g.tenor.com/v1/search?q=%{prefix} {term}&key=%{key}')
    gif_image = str(loads(gif_image.content))
    while "'gif'" in gif_image:
        gif_image = gif_image[gif_image.find("'gif'"):]
        start = gif_image.find("'url': '")+len("'url': '")
        gif_image = gif_image[start:]
        gif_url += [gif_image[:gif_image.find("'")]]
    image_url = choice(gif_url)
    del(gif_url)
    return image_url
