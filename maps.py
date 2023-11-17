import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt

def calculate_shortest_path():
    edges_weight = edges_var.get()
    edges_list = edges_weight.split(',')
    
    for edge in edges_list:
        node1, node2, weight = edge.split()
        G.add_edge(node1, node2, weight=int(weight))
    
    shortest_path = nx.single_source_dijkstra_path(G, source=start_var.get())
    shortest_path_str = ', '.join(f"{node}: {distance}" for node, distance in shortest_path.items())
    result_text.set(f"Shortest paths from {start_var.get()}: {shortest_path_str}")

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

# Create a graph
G = nx.Graph()

# Create the GUI
root = tk.Tk()
root.title("Dijkstra's Shortest Path Algorithm")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

start_label = tk.Label(frame, text="Start Node:")
start_label.grid(row=0, column=0)
start_var = tk.StringVar()
start_entry = tk.Entry(frame, textvariable=start_var)
start_entry.grid(row=0, column=1)

edges_label = tk.Label(frame, text="Edges & Weights (e.g., A B 5, B C 3):")
edges_label.grid(row=1, column=0)
edges_var = tk.StringVar()
edges_entry = tk.Entry(frame, textvariable=edges_var)
edges_entry.grid(row=1, column=1)

calculate_button = tk.Button(frame, text="Calculate", command=calculate_shortest_path)
calculate_button.grid(row=2, columnspan=2)

result_text = tk.StringVar()
result_label = tk.Label(frame, textvariable=result_text)
result_label.grid(row=3, columnspan=2)

root.mainloop()
