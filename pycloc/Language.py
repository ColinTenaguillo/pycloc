from typing import List


class Language:
    language_name: str
    files: int = 0
    codes: int = 0
    comments: int = 0
    blanks: int = 0

    def __init__(self, language_name) -> None:
        self.language_name = language_name

    def add_count(self, codes, comments, blanks) -> None:
        self.files += 1
        self.codes += codes
        self.comments += comments
        self.blanks += blanks

    def format(self) -> List:
        total_lines = self.codes + self.comments + self.blanks
        return [
            self.language_name, 
            self.files, 
            total_lines, 
            self.codes, 
            self.comments, 
            self.blanks
        ]