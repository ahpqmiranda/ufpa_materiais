    import math
    import pandas as pd
    import numpy as np
    import sympy as sp
    from sympy.interactive import init_printing
    init_printing(pretty_print=True)

x = sp.Symbol('x')
# funcao = x**10


def esf_cortante():
    texto = '########### CALCULO DE ESFORÇOS ###############\n' \
            'Determine uma origem no sistema de análise e\n' \
            'forneça as informações a seguir:\n'
    print(texto)
    L = float(input('digite o comprimento da barra em análise:\n'))
    n = int(input('digite o número de forças atuantes'))

    strengh_x = []
    strengh_y = []
    range_x = []
    range_y = []
    angles = []
    print('análise de forças:\n')
    for i in range(n):
        locate = str(input('\nDigite o eixo da força "x" ou "y", se for obliquo, digite o ângulo em graus:\n'))

        if locate == 'x':
            value = float(input('\ndigite o valor da força: '+str(i)))
            strengh_x.append(value)
            long = float(input('\nDigite a distância em x da origem da força:'+str(i)))
            range_x.append(long)
            range_y.append(int(0))
            angles.append(math.radians(0))

        elif locate == 'y':
            value = float(input('\nDigite o valor da força: ' + str(i)))
            strengh_y.append(value)
            long = float(input('\nDigite a distância em y da origem da força:' + str(i)))
            range_y.append(long)
            range_x.append(int(0))
            angles.append(math.radians(90))

        elif locate.isnumeric():
            angle = float(locate)
            angle = math.radians(angle)
            value = float(input('\nDigite o valor da força: ' + str(i)))
            vx = value * sp.cos(angle)
            vy = value * sp.sin(angle)
            strengh_x.append(vx)
            strengh_y.append(vy)
            angles.append(angle)
            for j in range(2):
                p = float(input('\nDigite a coordenada posição em x e depois em y:'))
                if j == 0:
                    range_x.append(p)
                else:
                    range_y.append(p)

        else:
            print('\nvalor não reconhecível, tente novamente!!!')
            i -= 1

    dic = {'F em x': strengh_x,
               'F em y': strengh_y,
               'Alavanca x':range_x,
               'Alavanca y':range_y,
                'Angulos':angles
               }

    df = pd.DataFrame().from_dict(dic)
    print(df)



    return

esf_cortante()
