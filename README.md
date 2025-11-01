# Mini Symbolic Execution Engine (Python + Z3)

This project is a simple symbolic execution engine built using Python and Z3.  
It symbolically explores execution paths in small programs and detects bugs such as assertion failures.

###  Features
- Symbolic variables using Z3
- Path constraint collection
- Branch exploration (true/false)
- Assertion violation detection

###  Structure
- `symbolic_executor.py` — core symbolic executor
- `examples/` — small sample programs to analyze

###  Example Output
[+] Exploring path: x > 0
Constraints: x > 0
Assertion holds 

[+] Exploring path: not(x > 0)
Constraints: x <= 0
❗ Assertion violated! Counterexample: x = 0

### 🧠 Learning Goal
To understand fundamental concepts behind:
- Symbolic execution
- SMT solving
- Automated program analysis

Inspired by research in program verification & formal methods.

### ⚙️ Requirements
pip install z3-solver

### 📌 Future Work
- Support loops (bounding)
- Support more operations
- Command-line interface

### 👤 Author
**Yuva Akhil Pattela**  
Prospective MSCS student interested in PL & Program Verification
