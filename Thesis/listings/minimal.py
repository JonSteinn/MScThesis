from comb_spec_searcher.bijection import ParallelSpecFinder
from comb_spec_searcher.isomorphism import Bijection
from tilings.strategies import BasicVerificationStrategy
from tilings.tilescope import TileScope, TileScopePack

pack = TileScopePack.row_and_col_placements(row_only=True)
pack = pack.add_verification(BasicVerificationStrategy(), replace=True)
searcher1 = TileScope("231", pack)
searcher2 = TileScope("132", pack)

specs = ParallelSpecFinder(searcher1, searcher2).find()
bijection = Bijection.construct(*specs)
for n in range(6):
    for gp in bijection.domain.generate_objects_of_size(n):
        print(f"{gp} -> {bijection.map(gp)}")