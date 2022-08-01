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
pycloc <path_to_project_directory>
```

```bash
pycloc Osiris\ 2
```

```bash
Language    Files       Lines       Codes       Comments    Blanks
----------  ----------  ----------  ----------  ----------  ----------
C++         106         53858       40232       7498        6128
----------  ----------  ----------  ----------  ----------  ----------
SUM :       106         53858       40232       7498        6128
```

```bash
pycloc tests/files
```

```bash
Language    Files       Lines       Codes       Comments    Blanks
----------  ----------  ----------  ----------  ----------  ----------
C++         1           17          5           9           3
RUBY        1           37          7           19          11
----------  ----------  ----------  ----------  ----------  ----------
SUM :       2           54          12          28          14
```

## Ruby

There is an edge case i found on [stack overflow](https://stackoverflow.com/questions/2989762/multi-line-comments-in-ruby) that i didnt manage to find a solution for :

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
