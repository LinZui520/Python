import re

import requests


class Github:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            "referer": "https: // github.com /",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/112.0.0.0 Safari/537.36"
        }

    @staticmethod
    def get_authenticity_token(html):
        return re.findall('<input type="hidden" name="authenticity_token" value="(.*?)"', html, re.S)[0]

    @staticmethod
    def get_timestamp(html):
        return re.findall('<input type="hidden" name="timestamp" value="(.*?)"', html, re.S)[0]

    @staticmethod
    def get_timestamp_secret(html):
        return re.findall('<input type="hidden" name="timestamp_secret" value="(.*?)"', html, re.S)[0]

    def login(self, username, password):
        login_url = 'https://github.com/login'
        html = self.session.get(login_url).text

        authenticity_token = Github.get_authenticity_token(html)
        timestamp = Github.get_timestamp(html)
        timestamp_secret = Github.get_timestamp_secret(html)

        data = {
            'commit': 'Sign in',
            'authenticity_token': authenticity_token,
            'login': username,
            'password': password,
            'webauthn-support': 'supported',
            'webauthn-iuvpaa-support': 'supported',
            'return_to': 'https://github.com/login',
            'allow_signup': '',
            'client_id': '',
            'integration': '',
            # 'required_field_e835': '',
            'timestamp': timestamp,
            'timestamp_secret': timestamp_secret,
        }

        return self.session.post('https://github.com/session', data=data)


if __name__ == "__main__":
    github = Github()
    response = github.login('', '')
