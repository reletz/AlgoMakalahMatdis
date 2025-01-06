import numpy as np

def prims_algorithm(adjacency_matrix):
  num_nodes = len(adjacency_matrix)
  
  # Cari simpul awal dengan sisi keluar berbobot minimum
  min_edge = (None, None, float('inf'))  # Format Tuple: (simpul1, simpul2, bobot)
  for i in range(num_nodes):
    for j in range(num_nodes):
      if adjacency_matrix[i][j] > 0 and adjacency_matrix[i][j] < min_edge[2]:
        min_edge = (i, j, adjacency_matrix[i][j])

  start_node = min_edge[0]  # Pilih simpul awal
  selected_nodes = [False] * num_nodes
  selected_nodes[start_node] = True  # Tandai simpul awal sebagai sudah dipilih

  mst_edges = []  # Menyimpan sisi dalam MST
  total_cost = 0  # Menyimpan total bobot MST

  for _ in range(num_nodes - 1):  # MST memiliki (n_simpul-1) sisi
    min_edge = (None, None, float('inf'))  # Reset edge terbaik

    for i in range(num_nodes):
      if selected_nodes[i]:  # Simpul i sudah dalam MST
        for j in range(num_nodes):
          if not selected_nodes[j] and adjacency_matrix[i][j] > 0:
            if adjacency_matrix[i][j] < min_edge[2]:
              min_edge = (i, j, adjacency_matrix[i][j])

    # Tambahkan sisi dengan bobot terkecil ke MST
    mst_edges.append((min_edge[0], min_edge[1], min_edge[2]))
    total_cost += min_edge[2]
    selected_nodes[min_edge[1]] = True  # Tandai simpul j sebagai telah dipilih

    # Ulangi hingga semua simpul telah dipilih
  return mst_edges, total_cost

# Contoh input adjacency matrix
adjacency_matrix = np.array([
  [0.000,0.452,0.422,0.611,0.493],
  [0.452,0.000,0.025,0.469,0.222],
  [0.422,0.025,0.000,0.523,0.371],
  [0.611,0.469,0.523,0.000,0.376],
  [0.493,0.222,0.371,0.376,0.000]
])

map_nodes = {
  0: 'I',
  1: 'R',
  2: 'P',
  3: 'T',
  4: 'M'
}

mst_edges, total_cost = prims_algorithm(adjacency_matrix)
for edge in mst_edges:
  print(f"{map_nodes[edge[0]]} - {map_nodes[edge[1]]} ({edge[2]:.3f})")
print("Total Cost of MST:", total_cost)
