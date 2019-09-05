import os.path

import archive_builders
import archive_scanners

class Archive():
	def __init__(self, path=None, format=None):
		self.get_path(path)
		self.get_format_from_path(self.path)

	def get_path(self, path):
		if path == None:
			self.path = os.getcwd()
		else:
			self.path = os.path.abspath(path)

	def get_format_from_path(self, path):
		# Set archive view type (viewing directory of files or compressed file)
		if path_is_directory(path):
			self.format = 'directory'
		else:
			print(parse_format_from_path(self.path))
			self.format = parse_format_from_path(self.path)

	def set_format(self, format):
		if format_is_valid(format):
			self.format = format
		else:
			print('Invalid Format')

	def scan(self):
		scanner = assign_scanner(path=self.path, format=self.format)
		self.__file_list = scanner.scan()
		print(self.__file_list)


def path_is_directory(path):
	return os.path.isdir(path)

def parse_format_from_path(path):
	if os.path.isfile(path):
		if type(path) == str:
			path_as_str = path
		else:
			path_as_str = str(path)
		suffix = path_as_str.split('.')[-1]
	else:
		raise TypeError
	return suffix

def file_exists(path):
	return os.path.exists(path)

def format_is_valid(format):
	builder_options = list(builder_menu.keys())
	scanner_options = list(scanner_menu.keys())

	if (format in builder_options) | (format in scanner_options):
		return True
	else:
		return False

def menu_lookup(format, menu):
	return menu[format]

def assign_scanner(path, format):
	scanner_details = menu_lookup(format, scanner_menu)
	scanner = scanner_details[0](path=path, format=scanner_details[1])
	return scanner

builder_menu = {
	'bztar': (archive_builders.StandardBuilder, 'bztar'),
	'gztar': (archive_builders.StandardBuilder, 'gztar'),
	'tar': (archive_builders.StandardBuilder, 'tar'), 
	'xztar': (archive_builders.StandardBuilder, 'xztar'),
	'zip': (archive_builders.StandardBuilder, 'zip'),
}

scanner_menu = {
	'bztar': (None, 'bztar'),
	'gztar': (None, 'gztar'),
	'tar': (None, 'tar'), 
	'xztar': (None, 'xztar'),
	'zip': (archive_scanners.ZipScanner, 'zip'),
	'directory': (archive_scanners.DirectoryScanner, 'directory'),
}