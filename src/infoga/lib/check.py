#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : Infoga - Email OSINT
# @url    : http://github.com/m4ll0k
# @author : Momo Outaadi (m4ll0k)

from lib.output import *
try:
	from urllib.parse import urlparse
except ImportError as e:
	from urlparse import urlparse

def checkTarget(target):
	o = urlparse(target)
	if o.netloc == "":
		return o.path.split('www.')[1] if "www." in o.path else o.path
	return o.netloc.split("www.")[1] if "www." in o.netloc else o.netloc

def checkEmail(email):
	if '@' not in email:
		exit(warn(f'Invalid email {email}'))
	return email

def checkSource(source):
	list_source = ['all','ask','baidu','google','bing',
	               'dogpile','exalead','jigsaw','pgp','yahoo'
	               ]
	if source not in list_source:
		exit(warn(f'Invalid search engine: {source}'))
	return source

def checkVerbose(ver):
	verb = int(ver)
	if   verb == 0: return 1
	elif verb == 1: return 1
	elif verb == 2: return 2
	else: return 3