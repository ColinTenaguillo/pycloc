import re
from typing import List
from xml.etree.ElementInclude import include

def count_comments_lines(comments: List[str]) -> int:
    lines = 0
    
    for comment in comments:
        comment_lines = comment.splitlines()
        blank_lines = len([l for l in comment_lines if l.strip(' \n') == ''])
        lines += len(comment_lines) - blank_lines
    
    return lines


def countlines(path: str):
    if not path.endswith(".cpp"):
        return

    with open(path, "r") as file:
        lines = file.readlines()
        file.seek(0)
        data = file.read()

        # Find blank lines
        blank_lines = len([l for l in lines if l.strip(' \n') == ''])

        # Find multiline comments
        comments: List[str] = re.findall("\/\*(?:\*(?:!\/)|[^*])*\*\/", data)
        comment_lines = count_comments_lines(comments)

        # Find single line comments
        for line in lines:
            line = line.lstrip()
            # Single line comments
            if line.startswith("//"):
                comment_lines += 1

        return {
            "lines": len(lines),
            "blank": blank_lines,
            "comment": comment_lines,
            "code": len(lines) - blank_lines - comment_lines,
        }