from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse, Http404
import os

from django.utils.encoding import smart_unicode, smart_str
from django.contrib.auth.decorators import login_required

import re, htmlentitydefs
from time import time

from bs4 import BeautifulSoup

from website.models import *


@csrf_exempt
@login_required
def userEdit(request):
    
    if not request.user.is_superuser:
        return Http404
    else:
    
        if request.method == 'POST':
        
            # find the file, open and replace with the new version
            template_name = "index_%s.html" % request.POST['lang']
            f = open(os.path.join('templates/', template_name), 'r')
            
            # archive the old file
            content = f.read()
            new_name = "index_%s.%s.html" % (request.POST['lang'], time())
            directory = "%s/templates/archives/%s/" % (settings.PROJECT_PATH, request.user)
            full_path = "".join((directory, new_name))
            new_file = open(full_path, 'w')
            new_file.write(content)
            new_file.close()
            f.close()
            
            
            file = open(os.path.join('templates/', template_name), 'r')
            # now do the new stuff
            soup = BeautifulSoup(file)  
            soup.find(id="container").string = smart_str(request.POST['new'])       
            
                    
            # finally, we'll overwrite the new file
            new_html = smart_unicode(unescape(soup.prettify())) 
            file = open(os.path.join('templates/', template_name), mode='w+')
            file.write(new_html.encode('utf8'))
            file.close()
        else:
            return Http404
                
    return HttpResponse('true')


def get_drafts(request, user):
    # will get old draft versions by a particular user
    
    return

def restore_draft(request):
    # will restore an old draft version, deleting other later versions 
     
    return


def unescape(text):
    def fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            # character reference
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text # leave as is
    return re.sub("&#?\w+;", fixup, text)