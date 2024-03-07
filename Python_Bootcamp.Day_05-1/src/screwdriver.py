import sys
import os
import requests

import argparse


def list_music():
    response = requests.get('http://localhost:8888/list_files')

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        files = data.get('files', [])
        for file in files:
            print(file)
    else:
        print(f"Error: {response.status_code}")


def upload_music(file):

    upload_url = 'http://localhost:8888/UploadFile'

    files = {'file': (file.name, file)}
    response_post = requests.post(upload_url, files=files)

    # Check the status code of the POST request
    if response_post.status_code == 200:
        print('File uploaded successfully!')
    else:
        print(f'Error: {response_post.status_code}')
        print(response_post.text)


def main():
    parser = argparse.ArgumentParser(
        description='Example command-line interface.')

    # Argument without parameters
    parser.add_argument('command', choices=[
                        'list', 'upload'], help='Specify the command (list or upload).')

    # Argument with a parameter (filepath)
    parser.add_argument('file', type=argparse.FileType(
        'rb'), nargs='?', help='Filepath for upload command.')

    args = parser.parse_args()

    if args.command == 'list' and not args.file:
        list_music()

    elif args.command == 'upload':
        if args.file:
            upload_music(args.file)
        else:
            print('Error: Missing filepath for upload command.')


if __name__ == '__main__':
    main()
