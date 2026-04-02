import matplotlib.pyplot as plt


# =============================================================================
#  CRYPTARITHMETIC: TWO + TWO = FOUR
# =============================================================================

def solve_crypto():

    print("=" * 60)
    print("PROBLEM 4 — TWO + TWO = FOUR")
    print("=" * 60)

    letters = ['T', 'W', 'O', 'F', 'U', 'R']
    carries = ['C1', 'C2', 'C3']
    variables = letters + carries

    domains = {l: list(range(10)) for l in letters}
    domains['C1'] = [0, 1]
    domains['C2'] = [0, 1]
    domains['C3'] = [0, 1]

    def backtrack(assignment):

        if len(assignment) == len(variables):
            d = assignment

            if (d['O'] + d['O']) != (d['R'] + 10 * d['C1']):
                return None
            if (d['W'] + d['W'] + d['C1']) != (d['U'] + 10 * d['C2']):
                return None
            if (d['T'] + d['T'] + d['C2']) != (d['O'] + 10 * d['C3']):
                return None
            if d['C3'] != d['F']:
                return None

            if d['T'] == 0 or d['F'] == 0:
                return None

            vals = [d[l] for l in letters]
            if len(set(vals)) != len(vals):
                return None

            return dict(assignment)

        var = next(v for v in variables if v not in assignment)

        for val in domains[var]:
            assignment[var] = val
            d = assignment
            ok = True

            # No leading zero
            if 'T' in d and d['T'] == 0:
                ok = False
            if 'F' in d and d['F'] == 0:
                ok = False

            # Distinct digits
            if ok:
                vals = [d[l] for l in letters if l in d]
                if len(set(vals)) != len(vals):
                    ok = False

            # Column checks
            if ok and all(v in d for v in ['O', 'R', 'C1']):
                if (d['O'] + d['O']) != (d['R'] + 10 * d['C1']):
                    ok = False

            if ok and all(v in d for v in ['W', 'U', 'C1', 'C2']):
                if (d['W'] + d['W'] + d['C1']) != (d['U'] + 10 * d['C2']):
                    ok = False

            if ok and all(v in d for v in ['T', 'O', 'C2', 'C3']):
                if (d['T'] + d['T'] + d['C2']) != (d['O'] + 10 * d['C3']):
                    ok = False

            if ok and all(v in d for v in ['C3', 'F']):
                if d['C3'] != d['F']:
                    ok = False

            if ok:
                result = backtrack(assignment)
                if result:
                    return result

            del assignment[var]

        return None

    solution = backtrack({})

    # ✅ Safe handling
    if solution is None:
        print("❌ No solution found!")
        return None

    d = solution

    TWO = 100*d['T'] + 10*d['W'] + d['O']
    FOUR = 1000*d['F'] + 100*d['O'] + 10*d['U'] + d['R']

    print("\nSolution:")
    for l in letters:
        print(f"{l} = {d[l]}")

    print(f"\nCarries: C1={d['C1']} C2={d['C2']} C3={d['C3']}")
    print(f"\n✔ {TWO} + {TWO} = {FOUR}")

    # =============================================================================
    #  VISUALIZATION
    # =============================================================================

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.axis('off')

    ax.text(0.5, 0.8, f"{TWO}", fontsize=20, ha='center')
    ax.text(0.5, 0.7, f"+ {TWO}", fontsize=20, ha='center')
    ax.text(0.5, 0.6, "------", fontsize=20, ha='center')
    ax.text(0.5, 0.5, f"{FOUR}", fontsize=20, ha='center')

    plt.title("TWO + TWO = FOUR")
    plt.savefig("crypto.png")
    plt.show()

    return solution


# ✅ FIXED MAIN
if __name__ == "__main__":
    solve_crypto()
