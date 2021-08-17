import itertools
from permuta.misc import UnionFind
from comb_spec_searcher.bijection import ParallelSpecFinder
from tilings.tilescope import TileScopePack, TileScope
from tilings.strategies import BasicVerificationStrategy


def class_bijections(bases, packs):
    uf = UnionFind(4)
    connections = []
    for packs in itertools.product(packs, packs):
        for idx1, basis1 in enumerate(bases):
            for idx2_offset, basis2 in enumerate(bases[idx1 + 1 :]):
                idx2 = idx1 + idx2_offset + 1
                if uf.find(idx1) == uf.find(idx2):
                    continue
                t1 = TileScope(basis1, packs[0])
                t2 = TileScope(basis2, packs[1])
                if ParallelSpecFinder(t1, t2).find() is not None:
                    uf.unite(idx1, idx2)
                    connections.append((idx1, idx2))
    return len(connections) == len(bases) - 1, connections


bases = [
    "0132_0213_0231_0312_0321_1032_1320_2301_3021",
    "0132_0213_0231_0312_1032_1302_1320_2301_3021",
    "0132_0213_0231_0321_1032_1302_1320_2301_3021",
    "0132_0213_0321_1032_1302_1320_2031_2301_3021",
]
packs = [
    TileScopePack.row_and_col_placements(row_only=True).add_verification(
        BasicVerificationStrategy(), replace=True
    ), 
    # Extend as needed
]
connected, connections = class_bijections(bases, packs)
print(f"Confirmed Wilf class: {connected}")
print(", ".join(f"({a},{b})" for a, b in connections))