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

from website.models import *


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