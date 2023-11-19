import qrcode
import pandas as pd

dataframe = pd.read_excel("Compiler/Output/EventOverview.xlsx")
# dataframe.drop()
csv = dataframe.to_csv()
print(len(csv))
img = qrcode.make("csv123456789123456789112345678912345678909")





# for i in range(500):
#     print(i)
#     dictionary[i] = 1
#     img = qrcode.make(dictionary)

img.save('Compiler/Output/TestQR.png')

# # f.close()

