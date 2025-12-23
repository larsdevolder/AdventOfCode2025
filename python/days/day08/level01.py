import numpy as np
import scipy as sp

junctionboxes_list = []
with open("inputs/day08/input.txt", encoding="utf8") as file:
    for line in file:
        vector = list(map(int, line.split(',')))
        junctionboxes_list.append(vector)

junctionboxes = np.array(junctionboxes_list)

distances = np.array(sp.spatial.distance.cdist(junctionboxes, junctionboxes, "euclidean"))

pairs_used = set()
networks = [{tuple(junction)} for junction in junctionboxes]
CONNECTIONS = 1000
wires = 0
for idx in np.argsort(distances, axis=None)[::]:
    if wires == CONNECTIONS:
        break
    row, col = np.unravel_index(idx, distances.shape)
    junction1 = tuple(junctionboxes[row])
    junction2 = tuple(junctionboxes[col])
    if junction1 == junction2:
        continue
    if frozenset((junction1, junction2)) in pairs_used:
        continue
    pairs_used.add(frozenset((junction1, junction2)))
    same_network = False
    network1 = set()
    network2 = set()
    wires += 1
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

lengths = sorted([len(network) for network in networks], reverse=True)
print(lengths[0] * lengths[1] * lengths[2])
