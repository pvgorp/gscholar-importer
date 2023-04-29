from scholarly import scholarly
import csv
from bs4 import BeautifulSoup
import requests     
## enable the following line for use with ipython3 debugging (see https://hasil-sharma.github.io/2017-05-13-python-ipdb/)
#import ipdb; ipdb.set_trace()
from random import randint
from time import sleep

# This function caches scholarly data to out.csv (e.g., citations, URL), for further procesing by custom code
def inToOut():
    outFieldnames = ['First name', 'Last name', 'affiliation', 'citations', 'scholar_page','url_pic']
    with open('out.csv', 'w', newline='') as outCsvfile:
        outWriter = csv.DictWriter(outCsvfile, fieldnames=outFieldnames)   
        outWriter.writeheader()
        with open('in.csv', newline='') as csvfile:
            csvreader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
            for row in csvreader:
                # print(', '.join(row))
                print(row)
                firstName= row['First name']
                lastName= row['Last name']
                affiliation= row[ 'Affiliation']                        

                scholEntry= next(scholarly.search_author( "%s %s, %s" % (firstName, lastName, affiliation)), None)
                if scholEntry is None: 
                    print("Error: %s %s, %s not found!"%(firstName, lastName, affiliation))
                else:
                    #process the publication
                    print(scholEntry)
                    citations= scholEntry['citedby']
                    url_pic= scholEntry['url_picture']
                    scholarPage= "https://scholar.google.com/citations?user="+scholEntry['scholar_id']
                    #print("%s %s, %s" % (firstName, lastName, affiliation))
                    outWriter.writerow({'First name': firstName, 'Last name': lastName, 'affiliation': affiliation, 'citations': citations, 'scholar_page': scholarPage, 'url_pic': url_pic})
         
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}

# this function for the getting inforamtion of the web page
def get_author_info(author_url):

  #download the page
  response=requests.get(author_url,headers=headers)

  # check successful response
  if response.status_code != 200:
    print('Status code:', response.status_code)
    raise Exception('Failed to fetch web page ')

  #parse using beautiful soup
  paper_doc = BeautifulSoup(response.text,'html.parser')
  return paper_doc


#### MAIN HERE

inToOut()
with open('out.csv', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        outFieldnames = ['First name', 'Last name', 'affiliation', 'citations', 'scholar_page','url_pic','citationsAll','citations5Y','hIndexAll','hIndex5Y','keywords']
        with open('out-h-index.csv', 'w', newline='') as outCsvfile:
            outWriter = csv.DictWriter(outCsvfile, fieldnames=outFieldnames)   
            outWriter.writeheader()

            for row in csvreader:
                print(row)
                firstName= row['First name']
                lastName= row['Last name']
                citations= row['citations']
                scholarPage= row['scholar_page']
                affiliation= row['affiliation']
                url_pic= row['url_pic']
                
                doc= get_author_info(scholarPage)
                print("Analyzing "+firstName+" "+lastName);

                citationsAll= doc.find_all("td", class_="gsc_rsb_std")[0].text
                citations5Y= doc.find_all("td", class_="gsc_rsb_std")[1].text
                hIndexAll= doc.find_all("td", class_="gsc_rsb_std")[2].text
                hIndex5Y= doc.find_all("td", class_="gsc_rsb_std")[3].text
                keywords= doc.find_all("a", class_="gsc_prf_inta gs_ibl")
                kw=""
                for a in doc.find_all("a", class_="gsc_prf_inta gs_ibl"):
                    kw=kw+a.text+";"
                print("keywords: "+kw)
      
                outWriter.writerow({'First name': firstName, 'Last name': lastName, 'affiliation': affiliation, 'citations': citations, 'scholar_page': scholarPage, 'url_pic': url_pic,
                    'citationsAll':citationsAll,'citations5Y':citations5Y,'hIndexAll':hIndexAll,'hIndex5Y':hIndex5Y,'keywords':kw})
                sleep(randint(1,3))

