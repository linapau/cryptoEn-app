import firebase_admin
from firebase_admin import credentials, storage

cred = credentials.Certificate('data/private_key_firebase.json') 

# Initialize Firebase
firebase_admin.initialize_app(cred, {
    'storageBucket': 'filesharerdb.appspot.com'
})

# Get a reference to the storage service
bucket = storage.bucket()

def upload_file_to_storage(file_data, file_name):
    blob = bucket.blob(file_name)
    blob.upload_from_file(file_data)
    return blob.public_url

def download_file_from_storage(file_name):
    blob = bucket.blob(file_name)
    file_content = blob.download_as_bytes()
    return file_content

