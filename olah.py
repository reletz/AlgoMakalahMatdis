import numpy as np

#Z-Score Normalization
def zscore(data):
  mean = np.mean(data)
  std = np.std(data)
  return (data - mean) / std

data = {
  "Inflasi": [2.72, 1.68, 1.87, 5.51, 2.61],
  "PDRB": [59107.89, 57812.48, 62237.89, 71043.44 , 74964.70],
  "PDB": [122.4, 120.1, 129.5, 137.4, 139.2],
  "TPT": [5.28, 7.07, 6.49, 5.86, 5.32],  
  "Median Upah": [3362435, 3317490, 3140168, 3496222, 3613930]
}
 

# Normalisasi Data
normalized_data = {
  "Inflasi": zscore(data["Inflasi"]),
  "PDRB": zscore(data["PDRB"]),
  "PDB": zscore(data["PDB"]),
  "TPT": zscore(data["TPT"]),
  "Median Upah": zscore(data["Median Upah"])
}

# Convert to numpy array
data_matrix = np.array(list(normalized_data.values()))

# Print correlation matrix
switcher = {
  0: "Inflasi\t\t",
  1: "PDRB\t\t",
  2: "PDB\t\t",
  3: "TPT\t\t",
  4: "Median Upah\t"
}

print("Data Normalisasi Z-Score:")
print("\t\t", end=f"{switcher[0]}{switcher[1]}{switcher[2]}{switcher[3]}{switcher[4]}\n")
for i in range (len(data_matrix)):
  print(2019+i, end="\t\t")
  for j in range (len(data_matrix[i])):
    print(f"{data_matrix[j][i]:.3f}", end="\t\t")
  print()

# Calculate correlation matrix
correlation_matrix = np.corrcoef(data_matrix)

print("Matriks Korelasi Pearson:")
print("\t\t", end=f"{switcher[0]}{switcher[1]}{switcher[2]}{switcher[3]}{switcher[4]}\n")
for i in range (len(correlation_matrix)):
  print(f"{switcher[i]}", end="")
  for j in range (len(correlation_matrix[i])):
    print(f"{correlation_matrix[i][j]:.3f}", end="\t\t")
  print()


print("Matriks Bobot")
print("[", end="")
for i in range (len(correlation_matrix)):
  print("[", end="")
  for j in range (len(correlation_matrix[i])):
    print(f"{(1 - abs(correlation_matrix[i][j])):.3f}", end=f"{"," if j < len(correlation_matrix[i])-1 else ""}")
  print("]", end=f"{",\n" if i < len(correlation_matrix)-1 else ""}")
print("]")