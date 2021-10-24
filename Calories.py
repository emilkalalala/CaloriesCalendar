import requests

api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
query = 'pizza'
response = requests.get(api_url + query, headers={'X-Api-Key': '+K83QUc3yx5viW1/jBEWqw==YJ6E1gKifoWb4kZn'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)



