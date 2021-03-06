from dropbox import client, rest, session
import sys

APP_KEY = 'YOUR_APP_KEY_HERE'
APP_SECRET = 'YOUR_APP_SECRET_HERE'

#
# Request authorization code (via browser)
#
def do_login():
    """log in to a Dropbox account"""
    flow = client.DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)
    authorize_url = flow.start()
    sys.stderr.write("1. Go to: " + authorize_url + "\n")
    sys.stderr.write("2. Click \"Allow\" (you might have to log in first).\n")
    sys.stderr.write("3. Copy the authorization code.\n")
    sys.stderr.write("Enter the authorization code here: ")
    code = raw_input("").strip()
    try:
        access_token, user_id = flow.finish(code)
    except rest.ErrorResponse as e:
        sys.stdout.write('Error: %s\n' % str(e))
        return None
    return access_token

#
# Initialize the session and Dropbox client
#
def initialize_dropbox_client():
    api_client = None
    try:
        access_token = do_login()
        api_client = client.DropboxClient(access_token)
        sys.stdout.write('Dropbox client initialized...\n')
    except Exception as e:
        sys.stdout.write('Invalid access token (%s)\n' % access_token)
    return api_client

#
# Check if the folder contains a file whose name matches the found .aaa file
#
def has_original_file(contents, original_file):
    for fileinfo in contents:
        if fileinfo['path'] == original_file:
            return True
    return False
