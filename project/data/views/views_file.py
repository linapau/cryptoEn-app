import os
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from firebase_admin import storage
from data.firebase import upload_file_to_storage, download_file_from_storage
from ssd_encryption.encryption.utils import EncryptionManager  # Import the encryption manager
import logging

firebase_storage = storage.bucket(settings.FIREBASE_BUCKET)

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file_data = request.FILES['file']
        file_name = file_data.name

        # Read file content
        file_content = file_data.read()

        # Encrypt file content
        password = 'my_secret_password'  # Ideally, use a secure password
        manager = EncryptionManager(password)
        encrypted_content = manager.encrypt_data(file_content)

        # Create a temporary file to store encrypted content
        encrypted_file_path = os.path.join(settings.MEDIA_ROOT, f'encrypted_{file_name}')
        with open(encrypted_file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_content)

        # Upload encrypted file to Firebase Storage
        with open(encrypted_file_path, 'rb') as encrypted_file:
            file_url = upload_file_to_storage(encrypted_file, file_name)

        # Remove the temporary file after uploading
        os.remove(encrypted_file_path)

        return HttpResponse('File uploaded successfully! :)')

    return render(request, 'data/upload_file.html')

def download_file(request, file_name):
    file_path = f'{file_name}'  # Adjust the path as per your Firebase Storage structure

    try:
        file_data = download_file_from_storage(file_path)

        # Decrypt file content
        password = 'my_secret_password'  # Use the same password used during encryption
        manager = EncryptionManager(password)
        decrypted_content = manager.decrypt_data(file_data)

        response = HttpResponse(decrypted_content, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response

    except Exception as e:
        return HttpResponse(f'Error downloading file: {str(e)}')

 
def browse_files(request):
    try:
        # List all files and folders recursively from Firebase Storage
        blobs = firebase_storage.list_blobs()

        # Extract file and folder names from blobs
        files = []
        for blob in blobs:
            if blob.name[-1] == '/':  # It's a folder
                files.append({'name': blob.name, 'type': 'folder'})
            else:  # It's a file
                files.append({'name': blob.name, 'type': 'file'})

        # Log to console to ensure this function is called
        logging.info(f"Fetched {len(files)} files from Firebase Storage")

        # Render template with file list
        return render(request, 'data/download_file.html', {'files': files})

    except Exception as e:
        logging.error(f"Error fetching files from Firebase Storage: {str(e)}")
        return render(request, 'data/download_file.html', {'files': [], 'error_message': str(e)})