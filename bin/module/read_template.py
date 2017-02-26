# encoding: utf-8
"""
setup.read_template - class ReadTemplate

Usage:
	from setup.read_template import ReadTemplate

	template_reader = ReadTemplate()
	content_template = template_reader.read(module)
	if content_template != None:
		# operate with content

@date: Feb 24, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from os.path import dirname, realpath

class ReadTemplate(object):
	"""
	Define class ReadTemplate with atribute(s) and method(s).
	Read a template file (setup.template) and return a string representation.
	It defines:
		attribute:
			__TEMPLATE_DIR - Prefix path to templates
			__TEMPLATES - Modules (python templates)
			__template - Absolute template file path
		method:
			__init__ - Create and initial instance
			read - Read a template and return a string representation
	"""
	
	__TEMPLATE_DIR = "/../../conf/template"

	__TEMPLATES = {
		"1" : "empty.template",
		"2" : "main.template",
		"3" : "class.template",
		"4" : "settings.template",
		"5" : "options.template",
		"6" : "abstract_base_class.template",
		"7" : "abstract_google_class.template"
	}

	def __init__(self):
		"""
		@summary: Basic constructor (initial absolute template file path)
		"""
		cdir = dirname(realpath(__file__))
		self.__template = "{0}{1}".format(cdir, ReadTemplate.__TEMPLATE_DIR)

	def read(self, module):
		"""
		@summary: Read a template file and return a content
		@return: String text code
		"""
		try:
			fpath = "{0}".format(
				self.__template + "/" + ReadTemplate.__TEMPLATES[module]
			)
			tfile = open(fpath, "r")
			setup_content = tfile.read()
			tfile.close()
			return setup_content
		except IOError as e:
			print("I/O error({0}): {1}".format(e.errno, e.strerror))
			return None

