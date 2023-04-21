import requests
import re


class Github:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48"
        }

    @staticmethod
    def get_authenticity_token(html):
        return re.findall('<input type="hidden" name="authenticity_token" value="(.*?)" />', html, re.S)[0]

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
        self.session.post('https://github.com/session', data=data)

    def follow_user(self, username):
        follow_url = f"https://github.com/{username}/"
        response = self.session.get(follow_url)

        html = response.text
        follow_auth_token = Github.get_authenticity_token(html)

        follow_data = {
            "commit": "Follow",
            "authenticity_token": follow_auth_token,
        }

        follow_response = self.session.post(
            f"https://github.com/users/follow?target={username}",
            data=follow_data,
        )

        return follow_response.status_code


if __name__ == "__main__":
    github = Github()
    github.login('', '')
    result = github.follow_user('cpt1225')
    print(result)
