# Prolog - Auto Generated #
import matplotlib
import os
import uuid

matplotlib.use('Agg')
import matplotlib.pyplot
import pandas

import sys

sys.tracebacklimit = 0


# os.chdir(u'C:/Users/alana/PythonEditorWrapper_5695ddf6-f19a-4018-9ea5-9e0e5f2c6aaa')
matplotlib.pyplot.figure(figsize=(5.55555555555556, 4.16666666666667), dpi=72)
matplotlib.pyplot.show = lambda args=None, kw=None: matplotlib.pyplot.savefig(str(uuid.uuid1()))
# Original Script. Please update your script content here and once completed copy below section back to the original editing window #


def dataset_filter():
    dataset = pandas.read_csv('export-analytics_2022-05-20_21_50_41.csv')
    dataset = pandas.DataFrame(dataset)
    dataset = dataset[["Produto", "Fase", "Data de cancelamento da inscrição"]]
    dataset = dataset.drop_duplicates()
    return dataset


fun_dataset = dataset_filter()


def datasetgen_filter():
    general = pandas.read_csv('general_inasistencia.csv', on_bad_lines='skip', sep=';')
    general = pandas.DataFrame(general)
    general = general[["Aluno", "Turma", "Faltas", "Fase", "Justificadas", "E-mail"]]
    general = general.drop_duplicates()
    return general


gen = datasetgen_filter()

frames = [gen, fun_dataset]
compilation = pandas.concat(frames).drop_duplicates().reset_index(drop=True)

turno = []
for i in compilation.Produto:
    if i == "0521CDCTDWI01BRED" or \
            i == "0222CDCTDWI1BRED0222FT" or \
            i == "0522CDGENCGTGBRED0522FT" or \
            i == "0821CDCTDWI2BRED":
        turno.append("FT")
    else:
        turno.append("PT")

compilation.insert(3, "Turno", turno)
compilation.to_csv('sge_minimalist.csv')

# Epilog - Auto Generated #
# os.chdir(u'C:/Users/alana/PythonEditorWrapper_5695ddf6-f19a-4018-9ea5-9e0e5f2c6aaa')
