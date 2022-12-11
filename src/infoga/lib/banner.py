#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : Infoga - Email OSINT
# @url    : http://github.com/m4ll0k
# @author : Momo Outaadi (m4ll0k)

from lib.colors import *

class Banner:
	def banner(self):
		print("")

	def usage(self,_exit_=False):
		self.banner()
		print("Usage: infoga.py [OPTIONS]\n")
		print("\t-d --domain\tTarget URL/Name")
		print("\t-s --source\tSource data, default \"all\":\n")
		print("\t\tall\tUse all search engine")
		print("\t\tgoogle\tUse google search engine")
		print("\t\tbing\tUse bing search engine")
		print("\t\tyahoo\tUse yahoo search engine")
		print("\t\task\tUse ask search engine")
		print("\t\tbaidu\tUse baidu search engine")
		print("\t\tdogpile\tUse dogpile search engine")
		print("\t\texalead\tUse exalead search engine")
		print("\t\tpgp\tUse pgp search engine\n")
		print("\t-b --breach\tCheck if email breached")
		print("\t-i --info\tGet email informations")
		print("\t-r --report\tSimple file text report")
		print("\t-v --verbose\tVerbosity level (1,2 or 3)")
		print("\t-H --help\tShow this help and exit\n")
		print("Example:")
		print("\tinfoga.py --domain site.gov -v 3")
		print("\tinfoga.py --info admin@site.gov -v 3")
		print("\tinfoga.py --domain site.gov --source pgp --breach -v 1")
		print("\tinfoga.py --domain site.gov --source google --breach --report site_gov.txt -v 3\n")
		if _exit_: exit(0)
