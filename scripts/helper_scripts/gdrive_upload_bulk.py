import os
import sys
import logging
import httplib2
from mimetypes import guess_type

# Following libraries can be installed by executing:
# sudo pip install --upgrade google-api-python-client
from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from apiclient.errors import ResumableUploadError
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage

credentials = ""

# Log only oauth2client errors
logging.basicConfig(level="ERROR")

# Path to token json file, it should be in same directory as script
token_file = sys.path[0] + '/auth_token.txt'

# Copy your credentials from the APIs Console
CLIENT_ID = ''
CLIENT_SECRET = ''
# Check https://developers.google.com/drive/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive.file'
# Redirect URI for installed apps, can be left as is
REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

for filename in os.listdir("."):
        if filename.endswith(".pdf"):
        	# Get mime type and name of given file
			def file_ops(filename):
			    mime_type = guess_type(filename)[0]
			    mime_type = mime_type if mime_type else 'text/plain'
#			    file_name = filename.split('/')[-1]
#			    return file_name, mime_type


			def create_token_file(token_file):
			# Run through the OAuth flow and retrieve credentials
			    flow = OAuth2WebServerFlow(
			        CLIENT_ID,
			        CLIENT_SECRET,
			        OAUTH_SCOPE,
			        redirect_uri=REDIRECT_URI
			        )
			    authorize_url = flow.step1_get_authorize_url()
			    print('Go to the following link in your browser: ' + authorize_url)
			    code = raw_input('Enter verification code: ').strip()
			    credentials = flow.step2_exchange(code)
			    storage = Storage(token_file)
			    storage.put(credentials)
			    return storage


			def authorize(token_file, storage):
			# Get credentials
		    	    if storage is None:
			        storage = Storage(token_file)
			        credentials = storage.get()
			# Create an httplib2.Http object and authorize it with our credentials
			    http = httplib2.Http()
			    credentials.refresh(http)
			    http = credentials.authorize(http)
			    return http


			def upload_file(filename, mime_type):
			# Create Google Drive service instance
			    drive_service = build('drive', 'v2', http=http)
			# File body description
			    media_body = MediaFileUpload(filename,
			                                 mimetype=mime_type,
			                                 resumable=True)
			    body = {
			        'title': filename,
			        'description': 'backup',
			        'mimeType': mime_type,
			    }
			# Permissions body description: anyone who has link can upload
			# Other permissions can be found at https://developers.google.com/drive/v2/reference/permissions
			    permissions = {
			        'role': 'reader',
			        'type': 'anyone',
			        'value': None,
			        'withLink': True
			    }
			# Insert a file
			    file = drive_service.files().insert(body=body, media_body=media_body).execute()
			# Insert new permissions
			    drive_service.permissions().insert(fileId=file['id'], body=permissions).execute()
			# Define file instance and get url for download
			    file = drive_service.files().get(fileId=file['id']).execute()
			    download_url = file.get('webContentLink')
			    return download_url

			if __name__ == '__main__':
			    try:
			        with open(filename) as f: pass
			    except IOError as e:
			        print(e)
			        sys.exit(1)
			# Check if token file exists, if not create it by requesting authorization code
			try:
			    with open(token_file) as f: pass
			except IOError:
			    http = authorize(token_file, create_token_file(token_file))
			# Authorize, get file parameters, upload file and print out result URL for download
			http = authorize(token_file, None)
			mime_type = file_ops(filename)
			# Sometimes API fails to retrieve starting URI, we wrap it.
			try:
			    print(upload_file(filename, mime_type))
			except ResumableUploadError as e:
			    print("Error occured while first upload try:", e)
			    print("Trying one more time.")
			    print(upload_file(filename, mime_type))
