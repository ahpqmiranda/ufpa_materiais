import pylatex as pl
import pylatex.utils as plu
import docx2txt as d2t
import pandas as pd
import os


if __name__ == '__main__':
    # Create a document
    geometry_options = {'tmargin': '1.5cm', 'lmargin': '1.5cm'}
    doc = pl.Document(geometry_options=geometry_options)
    with doc.create(pl.Section('1. Introdução', numbering=True, label='introducao')):
        doc.append(pl.NoEscape(r"""paragráfo 1"""))

    with doc.create(pl.Section("Tabela 1 - Tabela de Dados", numbering=True, label='tabela1')):
        doc.append(r""" texto // mais texto""")
        doc.append((pl.Subsection("Tabela 1.1 - Tabela de Dados")))
        doc.append(r""" texto // mais texto""")

        doc.generate_pdf('teste estrutura doc', clean_tex=False)