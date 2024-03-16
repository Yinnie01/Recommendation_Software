from graph_module import Graph
from growing_trees import bags, dresses, footwear, accessories, tops, skirts, jeans_trousers
# from growing_trees import *

#Drawing the graph based on the different body types available
body_fit = Graph()
body_fit.add_node("Maternity", dresses, accessories, footwear, bags)
body_fit.add_node("Curve and Plus size", dresses, tops, accessories, skirts, footwear, bags)
body_fit.add_node("Petite", dresses, accessories, footwear, bags)
body_fit.add_node("Tall", dresses, jeans_trousers, tops, accessories, footwear, bags)
body_fit.add_node("Hourglass", dresses, accessories, footwear, bags)

# body_fit.print_graph()

