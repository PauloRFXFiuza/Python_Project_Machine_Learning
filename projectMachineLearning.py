'''Machine Learning Project - By Paulo Fiuza- 12/29/2024
Projeto Machine Learning'''

import pandas as pd, matplotlib.pyplot as plt, seaborn as sb, sweetviz as sv
'''from pandas_profiling import ProfileReport as pr'''

pd.options.display.float_format = '{:,.2f}'.format
'''%matplotlib inline'''

'''Show Data Base
Mostrar a base de dados'''

base = pd.read_csv("melb_data.csv")
print(base)

'''Generate the database report
Gerar o relatório da base de dados'''

report = sv.analyze(base)
report.show_html("report.html")

'''Remove columns with high cardinality
Retirar colunas que tiverem uma alta cardinalidade'''

'''base = base.drop(["Suburb", "Address", "SellerG", "Date"], axis=1)
print(base)'''