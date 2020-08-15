from SPARQLWrapper import SPARQLWrapper, JSON


def download_wiki(title):
    pass


sparql = SPARQLWrapper("https://query.wikidata.org/sparql")


def download_wikidata_by_title(title):
    sparql.setQuery('''
    SELECT distinct ?item ?itemLabel ?itemDescription WHERE{  
      ?item ?label "%s"@vi.  
      ?article schema:about ?item .
      ?article schema:name "%s"@vi .
      ?article schema:inLanguage "vi" .
      ?article schema:isPartOf <https://vi.wikipedia.org/>.	
      SERVICE wikibase:label { bd:serviceParam wikibase:language "vi". }    
    }
    ''' % (title, title))
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    print(results)


title = 'Hà Nội'
download_wiki(title)

download_wikidata_by_title(title)
