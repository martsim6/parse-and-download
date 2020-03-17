from bs4 import BeautifulSoup as bs
import requests
import json
import re
from pprint import pprint
from os.path import basename
from cairosvg import svg2png

if __name__ == "__main__":
	url = 'https://gloria.tv/post/rgMiMjcAogMi222cEvsCzC6Uq?fbclid=IwAR1m3fbv9WDA72P80vk7UieWA-SFVBUFsVnsdblXfWk1ssPjaIGvC84NL9k'

	page = requests.get(url)
	soup = bs(page.content, 'html.parser')
	whole_data = soup.find_all('div', class_='book')
	data_needed = ""

	for pages in whole_data:
		data_needed = pages.get('data-book')

	data_json = json.loads(data_needed)
	# pprint(data_json)
	all_pages = []
	
	for page in data_json['pages']:
		all_pages.append(page['url'])

	for index, page in enumerate(all_pages):
		cutted_page_url = re.sub("\'", "", page)
		print('Spracuvavam {} z {} obrazkov'.format(index, len(all_pages)))
		svg_file = requests.get(cutted_page_url).content
		svg_file = svg_file.decode('utf8')
		svg2png(bytestring=svg_file, write_to="./book/pic{}.png".format(index))