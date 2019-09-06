import os.path
import shutil

class Builder():
    def __init__(self, format, base_dir, output_path, name, **kwargs):
        self.format = format
        self.base_dir = base_dir
        self.output_path = output_path
        self.name = name
        super().__init__(**kwargs)
    

class StandardBuilder(Builder):
    def __init__(self, format, base_dir, output_path, name, **kwargs):
        super().__init__(format, base_dir, output_path, name, **kwargs)

    def check_format(self):
        pass
    
    def build(self, dry_run=False):
        base_name = os.path.join(self.base_dir, self.name)
        self.__file_location = shutil.make_archive(
            base_name=base_name,
            format=self.format,
            base_dir=self.base_dir,
            dry_run=dry_run,
        )
        if self.base_dir != self.output_path:
            print('moving file to: ', self.output_path)
            self.move()
        return self.output_path

    def move(self):
        shutil.move(
            src=self.__file_location,
            dst=self.output_path, 
            copy_function='copy2',
            )

    
