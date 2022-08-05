import pandas as pd
import matplotlib.pyplot as plt

arquivo = pd.read_excel("arquivos-do-celular.xlsx", sheet_name=3, header=0)
# print(arquivo)

plt.pie(arquivo['Idade'])

plt.show