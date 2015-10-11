import pandas as pd

data4 = [61.4, 46.8, 65.1, 61.7, 77.4,
         63.9, 54.6, 71.1, 60.5, 52.5,
         73.4, 87.8, 32.5, 27.3, 47.5,
         57.3, 60.5, 52.9, 40.1, 47.9,
         54.8, 60.1, 19.9, 30.4, 58.6,
         56.8, 46.8, 32.7, 81.6, 60.2,
         76.4, 54.9, 37.4, 71.6, 48.2,
         32.1, 39.1, 19.1, 48.9, 38.1,
         52.3, 26.4, 53.3, 55.1, 58.1,
         27.3, 67.9, 74.1, 55.6, 32.5]

data4.sort()
aList = []
for data in data4:
    a = int((data // 10) * 10)
    aList.append(a)
    
freq_data = pd.Series(aList).value_counts()
print freq_data

df = pd.DataFrame({'A': aList})
d = df['A'].hist().get_figure()
d.savefig('3.7.jpg')
