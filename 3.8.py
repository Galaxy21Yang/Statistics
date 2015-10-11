import pandas as pd
data5 = [-3, 2, -4, -7, -11, -1, 7, 8, 9, -6,
         -14, -18, -15, -9, -6, -1, 0, 5, -4, -9,
         -6, -8, -12, -16, -19, -15, -22, -25, -24, -19,
         -8, -6, -15, -11, -12, -19, -25, -24, -18, -17,
         -14, -22, -13, -9, -6, 0, -1, 5, -4, -9,
         -3, 2, -4, -4, -16, -1, 7, 5, -6, -5]

data5.sort()
freq_data = pd.Series(data5).value_counts()
print freq_data

df = pd.DataFrame({'A': data5})
d = df['A'].hist().get_figure()
d.savefig('3.8.jpg')
