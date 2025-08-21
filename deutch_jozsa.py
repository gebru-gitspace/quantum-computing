"""
This is Deutsch–Jozsa algorithm implementation in Qiskit.
This code defines oracles for constant and balanced functions,  
and implements the Deutsch–Jozsa algorithm to determine if a function is constant or balanced.
It uses the Qiskit library for quantum circuit creation and simulation.
        
Gebru
Aug 18, 2025

"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


def constant_oracle(n: int):
    """Deutsch–Jozsa constant oracle (f(x)=0)."""
    qc = QuantumCircuit(n + 1)
    # Does nothing -> always returns 0
    return qc.to_gate(label="Const")

def balanced_oracle(n: int):
    """Deutsch–Jozsa balanced oracle: f(x) = x0 XOR x1 ... (simple version)."""
    qc = QuantumCircuit(n + 1)
    for i in range(n):
        qc.cx(i, n)  # parity function
    return qc.to_gate(label="Bal")

# ---------------- Deutsch–Jozsa core ----------------

def deutsch_jozsa(oracle, n: int, shots: int = 1):
    """
    Run Deutsch–Jozsa algorithm with given oracle.
    n = number of input qubits
    Returns 'constant' or 'balanced'.
    """
    qc = QuantumCircuit(n + 1, n)

    # 1. Prepare ancilla |1>
    qc.x(n)

    # 2. Hadamard on all qubits
    qc.h(range(n + 1))

    # 3. Apply oracle
    qc.append(oracle, range(n + 1))

    # 4. Hadamard on input register
    qc.h(range(n))

    # 5. Measure input register
    qc.measure(range(n), range(n))

    # --- Simulation ---
    sim = AerSimulator()
    tqc = transpile(qc, sim)
    result = sim.run(tqc, shots=shots).result()
    counts = result.get_counts()

    # Decision rule
    return "constant" if "0"*n in counts else "balanced", counts, qc


if __name__ == "__main__":
    n = 4  # number of input qubits

    # Test constant oracle
    const_oracle = constant_oracle(n)
    decision_c, counts_c, qc_c = deutsch_jozsa(const_oracle, n)
    print("Constant oracle result:", decision_c, counts_c)
    print(qc_c.draw())
    
    # Test balanced oracle
    bal_oracle = balanced_oracle(n)
    decision_b, counts_b, qc_b = deutsch_jozsa(bal_oracle, n)
    print("Balanced oracle result:", decision_b, counts_b)
    print(qc_b.draw())

