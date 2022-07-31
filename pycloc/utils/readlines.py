import re


def countlines(path: str):
    with open(path, "r") as file:
        lines = file.readlines()
        blank_lines = len([l for l in lines if l.strip(' \n') == ''])

        regex = re.compile("\/\*(\*(?!\/)|[^*])*\*\/")

        result = regex.search(file.read())
        print("result", result)

        comment_lines = 0
        for line in lines:
            line = line.lstrip()

            # Single line comments
            if line.startswith("//"):
                comment_lines += 1

            # Multiline comments

        return {
            "lines": len(lines),
            "blank": blank_lines,
            "comment": comment_lines,
            "code": len(lines) - blank_lines - comment_lines,
        }