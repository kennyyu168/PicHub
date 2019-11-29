from imgurpython import ImgurClient
import webbrowser, os, requests, shutil

client_id = 'df4cc21b8273314'
client_secret = '22711de5d4a1e798c2af674f0f036de70a44e881'
# get token
# https://api.imgur.com/oauth2/authorize?client_id=df4cc21b8273314&response_type=token
token = '8fbe3dad26282f0849cca4cb07bfae70289faa71'

client = ImgurClient(client_id, client_secret)

username = "username4pichub"

"""
    # Authorization flow, pin example (see docs for other auth types)
    authorization_url = client.get_auth_url('code')

    # ... redirect user to `authorization_url`, obtain pin (or code or token) ...

    credentials = client.authorize('PIN OBTAINED FROM AUTHORIZATION', 'code')
    client.set_user_auth(credentials['access_token'], credentials['refresh_token'])
"""

def authorize():
    auth_url = client.get_auth_url('token')
    webbrowser.open(auth_url, new=2, autoraise=True)

def get_links():
    items = client.gallery()
    for item in items:
        print(item.link)

def get_images(username):
    # removes all .txt files
    init_command = 'rm *.txt'
    os.system(init_command)
    # get list of most recent pictures from imgur account
    command = 'curl --location --request GET "https://api.imgur.com/3/account/' + username + '/images/" \--header "Authorization: Bearer ' + token +'" >> img_data.txt'
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
            path = "./imgur/img" + str(counter) + ".jpg"
            with open(path, 'wb') as img:
                img.write(response.content)
            counter+=1
    print("DONE DOWNLOADING")

    # load files to home
    imgur_source = "./imgur/"
    home_dest1 = "./frontend/static/h_images/fulls"
    home_dest2 = "./frontend/static/h_images/thumbs"

    files = os.listdir(imgur_source)

    for img in files:
        shutil.copy(imgur_source + img, home_dest1)
        shutil.copy(imgur_source + img, home_dest2)

    print("DONE MOVING")

def get_account(username):
    command = 'curl --location --request GET "https://api.imgur.com/3/account/' + username + '" \--header "Authorization: Client-ID df4cc21b8273314" >> imgur_account.json'
    os.system(command)
