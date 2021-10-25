# Aca colocaran el cod que iran avanzando
import csv
import numpy as np
import matplotlib.pyplot as plt
def read_csv(filename):
  csv_file = list()
  with open(filename) as File:
    reader = csv.reader(File, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        if row[0] != 'x':
          row[0], row[1] = int(row[0]), int(row[1])
          csv_file.append(row)
  csv_file.sort(key = lambda x: (x[0], x[1]))
  return csv_file
almacenes = read_csv("almacenes.csv")
casas = read_csv("casas.csv")
x, y = np.array(almacenes).T
x2, y2 = np.array(casas).T
plt.figure(figsize=(15, 15))
plt.scatter(x,y, 2, c="red")
plt.scatter(x2,y2, 2, c="blue")
plt.show()

def write_csv(headers, fields, filename):
  with open(filename, 'w') as f:   
    write = csv.writer(f)
    if headers != None: write.writerow(headers)
    write.writerows(fields)

for i, _ in enumerate(almacenes):
  almacenes[i].append("A")
for i, _ in enumerate(casas):
  casas[i].append("C")
city = list()
city.extend(almacenes)
city.extend(casas)
city.sort(key = lambda x: (x[0], x[1]))
write_csv(['x', 'y', 'type'], city, 'city.csv')

graph = [[] for _ in city]
for i, _ in enumerate(city):
  for j, _ in enumerate(city):
    if i == j: continue
    if city[i][0] == city[j][0] or city[i][1] == city[j][1]: graph[i].append(j)
write_csv(None, graph, 'graph.csv')
