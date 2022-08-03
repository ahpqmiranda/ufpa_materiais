import pylatex as pl
import pylatex.utils as plu
import docx2txt as d2t
import pandas as pd
import os

def gen_table(df, align='c'):
    """
    Generate a LaTeX table from a pandas dataframe.
    """
    # Create table
    table = pl.Table(table_format= + align * df.shape[1])
    table.add_hline()
    # Add header
    for col in df.columns:
        table.add_row([pl.NoEscape(col)])
        table.add_hline()
    # Add data
    for index, row in df.iterrows():
        table.add_row(row)
        table.add_hline()
    return table

def gen_dataframe():
    """
    Generate a pandas dataframe.
    """
    df = pd.DataFrame(
        data={
            'Name': ['John', 'Paul', 'George', 'Ringo'],
            'Age': [25, 45, 37, 27],
            'Profession': ['Programmer', 'Busser', 'Plumber', 'Mechanic']
        }
    )
    return df

if __name__ == '__main__':
    name = 'RESENHA CRÍTICA RECICLAGEM DE LIXO ELETRÔNICO.docx'
    content = d2t.process(name)
    paragraphs = []
    for line in content.splitlines():
       if len(line) > 15:
           paragraphs.append(line)
    Series_paragraph = pd.Series(paragraphs)
    print(Series_paragraph[9])
    if __name__ == '__main__':
        address = 'mecânica geral/Diagrama_de_Estrutura_(escala_0.6).png'
        graphs = os.path.join(os.path.dirname(__file__), address)

        # Create a document
        geometry_options = {'tmargin': '1.5cm', 'lmargin': '1.5cm'}
        doc = pl.Document(geometry_options=geometry_options)

        with doc.create(pl.Section(Series_paragraph[6])):
            doc.append(Series_paragraph[8])
            doc.append(Series_paragraph[9])
            with doc.create(pl.Subsection(Series_paragraph[7])):
                doc.append(Series_paragraph[10])
                doc.append(Series_paragraph[11])
                doc.append(Series_paragraph[12])

        with doc.create(pl.Section('table')):
            doc.append(gen_table(gen_dataframe()), align='c')

        doc.generate_pdf('RESENHA CRÍTICA RECICLAGEM DE LIXO ELETRÔNICO', clean_tex=False)

