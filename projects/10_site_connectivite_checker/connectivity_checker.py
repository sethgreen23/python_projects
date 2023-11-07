import requests
import socket

def check_connectivity(url):
    try:
        print("Checking connectivity...")
        # Request the url and then check the status
        response = requests.get(url)
        if response.status_code == 200:
            print(f'Successfully connected to {url}')
        else:
            print(f'Failed to connect to {url}. Status code {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Failed to connect to {url}.Exception: {str(e)}')
    except socket.gaierror as e:
        print(f'Failed to resolve hostname for {url}. Exception: {str(e)}')

url = input("Please enter the url: ")
check_connectivity(url)
