import networkx as NX
import matplotlib.pyplot as PLT

dict_adj = {
    "A":[("B",1), ("C", 3), ("D",3)],
    #"B":[("A",1),("F",1)],
    "B":[("F",1)],
    #"C":[("A",3), ("F", 2), ("G",6)],
    "C":[("A",3), ("F", 2), ("G", 6)],
    "F":[("C",3), ("E",1)],
    "E":[("H",8, {'node_color': 'black'}), ("G",2)],
    "H":[("I",1), ("G",4)],
    "G":[("D",8), ("C",6), ("I",1)]
}

G = NX.Graph(year='2009',city='New York')
for nodo in dict_adj: #la chiave (A, B, H) è il nodo
    print(nodo)
    options = {
        'node_color': 'red',
        'node_size': 1000,
        'width': 3,
    }
    G.add_node(nodo,**options)
    lista = dict_adj[nodo]
    for nodoaciacente in lista:
        letteraNodoAdiacente = nodoaciacente[0]
        pesoNodoAdiacente = nodoaciacente[1]
        
        G.add_edge(nodo, letteraNodoAdiacente, weight=pesoNodoAdiacente)



NX.draw(G, with_labels=True, font_color='white', font_weight="bold")

print(NX.shortest_path(G, source="A", target="H", weight="weight"))

#stampo a video 
PLT.show()
