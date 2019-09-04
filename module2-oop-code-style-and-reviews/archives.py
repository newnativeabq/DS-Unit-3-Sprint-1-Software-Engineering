import os.path
from os import path
import os

from shutil import make_archive


class Archive():
	def __init__(self, path=None, output_format=None, archive_name=None, root_dir=None):
		if path == None:
			self.path = os.getcwd()
		else:
			self.path = path
		self.format = self.get_format()
		self.output_format = output_format
		self.archive_name = archive_name
		if file_exists(self.path):
			self.assign_scanner()
		if output_format != None:
			self.assign_builder()
		else:
			self.output_format = format

	def assign_scanner(self):
		self.root_dir, self.scanner = 'Directory', DummyScanner()
	def assign_builder(self):
		self.builder = DummyBuilder()
	def get_format(self):
		return parse_format_from_path(self.path)
	def set_format(self):
		self.builder = 'TestBuilder'


class DummyBuilder(Archive):
	def __init__(self, **kwargs):
		super().__init__(kwargs)
	def build(self):
		return make_archive(self.archive_name, self.format, self.root_dir)

class DummyScanner(Archive):
	def __init__(self, **kwargs):
		super().__init__(kwargs)
	def scan(self):
		return os.listdir(self.path)


def parse_format_from_path(path):
	path_as_str = str(path)
	return path_as_str.split('.')[-1]


def file_exists(path):
	print('checking path', path)
	return os.path.exists(path)

