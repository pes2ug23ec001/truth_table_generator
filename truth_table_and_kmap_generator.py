import itertools

def gray_code(n):
    if n == 0:
        return ['']
    smaller = gray_code(n - 1)
    return ['0' + code for code in smaller] + ['1' + code for code in reversed(smaller)]

# --- reuse your existing truth table logic ---
var_input = input("Enter input variables: ")
variables = var_input.split()
expression = input("Enter the Boolean expression: ")

n = len(variables)

# build a lookup table: {(0,1,1,0): output, ...}
lookup = {}
for combo in itertools.product([0, 1], repeat=n):
    values = dict(zip(variables, combo))
    result = int(eval(expression, {}, values))
    lookup[combo] = result

# --- split variables into row-group and column-group ---
half = n // 2
row_vars = variables[:n - half]   # gets the larger half if odd
col_vars = variables[n - half:]

row_codes = gray_code(len(row_vars))
col_codes = gray_code(len(col_vars))

# --- print the K-map ---
print("\nK-map:")
print("      " + " ".join(col_codes) + "   <- " + "".join(col_vars))
for r in row_codes:
    row_values = [int(bit) for bit in r]
    row_output = []
    for c in col_codes:
        col_values = [int(bit) for bit in c]
        full_combo = tuple(row_values + col_values)
        row_output.append(str(lookup[full_combo]))
    print(r + " | " + "  ".join(row_output))
print("^\n" + "".join(row_vars))