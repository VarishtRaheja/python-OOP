"""File checker in IP. Contributions welcome."""

import pathlib,os

class File:
    def __init__(self, filename):
        self.filename = filename

    def check_existence(self):
        curr_path = pathlib.Path.cwd().joinpath(f"/{self.filename}")
        if curr_path.exists():
            yield f"The {self.filename} exists in the directory."
            os.remove(curr_path)
        else:
            return "File does not exist."

canvas_name = input("Enter name of canvas name: ")
file_obj = File(canvas_name).check_existence()
print(file_obj)
# curr_path = pathlib.Path.absolute(pathlib.Path.cwd()+"/"+file_path)

