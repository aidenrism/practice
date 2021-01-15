
url = ''
response = requests.get(url).text

data = BeautifulSoup(response, 'html.parser')

result = data.select_one(' ').text
print(result) 