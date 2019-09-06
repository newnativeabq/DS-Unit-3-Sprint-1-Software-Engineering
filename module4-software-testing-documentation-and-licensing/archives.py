import os.path

import archive_builders
import archive_scanners

class Archive():
	def __init__(self, path=None, input_type=None):
		self.get_path(path)
		self.get_input_type_from_path(self.path)

	def get_path(self, path):
		if path == None:
			self.path = os.getcwd()
		else:
			self.path = os.path.abspath(path)

	def get_input_type_from_path(self, path):
		# Set archive view type (viewing directory of files or compressed file)
		if path_is_directory(path):
			self.input_type = 'directory'
		else:
			self.input_type = parse_format_from_path(self.path)

	def set_format(self, format):
		if format_is_valid(format):
			self.format = format
		else:
			self.format = 'directory' # default no compression
			print('Invalid Format')

	def scan(self, temp_path=None):
		if temp_path == None:
			scanner = assign_scanner(path=self.path, format=self.input_type)
		else:	
			scanner = assign_scanner(path=self.path, format=self.input_type)
		self.__file_list = scanner.scan()
		return self.__file_list
	
	def build(self, name, format, output_path=None):
		# Set defaults if none given
		if output_path == None:	output_path = self.path
		name = strip_name(name) 
		# Builders need: format, base_dir, output_path, name,
		builder = assign_builder(
			input_path=self.path,
			output_path=output_path,
			name=name,
			format=format,
		)
		self.__archive_location = builder.build()
		return self.__archive_location

	def add(self):
		'''
		Create custom directory of files
		'''
		pass

def strip_name(name):
	test_name = str(name)
	name_components = test_name.split('.')
	if len(name_components) > 1:
		return ''.join(name_components[0:(len(name_components)-1)])
	return name_components[0]

def path_is_directory(path):
	return os.path.isdir(path)

def parse_format_from_path(path):
	if os.path.isfile(path):
		if type(path) == str:
			path_as_str = path
		else:
			path_as_str = str(path)
		suffix = path_as_str.split('.')[-1]
		return suffix
	else:
		raise TypeError("File or directory unavailable")

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

def assign_builder(input_path, output_path, name, format):
	print(type(input_path), type(output_path), type(name), input_path, output_path, name)
	builder_details = menu_lookup(format, builder_menu)
	builder = builder_details[0](format=builder_details[1], base_dir=input_path, output_path=output_path, name=name)
	return builder

builder_menu = {
	'bztar': (archive_builders.StandardBuilder, 'bztar'),
	'gztar': (archive_builders.StandardBuilder, 'gztar'),
	'tar': (archive_builders.StandardBuilder, 'tar'), 
	'xztar': (archive_builders.StandardBuilder, 'xztar'),
	'zip': (archive_builders.StandardBuilder, 'zip'),
	'directory': (archive_builders.StandardBuilder, 'directory'),
}

scanner_menu = {
	'bztar': (None, 'bztar'),
	'gztar': (None, 'gztar'),
	'tar': (None, 'tar'), 
	'xztar': (None, 'xztar'),
	'zip': (archive_scanners.ZipScanner, 'zip'),
	'directory': (archive_scanners.DirectoryScanner, 'directory'),
}