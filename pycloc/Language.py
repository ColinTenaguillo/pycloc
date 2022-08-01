from typing import List


class Language:
    language_name: str
    files: int = 0
    codes: int = 0
    comments: int = 0
    blanks: int = 0
    single_line_comments: List[str] = []
    multiline_comments_regex: List[str] = []

    def __init__(
        self, 
        language_name: str, 
        single_line_comments: List[str], 
        multiline_comments_regex: List[str]
    ) -> None:
        self.language_name = language_name
        self.single_line_comments = single_line_comments
        self.multiline_comments_regex = multiline_comments_regex

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