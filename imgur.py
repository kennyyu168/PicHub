from imgurpython import ImgurClient
import webbrowser
import os
import json
import requests

client_id = 'df4cc21b8273314'
client_secret = 'ae0d06b7ade1d60d1ea6fe68481fb8df319bf821'
# get token
# https://api.imgur.com/oauth2/authorize?client_id=df4cc21b8273314&response_type=token
token = 'ff8e2a90474a36962377f9013bdbd3619f8601fe'

client = ImgurClient(client_id, client_secret)

username = "username4pichub"

"""
    # Authorization flow, pin example (see docs for other auth types)
    authorization_url = client.get_auth_url('code')

    # ... redirect user to `authorization_url`, obtain pin (or code or token) ...

    credentials = client.authorize('PIN OBTAINED FROM AUTHORIZATION', 'code')
    client.set_user_auth(credentials['access_token'], credentials['refresh_token'])
"""

def get_links():
    items = client.gallery()
    for item in items:
        print(item.link)

def get_token():
    url = 'https://api.imgur.com/oauth2/authorize?client_id=df4cc21b8273314&response_type=token'
    token_url = requests.get(url)
    print(token_url.url)

def get_images(username):
    # removes all .txt files
    init_command = 'rm *.txt'
    os.system(init_command)
    # get list of most recent pictures from imgur account
    command = 'curl --location --request GET "https://api.imgur.com/3/account/username4pichub/images/" \--header "Authorization: Bearer ff8e2a90474a36962377f9013bdbd3619f8601fe" >> img_data.txt'
    os.system(command)
    # parses the file to only get the url to the pictures
    links = []
    with open('img_data.txt', 'r') as f:
        data = f.read()
        data = "\n".join(data.split(","))
    with open('img_data.txt', 'w') as f:
        f.write(data)
    with open('img_data.txt', 'r') as f:
        for line in f:
            if ("link" in line):
                line = line.replace('"', '')
                line = line.replace('link:', '')
                line = line.replace('}', '')
                line = line.replace(']', '')
                line = line.replace("\/", "/")
                line = line.replace('\n', '')
                links.append(line)
    f.close()
    # downloads the images to /imgur folder
    counter = 1
    for link in links:
        response = requests.get(link)
        if response.status_code == 200:
		if counter != 10:
			path = "/Users/kenny/Desktop/PicHub/imgur/0" + str(counter) + ".jpg"
		else
			path = "/Users/kenny/Desktop/PicHub/imgur/" + str(counter) + ".jpg"
            with open(path, 'wb') as img:
                img.write(response.content)
            counter+=1
    print("DONE")

def get_account(username):
    command = 'curl --location --request GET "https://api.imgur.com/3/account/' + username + '" \--header "Authorization: Client-ID df4cc21b8273314" >> imgur_account.json'
    os.system(command)
