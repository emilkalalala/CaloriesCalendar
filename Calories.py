import requests

api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
query = 'pdksjnk'
response = requests.get(api_url + query, headers={'X-Api-Key': '+K83QUc3yx5viW1/jBEWqw==YJ6E1gKifoWb4kZn'})
if response.status_code == requests.codes.ok:
    try:
        print(response.json()["items"][0]["calories"])
    except:
        print ("wrond ")
else:
    print("Error:", response.status_code, response.text)



