# pycloc

## Installation

It might be a good idea to create a python venv with the env manager of your choice.
It will help prevent libraries conflict even thought there is not a lot used in this project.

Pip install at root of the project.

```bash
pip install -e .
```

## Usage

```
pycloc <path_to_project_directory_or_file>
```

```bash
pycloc Osiris\ 2
```

```bash
Language    Files       Lines       Codes       Comments    Blanks
----------  ----------  ----------  ----------  ----------  ----------
C++         29          36206       28209       3987        4010
----------  ----------  ----------  ----------  ----------  ----------
SUM :       29          36206       28209       3987        4010
```

```bash
pycloc lib\ 2
```

```bash
Language    Files       Lines       Codes       Comments    Blanks
----------  ----------  ----------  ----------  ----------  ----------
RUBY        1482        294891      215208      46099       33584
----------  ----------  ----------  ----------  ----------  ----------
SUM :       1482        294891      215208      46099       33584
```

```bash
pycloc tests/files
```

```bash
Language    Files       Lines       Codes       Comments    Blanks
----------  ----------  ----------  ----------  ----------  ----------
C++         1           13          5           6           2
RUBY        2           44          8           23          13
----------  ----------  ----------  ----------  ----------  ----------
SUM :       3           57          13          29          15
```

## TODO

There is an edge case in ruby i found on [stack overflow](https://stackoverflow.com/questions/2989762/multi-line-comments-in-ruby) that i didnt manage to resolve :

```ruby
<<-DOC
Also, you could create a docstring.
which...
DOC

puts "Hello world!"

"..is kinda ugly and creates
a String instance, but I know one guy
with a Smalltalk background, who
does this."
```
