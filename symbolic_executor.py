from z3 import *

def symbolic_execute(condition, assertion):
    x = Int('x')
    solver = Solver()

    # Branch 1: condition true
    solver.push()
    solver.add(condition(x) == True)
    print(f"[+] Exploring path: {condition.__name__} == True")

    if solver.check() == sat:
        model = solver.model()
        if not assertion(x) == True:
            print("  ❗ Assertion may fail")
        else:
            print("  Assertion holds ✅")
        print(f"  Example: x = {model[x]}")
    solver.pop()

    # Branch 2: condition false
    solver.push()
    solver.add(condition(x) == False)
    print(f"[+] Exploring path: {condition.__name__} == False")

    if solver.check() == sat:
        model = solver.model()
        if not assertion(x) == True:
            print("  ❗ Assertion violated!")
            print(f"  Counterexample: x = {model[x]}")
        else:
            print("  Assertion holds ✅")
        print(f"  Example: x = {model[x]}")
    solver.pop()

# Example conditions & assertions
def cond(x): return x > 0
def assert_rule(x): return x != 0

if __name__ == "__main__":
    symbolic_execute(cond, assert_rule)
