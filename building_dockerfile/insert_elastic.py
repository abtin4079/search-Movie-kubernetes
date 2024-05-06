from elasticsearch import Elasticsearch
from api import api

def elasticSearch(movie_name, URL):
    # Create an Elasticsearch client instance
    es = Elasticsearch([URL])  
    print(es)
    # Define the search query
    search_query = {
        "query": {
            "match": {
                "Series_Title": movie_name  # Example search term
            }
        }
    }

    # Perform the search
    search_results = es.search(index="movie", body=search_query)

    # Check if there are any search results
    if search_results['hits']['total']['value'] > 0:
        # Save the Poster_Link of the first document
        poster_link = search_results['hits']['hits'][0]['_source']['Released_Year']
        print("Poster Link:", poster_link)
        return poster_link
    else:
        print("No documents found matching the search criteria.")
        return "invalid"

def ssss():
    host = '162.2.20.5'
    port = 1235
    url = 'http://' + host + ":" + str(port)
    print(url)

if (__name__ == '__main__'):
    ssss()