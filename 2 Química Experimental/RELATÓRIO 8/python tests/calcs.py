from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape
from report_file import chemical


def calcs_equations():
    # (1) 2HCl + NaOH -> NaCl + H2O
    # impute data like (name, molar mass, density, m)
    formulas = chemical('NaOH', 40.00, 2.13, 0.100)
    formulas2 = chemical('NaCl', 58.44, 2.17, 0.100)
    formulas3 = chemical('HCl', 36.46, 1.19, 0.100)
    formulas4 = chemical('H2O', 18.02, 1.00, 0.100)



def fill_document(doc):
    """Add a section, a subsection and some text to the document.

    :param doc: the document
    :type doc: :class:`pylatex.document.Document` instance
    """
    with doc.create(Section('A section')):
        doc.append('Some regular text and some ')
        doc.append(italic('italic text. '))

        with doc.create(Subsection('A subsection')):
            doc.append('Also some crazy characters: $&#{}')


if __name__ == '__main__':
    calcs_equations()

# if __name__ == '__main__':
    # Basic document
    doc = Document('basic')
    fill_document(doc)

    doc.generate_pdf(clean_tex=False)
    doc.generate_tex()

    # Document with `\maketitle` command activated
    doc = Document()

    doc.preamble.append(Command('title', 'Awesome Title'))
    doc.preamble.append(Command('author', 'Anonymous author'))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.append(NoEscape(r'\maketitle'))

    fill_document(doc)

    doc.generate_pdf('basic_maketitle', clean_tex=False)

    # Add stuff to the document
    with doc.create(Section('A second section')):
        doc.append('Some text.')

    doc.generate_pdf('basic_maketitle2', clean_tex=False)
    tex = doc.dumps()  # The document as string in LaTeX syntax
