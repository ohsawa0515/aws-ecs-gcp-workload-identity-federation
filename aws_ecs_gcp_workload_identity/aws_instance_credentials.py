import os
from urllib.parse import urljoin
import requests


class AwsInstanceCredentials:

    @classmethod
    def set_credentials(self) -> None:
        url_path = os.environ.get('AWS_CONTAINER_CREDENTIALS_RELATIVE_URI')
        if url_path is None:
            return

        # When the execution environment is ECS, set credentials in env variables.
        url = urljoin('http://169.254.170.2', url_path)
        res = requests.get(url, timeout=3).json()
        os.environ['AWS_ACCESS_KEY_ID'] = res['AccessKeyId']
        os.environ['AWS_SECRET_ACCESS_KEY'] = res['SecretAccessKey']
        os.environ['AWS_SESSION_TOKEN'] = res['Token']


AwsInstanceCredentials.set_credentials()
