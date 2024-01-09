import requests
from getpass import getpass

def github_request():
    with requests.Session() as session:
        session.auth = ('fekri8614', getpass())
        response = session.get('https://api.github.com/user')
    
    return response.text

def main():
    print(github_request())


if __name__ == '__main__':
    main()
