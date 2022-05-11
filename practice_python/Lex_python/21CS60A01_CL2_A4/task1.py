# Agnik Saha
# Roll: 21CS60A01
# Assignment 4 task 1

#importing modules
import os
import requests

headers = {

        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'

    }

inputFileName = "worldometers_countrylist.txt"


main_url = "https://www.worldometers.info/coronavirus/"
response = requests.get(main_url, headers=headers)
page_content = response.text

if not os.path.exists("./COUNTRIES"): 
    os.mkdir("./COUNTRIES")

file_name = "./COUNTRIES/world.html"
f = open(file_name, 'w',encoding='utf-8')
f.write(page_content)
f.close()


with open(inputFileName) as f:
    lines = [ line.strip('\n').lower().replace(' ', '-') for line in list(f) ]


'''
here lines is the list of the each line of the text file.

['europe:',
 '--------',
 'france',
 'uk',
 'russia',
 'italy',
 'germany',....................]

'''

a = lines
b = ["--------","--------","--------","--------", "","europe:", "---------","north-america:","asia","south-america","africa","oceania"]

# country_list is the list of all the countries containing in the text file
country_list = [x for x in a if (x not in b)]

# urls is the list of all the urls of each country in the worldometers website
urls = []
for coun in country_list:
    url ="https://www.worldometers.info/coronavirus/country/{name}/".format(name =  coun)
    urls.append(url)


# saving the html file of each country in the "COUNTRIES" folder
if not os.path.exists("./COUNTRIES"): 
    os.mkdir("./COUNTRIES")

for i in range(0,len(urls)):
    print(f'Fetching web page: {urls[i]}')
    try:
        response = requests.get(url=urls[i], headers=headers)
        page_content = response.text
    except Exception as e:
        print(e)
        continue
    mov_name = "./COUNTRIES/" + country_list[i] + ".html"
    f = open(mov_name, 'w')
    f.write(page_content)
    f.close()