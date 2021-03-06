
from django.shortcuts import render
from django.http import HttpResponse

import requests
import urllib.request
import urllib.response
import sys
import os, glob

import http.client, urllib
import json
import re
import os


from NLP.audio2text import *


accessKey = ' 401ee36d0e6845bbaee016135291e220'
url = 'westcentralus.api.cognitive.microsoft.com'
path = '/text/analytics/v2.0/keyPhrases'
result = []

def get_detials(json_query):
    res = {}
    res['Address'] = '1600 Amphitheatre Parkway, Mountain View, CA'
    res['Intensity'] = 1
    return res

def get_info():
    # 1.
    documents = extractText()
    # 2. Perform Text Analysis
    result = TextAnalytics(documents)
    print(result)
    res = get_detials(result)
    return res
    # 3. Print Results
    #print (json.dumps(json.loads(result), indent=4))

def extractText():
    documents = { 'documents': []}
    count = 1

    text =get_text_from_audio()
    #text = text.strip('\n')
    text = text.encode('ascii','ignore').decode('ascii')
    documents.setdefault('documents').append({"language":"en","id":str(count),"text":text})
    #count+= 1
    return documents


def TextAnalytics(documents):
    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = http.client.HTTPSConnection(url)
    body = json.dumps (documents)
    conn.request ("POST", path, body, headers)
    response = conn.getresponse ()
    return response.read ()
