import os
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
    if not path.endswith((".cpp", ".h", ".hpp")):
        return

    with open(path, "r") as file:
        lines = file.readlines()
        total_lines = len(lines)

        # Remove and Count blank lines
        blank_lines = len([l for l in lines if l.strip(' \n') == ''])
        lines = [s for s in lines if s.strip(' \n') != '']

        # Remove and count single line comments
        comment_lines = len([l for l in lines if l.strip().startswith("//")])
        lines = [l for l in lines if not l.strip().startswith("//")]

        # Find multiline comments
        data = "".join(lines)
        comments: List[str] = re.findall("\/\*(?:.|[\r\n])*?\*\/", data)
        comment_lines += count_comments_lines(comments)

        return {
            "blanks": blank_lines,
            "comments": comment_lines,
            "codes": total_lines - blank_lines - comment_lines,
        }