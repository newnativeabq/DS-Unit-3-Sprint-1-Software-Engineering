import os
import zipfile


class Scanner():
    def __init__(self, format, **kwargs):
        self.format = format
        super().__init__(**kwargs)


class ZipScanner(Scanner):
    def __init__(self, path, format, **kwargs):
        self.path = path
        super().__init__(format=format, **kwargs)

    def check_format(self):
        return zipfile.is_zipfile(self.path)
    
    def scan(self):
        with zipfile.ZipFile(self.path) as active_zip:
            namelist = active_zip.namelist()
        return namelist


class DirectoryScanner(Scanner):
    def __init__(self, path, format, **kwargs):
        self.path = path
        super().__init__(format=format, **kwargs)

    def check_format(self):
        return os.path.isdir(self.path)

    def scan(self):
        namelist = []
        with os.scandir(self.path) as entries:
            for entry in entries:
                if entry.is_file():
                    namelist.append(entry.name)
        return namelist