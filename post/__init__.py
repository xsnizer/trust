
import logging
import ssl
import urllib.parse
import urllib.request
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    #incoming_request = urlparse(req.url)
    #dict(req.headers).items()
    header_dict = {}
    get_url = 'https://20.243.150.8/api//jquery-3.3.2.min.js'
    for key, value in dict(req.headers).items():
        header_dict.update({key : value})
    #ssl._create_default_https_context = ssl._create_unverified_context
    post_data = req.get_body()
    request = urllib.request.Request(get_url, data=post_data, headers=header_dict)
    with urllib.request.urlopen(request) as response:
        html = response.read()
    return func.HttpResponse(html)
    