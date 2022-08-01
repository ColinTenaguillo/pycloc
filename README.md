# pycloc

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
