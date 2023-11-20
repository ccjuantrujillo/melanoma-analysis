# coding=utf-8
import requests
import json
import os
from apig_sdk import signer
from dotenv import load_dotenv
load_dotenv()
class Melanoma:

    def __init__(self):
        self.consumer_key    = os.getenv('API_KEY')
        self.consumer_secret = os.getenv('API_SECRET_KEY')
        self.url_auth        = os.getenv('API_AUTHENTICATE_DOMAIN')
        self.rl_melanoma     = os.getenv('MELANOMA_DOMAIN')
        self.x_auth_token    = ""

    def autenticar(self):
        sig         = signer.Signer()
        sig.Key     = self.consumer_key
        sig.Secret  = self.consumer_secret
        r = signer.HttpRequest("POST", self.url_auth)
        r.headers   = {"content-type": "application/json"}
        r.body      = '{"auth": {"identity": {"methods": ["password"],"password": {"user": {"name": "mtrujillo","password": "Mar.Tru123","domain": {"name": "hid_rzu-2bwbcq7cty1"}}}},"scope": {"project": {"id": "87dc0a784b15427f8c8072d122b82f99"}}}}'
        sig.Sign(r)
        resp = requests.request(r.method, r.scheme + "://" + r.host + r.uri, headers=r.headers, data=r.body)
        if (resp.status_code == 201):
            self.x_auth_token = resp.headers.get("X-Subject-Token")

    def consultar(self, ruta_imagen, nombre_imagen):
        self.autenticar()
        headers  = {"X-AUTH-TOKEN": self.x_auth_token}
        payload  = {}
        files=[
            ('images',(nombre_imagen,open(ruta_imagen,'rb'),'image/jpeg'))
        ]
        response = requests.request("POST", self.rl_melanoma, headers=headers, data=payload, files=files)
        return response.text