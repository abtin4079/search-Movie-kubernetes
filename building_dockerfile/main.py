from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import redis
import uvicorn 
from insert_elastic import elasticSearch
from api import api
from dotenv import load_dotenv
import os

app = FastAPI(title= "film recommender")

# Load the enviorment variable 
load_dotenv()



# import the enviorment varible for connecting to elasticsearch
elasticsearch_host = os.environ.get('ELASTICSEARCH_SERVICE_SERVICE_HOST')
elasticsearch_port = os.environ.get('ELASTICSEARCH_SERVICE_SERVICE_PORT')
elastic_url = 'http://' + elasticsearch_host + ":" + str(elasticsearch_port)

# import the enviorment varible for connecting to redis
redis_host = os.environ.get('REDIS_SERVICE_SERVICE_HOST')
redis_port = os.environ.get('REDIS_SERVICE_SERVICE_PORT')


print(elasticsearch_host)
print(elasticsearch_port)
print(redis_host)
print(redis_port)

# Connect to Redis
redis_client = redis.StrictRedis(host= redis_host, port= redis_port, db=0, decode_responses=True)





class SearchRequest(BaseModel):
    query: str

@app.on_event("startup")
async def startup():
    pass


@app.on_event("shutdown")
async def shutdown():
    pass

@app.get('/')
async def up():
    return f"Hey!"


@app.post("/search/")
async def search(search_request: SearchRequest):
    try:

        # Send search query to Redis
        print(search_request.query)
        response_body = redis_client.get(search_request.query)
        print(response_body)
        if response_body is not None:
            print("Response body found in Redis: ", response_body)
            return 0
        else:
            print("We don't find any matching film name in redis! ")


        # search through the elastic
        released_year = elasticSearch(search_request.query, elastic_url)
        if (released_year != "invalid"):
            redis_client.set( search_request.query, released_year)
            print("We successfully set these film name from elastic with its released year: ", released_year)
            return 0
        else:
            print("We don't find any matching film name in elasticsearch! ")

        #search through the api
        api_year = api(search_request.query)
        if(api_year != "invalid"):
            redis_client.set( search_request.query, api_year)
            print("We successfully set this film name and its released year from api: ", api_year)
            return 0
        else:
            print("there is no matching film in this API! ")
            return 0

    except Exception as e:
        # Log the exception or handle it as needed
        return {"error": str(e)}








if __name__ == '__main__':
    uvicorn.run("main:app", host='localhost', port=7000, reload=True)