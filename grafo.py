import networkx as NX
import matplotlib.pyplot as PLT

G = NX.Graph()

G.add_edge("A", "B", weight=1)
G.add_edge("A", "C", weight=3)

G.add_edge("B", "F", weight=4)
G.add_edge("F", "E", weight=1)
G.add_edge("E", "H", weight=8)

G.add_edge("H", "I", weight=1)
G.add_edge("I", "G", weight=4)

NX.draw(G, with_labels=True, font_color='white', font_weight="bold")



#stampo a video 
PLT.show()