import requests


def api(movie_name):
    url = f"https://imdb-movies-web-series-etc-search.p.rapidapi.com/{movie_name}.json"

    headers = {
        "X-RapidAPI-Key": "0e566a50abmshcbb2f7203fd11b5p14de52jsn691d435af501",
        "X-RapidAPI-Host": "imdb-movies-web-series-etc-search.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    #print(response.status_code)
    if (response.status_code == 404):
        print("there is no valid film with your request!")
        return "invalid"

    if (response.status_code == 200):  
        api_url = response.json()['d'][0]['y']
        print(api_url)
        return api_url

if __name__ == "__main__":
    api("suits")
