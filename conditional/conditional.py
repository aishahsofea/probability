from numpy import transpose
from itertools import permutations 

# usage:
# ways to arrange n coins - coin: {H, T}
# ways to arange n dice - die: {1, 2, 3, 4, 5, 6}


class Conditional():

    def __init__(self, elementary_events, is_independent=True):
        self.elementary_events = elementary_events
        self.is_independent = is_independent

    def arrange_items(self, total_items):
        chunk_size = len(self.elementary_events) ** (total_items - 1)
        arrangements = []
        multiple = 1
        perm = (permutations(self.elementary_events, total_items)) 

        if not self.is_independent:
            return [p for p in perm]
        else:
            while chunk_size >= 1:
                arrangement = []
                for e in self.elementary_events:
                    for i in range(chunk_size):
                        arrangement.append(str(e))

                arrangements.append(arrangement * multiple)
                multiple *= len(self.elementary_events)
                chunk_size //= len(self.elementary_events)

            return transpose(arrangements)
