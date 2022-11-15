from re import compile, match

class Document:
    ini = 'ini'
    title = 'title'
    author = 'author'
    journal = 'journal'
    abstract = 'abstract'

test_text = """.I 1
.T
experimental investigation of the aerodynamics of a
wing in a slipstream .
.A
brenckman,m.
.B
j. ae. scs. 25, 1958, 324.
.W
experimental investigation of the aerodynamics of a
wing in a slipstream .
  an experimental study of a wing in a propeller slipstream was
made in order to determine the spanwise distribution of the lift
increase due to slipstream at different angles of attack of the wing
and at different free stream to slipstream velocity ratios .  the
results were intended in part as an evaluation basis for different
theoretical treatments of this problem .
  the comparative span loading curves, together with
supporting evidence, showed that a substantial part of the lift increment
produced by the slipstream was due to a /destalling/ or
boundary-layer-control effect .  the integrated remaining lift
increment, after subtracting this destalling lift, was found to agree
well with a potential flow theory .
  an empirical evaluation of the destalling effects was made for
the specific configuration of the experiment ."""

def parse_document(document):
    """Parse document into a list of words."""
    parsed_document = []
    pattern = compile(r'\w*[\d\.\,]\w*')
    lines = document.split('\n')
    for line in lines:
        for word in line.split():
            if match(pattern, word):
                continue
            parsed_document.append(word)
    return parsed_document

if __name__ == '__main__':
    doc = parse_document(test_text)
    print(doc)