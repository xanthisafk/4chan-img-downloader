import bs4 as bs
import urllib
import requests
import os

def get_links(url):

	print("Retrieving data...")

	page = requests.get(url)

	soup = bs.BeautifulSoup(page.content, "html.parser")

	results = soup.find_all(class_="fileText")

	links = []

	for i in results:
		k = i.find("a")
		links.append(('https://' + k['href'][2:]))

	return links


def save_links(links):

	print("Saving links...")

	txt = ''
	for i in links:
		txt += i + "\n"

	with open('links.txt', 'w+') as f:
		f.write(txt)

	print("File saved as `links.txt`")

def download(links):

	if not os.path.exists('img'):
		print("Creating `img` folder")
		os.makedirs('img')

	print("Starting download")
	for url in links:
		link = url.split('/')
		path = 'img/'+ link[len(link)-1]
		urllib.request.urlretrieve(url, path)
		print("Saved file:", path, "from:", url)

def main():
	url = input("URL of 4chan thread: ")
	save_ = True if input("Save links? (overwrites `links.txt` if exists): ") in ['y', 'yes', 'true'] else False

	links = get_links(url)

	if save_:
		save_links(links)

	download(links)

	print("Done!")

if __name__ == '__main__':
	main()