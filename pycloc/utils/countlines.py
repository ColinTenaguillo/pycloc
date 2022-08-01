import os
import re
from typing import List
from pycloc.language import Language

def count_comments_lines(comments: List[str]) -> int:
    lines = 0
    
    for comment in comments:
        comment_lines = comment.splitlines()
        blank_lines = len([l for l in comment_lines if l.strip(' \n') == ''])
        lines += len(comment_lines) - blank_lines
    
    return lines


def countlines(
        path: str,
        single_line_comments: List[str],
        multiline_comments_regex: List[str],
    ):
    with open(path, "r") as file:
        lines = file.readlines()
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
            comment_lines += count_comments_lines(comments)

        return {
            "blanks": blank_lines,
            "comments": comment_lines,
            "codes": total_lines - blank_lines - comment_lines,
        }