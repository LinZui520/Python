import requests
import re
import time


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

        response = self.session.post('https://github.com/session', data=data)

        if response.status_code == 200:
            return True
        else:
            return False

    def follow_user(self, username):

        url = f"https://github.com/{username}"

        response = self.session.get(url)

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

        if follow_response.status_code == 200:
            return True
        else:
            return False

    def unfollow_user(self, username):
        url = f"https://github.com/{username}"

        response = self.session.get(url)

        html = response.text

        unfollow_auth_token = Github.get_authenticity_token(html)

        unfollow_data = {
            "commit": "Unfollow",
            "authenticity_token": unfollow_auth_token,
        }

        unfollow_response = self.session.post(
            f"https://github.com/users/unfollow?target={username}",
            data=unfollow_data,
        )

        if unfollow_response.status_code == 200:
            return True
        else:
            return False


if __name__ == "__main__":
    github = Github()
    print(github.login('', ''))
    result = github.unfollow_user('cpt1225')
    if result:
        print('User unfollowed successfully!')
    else:
        print('Failed to unfollow user.')
