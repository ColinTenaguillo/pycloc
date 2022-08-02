from pycloc.language import Language

LANGUAGES = {
    ('.cpp'): Language("C++", ["//"], ["\/\*(?:.|[\r\n])*?\*\/"]), 
    ('.rb'): Language("RUBY", ["#"], ["=begin(?:.|[\r\n])*=end", "__END__(?:.|[\r\n])*", "<<-DOC(?:.|[\r\n])*DOC"]),
}