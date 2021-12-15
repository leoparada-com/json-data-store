import json # para formatear visualizacion de un .json en consola
import pandas as pd
from   tabulate import tabulate
import numpy  as np

# ----------------------------------------------------------------------------------
# [1] LECTURA DE ARCHIVO .json COMO UN DICCIONARIO
# ----------------------------------------------------------------------------------

def load_json(file_name):
    # Opening JSON file
    f = open(file_name) 
    # returns JSON object as a dictionary
    diccionario = json.load(f)
    # Closing file
    f.close()
    return diccionario

# ----------------------------------------------------------------------------------
# [2] GUARDADO DE ARCHIVO .json COMO UN DICCIONARIO
# ----------------------------------------------------------------------------------

def save_json(file_content, file_name):
    with open(file_name, 'w') as file:
        json.dump(file_content, file, indent=4)
    file.close()
    return

# ----------------------------------------------------------------------------------
# [4] TABULACION DE: DATAFRAME, DICCIONARIO
# ----------------------------------------------------------------------------------

def print_tabula_df(element_df): 
    keys = element_df.columns.tolist()
    print(tabulate(element_df, headers = keys, showindex=True, tablefmt='fancy_grid'))
    return

def print_tabula_dic(element_dic): 
    keys = element_dic.keys()
    print(tabulate(element_dic, headers = keys, showindex=True, tablefmt='fancy_grid'))
    return

# ----------------------------------------------------------------------------------
# [5] TRANSFORMACION DE UN DATAFRAME A DICCIONARIO
# ----------------------------------------------------------------------------------

def df2dic(data_frame):
    diccio = {}
    keys = data_frame.columns.tolist()
    for i in keys:
        diccio[i] = list(data_frame[i])
    return diccio


def dic2df(elemento_diccionario):
    A = elemento_diccionario
    B = list(elemento_diccionario.keys())   
    data_frame = pd.DataFrame(A, columns = B) # creacion del data frame 
       
    return data_frame

# -----------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------
#                                         INCIO
# ----------------------------------------------------------------------------------
# [1] LECTURA DEL ARCHIVO
file_name   = 'data_in.json'
# lectura a diccionario
# diccionario = load_json(file_name)
# lectura a DataFrame
df = pd.read_json('data_in.json')
# ----------------------------------------------------------------------------------

# [2] VISUALIZACION DE LA DATA DEL ARCHIVO
#json_formatted_str = json.dumps(diccionario, indent=1)

opt = True
if (opt):
    #print(json_formatted_str)
    print('INPUT: data_frame')
    print_tabula_df(df)
    print()
# print_tabula_dic(diccionario)


# ======================================================================================
# ---- [3] PROCESAMIENTO ---------------------------------------------------------------
# TODO


input = df

# anexear un registro
diccionario_2 =  {
        "equipo"             : ["Equipo EXTRA numero 2"],
        "puntos"             : [31],
        "goles_a_favor"      : [62],
        "goles_en_contra"    : [2],
        "tarjetas_amarillas" : [24],
        "tarjetas_rojas"     : [3]
    }

df_2 = dic2df(diccionario_2)


out = pd.concat([df, df_2])



# ======================================================================================


# [4] ----------------------------------------------------------------------------------
# RECONVERSION A DICCIONARIO
diccionario_2 = df2dic(out)
print(diccionario_2)
if (opt):
    print('OUTPUT: data_frame')
    print_tabula_dic(diccionario_2)

# [5] ----------------------------------------------------------------------------------
# GUARDADO DEL DICCIONARIO A ARCHIVO .json
save_json(diccionario_2,'data_out.json')




