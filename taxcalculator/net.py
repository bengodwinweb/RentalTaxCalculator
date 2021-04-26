# import urllib.request as req
import requests

def format_sheets_url(sheet_url: str) -> str:
    last_slash = sheet_url.rfind('/')
    if last_slash != -1:
        sheet_url = sheet_url[:last_slash + 1]
    return sheet_url + 'pub?output=csv'


def get_data(url: str, fname: str):
    """
    Makes a request to the url and writes the output to a file
    @param url: data source
    @type url: str
    @param fname: output file
    @type fname: str
    """
    r = requests.get(url)
    data = r.content
    with open(fname, 'wb') as fout:
        fout.write(data)
