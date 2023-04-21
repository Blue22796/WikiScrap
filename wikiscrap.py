import requests
import bs4

def search(target):
	page = requests.get('https://en.wikipedia.org/wiki/'+target)
	soup = bs4.BeautifulSoup(page.content,'html.parser')
	links = [link['href'] for link in soup.find_all('a',href=True) if link['href'][:5]=='https']
	text = [p.text for p in soup.find_all('p')]
	return text,links

target = input('What would you like to look up? (Use_This_Format)\n')
text, links = search(target)
for i in range(len(text)):
	print(text[i])
	if i%5==0:
		input("Press ENTER to continue")
cont = input("View external links?\ny/n\n")
if cont=='y' or cont=='\n':
	print("\n\n\nExtenral links:\n")
	for i in range(len(links)):
		print(links[i])
		if i%10==0:
			input("Press ENTER to continue")
else:
	print(cont)

input('Press ENTER to exit')