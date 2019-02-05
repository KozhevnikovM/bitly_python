import requests, json, os
from dotenv import load_dotenv
from urllib.parse import urlparse


def generate_headers():
    """
    :return: http headers with bitly token
    """
    headers = {'Authorization': 'Bearer {}'.format(TOKEN)}
    return headers


def get_response(api_path, method='get', data=None):
    """
    :param api_path: path to bitly api method
    :param method: http method 'get' or 'post'
    :param data: Any data in json.
    :return: requests.models.Response
    """
    url = 'https://api-ssl.bitly.com/v4/{}'.format(api_path)
    headers = generate_headers()
    if method == 'get':
        response = requests.get(url, headers=headers)
    if method == 'post':
        response = requests.post(url, headers=headers, data=data)
    return response

def check_if_bitlink(url):
    url = urlparse(url)[1]+urlparse(url)[2]
    response = get_response('bitlinks/{bitlink}'.format(bitlink=url))
    return response.ok

def get_bitlink(long_url):
    """
    :param long_url: url that need to be shorten
    :return: bitlink
    """
    data = json.dumps(
        {'long_url': long_url}
    )
    response = get_response('bitlinks', method='post', data=data)
    if not response.ok:
        response.raise_for_status()
    short_link = json.loads(response.text)['link']
    return short_link


def get_clicks_amount(bitlink):
    """
    :param bitlink
    :return: Total clicks on bitlink
    """
    bitlink = urlparse(bitlink)[1] + urlparse(bitlink)[2]
    response = get_response('bitlinks/{}/clicks/summary'.format(bitlink))
    if not response.ok:
        response.raise_for_status()
    total_clicks = json.loads(response.text)['total_clicks']
    return total_clicks


def handle_any_link(url):
    """
    :param url: Bitlink or url that need to be shorten
    :return: Bitlink or Total clicks on bitlink
    """
    if check_if_bitlink(url):
        return "Total links on bitlink: {}".format(get_clicks_amount(url))
    else:
        return 'Take your bitlink: {}'.format(get_bitlink(url))


if __name__ == '__main__':
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    url = input('Enter long url or BitLink: ')
    try:
        print(
            handle_any_link(url)
        )
    except requests.exceptions.HTTPError as error:
        print('{}\nCheck the url you entered'.format(error))
