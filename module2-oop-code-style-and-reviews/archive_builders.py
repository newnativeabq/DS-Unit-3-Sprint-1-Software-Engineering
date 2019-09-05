import os.path
from shutil import make_archive

class Builder():
    def __init__(self, format, file_list, output_path, **kwargs):
        self.format = format
        self.file_list = file_list
        self.output_path = output_path
        super().__init__(**kwargs)
    

class StandardBuilder(Builder):
    def __init__(self, format, file_list, output_path, **kwargs):
        super().__init__(format, file_list, output_path, **kwargs)

    def check_format(self):
        pass
    
    def build(self):
        pass

    def move_to_target_directory(self):
        pass
    
