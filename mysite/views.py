import re
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from bs4 import BeautifulSoup as bs
import urlparse
from urllib2 import urlopen
from urllib import urlretrieve
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
import os
import sys

def search_form(request):
    return render(request,'search_form.html')
  
def search(request):

    if 'q' in request.GET:
        url = request.GET['q']
	regex = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
	urls = re.search(regex,url)
	match = urls.group(0)
	match2=match.rstrip('/.')
	
    else:
        match = 'You submitted an empty form.'

    soup=bs(urlopen(match2))
    
    outputFolder="/home/gunendu/mysite/static/mysite"
    for image in soup.findAll("img", limit=2):
        image_url=urlparse.urljoin(match2,image['src'])  
	filename=image["src"].split("/")[-1]
	outpath=os.path.join(outputFolder,filename)
	urlretrieve(image_url,outpath)
	
	
    return render_to_response('search_form.html',{'url':url},context_instance=RequestContext(request))
	
