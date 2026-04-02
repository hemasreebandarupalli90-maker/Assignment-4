import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx


# =============================================================================
#  GENERIC CSP FRAMEWORK
# =============================================================================

class CSP:
    def __init__(self, variables, domains, neighbors, constraint):
        self.variables = list(variables)
        self.domains = {v: list(domains[v]) for v in variables}
        self.neighbors = neighbors
        self.constraint = constraint

    def backtracking_search(self):
        return self._backtrack({})

    def _backtrack(self, assignment):
        if len(assignment) == len(self.variables):
            return dict(assignment)

        var = self._mrv(assignment)

        for value in self.domains[var]:
            if self._consistent(var, value, assignment):
                assignment[var] = value

                # Save domain snapshot
                snapshot = {v: list(self.domains[v]) for v in self.variables}

                if self._forward_check(var, value, assignment):
                    result = self._backtrack(assignment)
                    if result is not None:
                        return result

                # Restore domains
                self.domains = snapshot
                del assignment[var]

        return None

    def _mrv(self, assignment):
        unassigned = [v for v in self.variables if v not in assignment]
        return min(unassigned, key=lambda v: len(self.domains[v]))

    def _consistent(self, var, value, assignment):
        for nb in self.neighbors.get(var, []):
            if nb in assignment:
                if not self.constraint(var, value, nb, assignment[nb]):
                    return False
        return True

    def _forward_check(self, var, value, assignment):
        for nb in self.neighbors.get(var, []):
            if nb not in assignment:
                new_domain = [
                    v for v in self.domains[nb]
                    if self.constraint(nb, v, var, value)
                ]

                if not new_domain:
                    return False

                self.domains[nb] = new_domain
        return True


def ne_constraint(A, a, B, b):
    return a != b


# =============================================================================
#  AUSTRALIA MAP COLORING
# =============================================================================

def solve_australia():

    variables = ['WA', 'NT', 'Q', 'SA', 'NSW', 'V', 'T']
    colors = ['Red', 'Green', 'Blue']
    domains = {v: colors[:] for v in variables}

    neighbors = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'Q', 'SA'],
        'Q': ['NT', 'SA', 'NSW'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW'],
        'T': []
    }

    csp = CSP(variables, domains, neighbors, ne_constraint)
    solution = csp.backtracking_search()

    if solution is None:
        print("No solution found!")
        return

    # Optional: assign Tasmania
    solution['T'] = 'Green'

    print("\nSolution:")
    for v in variables:
        print(f"{v} → {solution[v]}")

    # Graph Visualization
    HEX = {'Red': '#e74c3c', 'Green': '#27ae60', 'Blue': '#2980b9'}

    pos = {
        'WA': (0, 2),
        'NT': (2, 3),
        'Q': (4, 3),
        'SA': (2.5, 2),
        'NSW': (4, 2),
        'V': (3.5, 1),
        'T': (3.5, 0)
    }

    G = nx.Graph()
    G.add_nodes_from(variables)

    for v in neighbors:
        for nb in neighbors[v]:
            G.add_edge(v, nb)

    node_colors = [HEX[solution[v]] for v in G.nodes()]

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True,
            node_color=node_colors,
            node_size=2000,
            font_color='white')

    legend = [mpatches.Patch(color=HEX[c], label=c) for c in colors]
    plt.legend(handles=legend)

    plt.title("Australia Map Coloring (CSP)")
    plt.savefig("australia_map.png")
    plt.show()


if __name__ == "__main__":
    solve_australia()
