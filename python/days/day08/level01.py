import numpy as np
import scipy as sp
from collections import Counter

junctionboxes_list = []
with open("inputs/day08/example.txt", encoding="utf8") as file:
    for line in file:
        vector = list(map(int, line.split(',')))
        junctionboxes_list.append(vector)

junctionboxes = np.array(junctionboxes_list)

distances = np.array(sp.spatial.distance.cdist(junctionboxes, junctionboxes, "euclidean"))

networks = [{tuple(junction)} for junction in junctionboxes]
CONNECTIONS = 9
for idx in np.argsort(distances, axis=None)[::]:
    lengths = [len(network) - 1 for network in networks]
    if sum(lengths) == CONNECTIONS:
        break
    row, col = np.unravel_index(idx, distances.shape)
    junction1 = tuple(junctionboxes[row])
    junction2 = tuple(junctionboxes[col])
    if junction1 == junction2:
        continue
    same_network = False
    network1 = set()
    network2 = set()
    for network in networks:
        if junction1 in network and junction2 in network:
            same_network = True
            break
        if junction1 in network:
            network1 = network
        if junction2 in network:
            network2 = network
    if same_network:
        continue
    network1.update(network2)
    networks.remove(network2)

print(lengths)
