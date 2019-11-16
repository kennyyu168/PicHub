from imgurpython import ImgurClient
import webbrowser
import os

client_id = 'df4cc21b8273314'
client_secret = 'ae0d06b7ade1d60d1ea6fe68481fb8df319bf821'

client = ImgurClient(client_id, client_secret)

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


def get_account():
    command = '''curl --location --request GET "https://api.imgur.com/3/account/username4pichub" \--header "Authorization: Client-ID df4cc21b8273314" >> imgur_account.json'''
    os.system(command)

get_account()
