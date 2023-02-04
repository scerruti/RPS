DOCSTRING = '<!DOCTYPE html>'
HTML_START = '<html>'
HTML_END = '</html>'
HTML_HEAD = '<head><title>{}</title></head>'
BODY_START = "<body>"
BODY_END = "</body>"

# How to use HTML_HEAD:
# print(HTML_HEAD.format('About Me Webpage'))

PARAGRAPH = '<p>{}</p>'

HEADING1 = '<h1>{}</h1>'
HEADING2 = '<h2>{}</h2>'
HEADING3 = '<h3>{}</h3>'
HEADING4 = '<h4>{}</h4>'
HEADING5 = '<h5>{}</h5>'

IMAGE = "<img src={} alt={} />"

ORDERED_LIST_START = "<ol>"
ORDERED_LIST_END = "</ol>"

UNORDERED_LIST_START = "<ul>"
UNORDERED_LIST_END = "</ul>"

LIST_ITEM = "<li>{}</li>"

"""
    How to use LIST_ITEM:
    
    print(ORDERED_LIST_START)
    print(LIST_ITEM.format(Item 1'))
    print(LIST_ITEM.format(Item 2'))
    print(LIST_ITEM.format(Item 3'))
    print(ORDERED_LIST_END)
"""



