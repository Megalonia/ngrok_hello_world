from typing import Dict
from dotenv import load_dotenv
import os
import requests

load_dotenv()
api_key: str = os.environ["authtoken"]
domain: str = os.environ['domain']

tunnels: str         = 'https://api.ngrok.com/tunnels'
https_edge: str      = 'https://api.ngrok.com/edges/https'
reserved_domain: str = 'https://api.ngrok.com/reserved_domains'
http_response: str   = 'https://api.ngrok.com/backends/http_response'

header : Dict[str,str] = {
    "Authorization" : "Bearer " + api_key,
    "Content-Type"  : "application/json",
    "Ngrok-Version" : "2"
}

reserved_domain_obj : Dict[str,str] = {
    "name"  : domain,
    "region": "us",
}

https_response_obj: dict = {
    "body"       : "Hello, World!",
    "headers"    : {"Content-Type": "text/plain"},
    "status_code": 418
}

https_edge_obj : Dict[str,str] = {
    "hostports":  domain + ":443",
}

"""data : Dict[str,str] = {
    "match_type" : "exact_path",
    "match"      : "temp",
}"""

def getTunnels(url: str, header: Dict[str,str]) -> None:
    req = requests.get(url, headers = header)
    print(req.text)

#Maybe make single post function; seems that each post req is the same format over multiple differnt
#req types; just need to pass specific urls and obj into function param
#def postHttpEdge(url,header,data) -> None:
#    req = requests.post(url, json = obj, headers = header)
#    print(req.text)

#def postHttpBackend(url: str, header: Dict[str,str], obj: Dict[str,str]) -> None:
#    req = requests.post(url, json = obj, headers = header)
#    print(req.text)

#def postReservedDomain(url: str, header: Dict[str,str], obj: Dict[str,str]) -> None:
#    req = requests.post(url, json = obj, headers = header)
#    print(req.text)

def post(url: str, header: Dict[str,str], obj: Dict[str,str]) -> None:
    req = requests.post(url, json = obj, headers = header)
    print(req.text)


if __name__ == '__main__':
    getTunnels(tunnels,header)
    post(reserved_domain,header,reserved_domain_obj)

