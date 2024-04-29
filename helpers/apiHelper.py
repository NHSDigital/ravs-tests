import sys
import requests

class ApiRequestBase:

    @staticmethod
    def handle_response(response):
        if response.status_code == 200:
            return response.text
        elif response.status_code == 502:
            print("Deployment may be in progress, and the environment is not available. Also, check the env Url for any issues. Terminating the program.")
            sys.exit()
        else:
            print(f"API call failed with status code {response.status_code}")
            return None

    @staticmethod
    def get_request(url, headers=None):
        try:
            options = {}
            if headers is not None:
                options['headers'] = headers

            response = requests.get(url, **options)
            return ApiRequestBase.handle_response(response)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    @staticmethod
    def post_request(url, headers=None, data=None, files=None):
        try:
            options = {}
            if headers is not None:
                options['headers'] = headers

            if data is not None:
                options['data'] = data

            if files is not None:
                options['files'] = files

            response = requests.post(url, **options)
            return ApiRequestBase.handle_response(response)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

class ApiHelper(ApiRequestBase):

    @staticmethod
    def post_request_datafiles(url, headers=None, data=None):
        try:
            response = requests.post(url, headers=headers, data=data)
            return ApiRequestBase.handle_response(response)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
