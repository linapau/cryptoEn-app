import os

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from firebase_admin import storage
from data.firebase import upload_file_to_storage, download_file_from_storage
import logging

firebase_storage = storage.bucket(settings.FIREBASE_BUCKET)

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file_data = request.FILES['file']
        file_name = file_data.name

        # Upload file to Firebase Storage
        file_url = upload_file_to_storage(file_data, file_name)

        return HttpResponse(f'File uploaded successfully! URL: {file_url}')

    return render(request, 'data/upload_file.html')

def download_file(request, file_name):
    # Construct the full path to the file in Firebase Storage
    file_path = f'{file_name}'  # Adjust the path as per your Firebase Storage structure

    try:
        # Download file content using the function from firebase.py
        file_data = download_file_from_storage(file_path)

        # Create HTTP response with the file data
        response = HttpResponse(file_data, content_type='application/octet-stream')
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