import re
from typing import Dict, List

def count_non_blank_lines(texts: List[str]) -> int:
    """Take a list of string, remove blank lines, and count rest of lines

    Args:
        texts (List[str]): List of texts as strings

    Returns:
        int: return the number of lines within given texts
    """    
    i = 0
    for text in texts:
        lines = text.splitlines()
        blank_lines = len([l for l in lines if l.strip(' \n') == ''])
        i += len(lines) - blank_lines
    
    return i


def countlines(
        path: str,
        single_line_comments: List[str],
        multiline_comments_regex: List[str],
    ) -> Dict[str, int]:
    """Count lines of codes, comments, and blanks within a file.

    Args:
        path (str): path to file
        single_line_comments (List[str]): Starting character of line for comments
        multiline_comments_regex (List[str]): Regexp use to find comments in files.

    Returns:
        Dict[str, int]: Return a dict with blanks, comments and codes total count.
    """    
    with open(path, "r") as file:
        try:
            lines = file.readlines()
        except UnicodeDecodeError:
            print(path)
        total_lines = len(lines)

        # Remove and Count blank lines
        blank_lines = len([l for l in lines if l.strip(' \n') == ''])
        lines = [s for s in lines if s.strip(' \n') != '']

        comment_lines = 0
        # Remove and count single line comments
        for single_line_comment in single_line_comments:
            comment_lines += len([l for l in lines if l.strip().startswith(single_line_comment)])
            lines = [l for l in lines if not l.strip().startswith(single_line_comment)]

        # Find multiline comments
        data = "".join(lines)

        for multiline_comments_regex in multiline_comments_regex:
            comments: List[str] = re.findall(multiline_comments_regex, data)
            comment_lines += count_non_blank_lines(comments)

        return {
            "blanks": blank_lines,
            "comments": comment_lines,
            "codes": total_lines - blank_lines - comment_lines,
        }