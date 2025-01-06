import csv

medians = []
for year in range(2019, 2024):
  data = []
  # Read CSV file
  with open(f'Rata-Rata Upah_Gaji, {year}.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for i, row in enumerate(csv_reader):
      # Skip header and average row
      if i > 3 and i < 21:
        row_mean = (int(row[1]) + int(row[2]))//2
        data.append(row_mean)
  
  # Sort the data
  data.sort()

  # Calculate median
  if len(data) % 2 == 0:
    median = (data[len(data)//2] + data[len(data)//2 - 1])/2
  else:
    median = data[len(data)//2]
  medians.append(median)
  median = f"Rp{median:,}".replace(',', '.')
  print(f"Median Upah di Tahun {year}: {median}")

print(medians)
print(f"Rata-rata Median Upah dari 2019-2023: Rp{sum(medians)/len(medians):,.2f}".replace(',', '.'))