"""
This module implements a quantum teleportation protocol for multiple qubits.
It prepares arbitrary single-qubit states and teleports them sequentially using only 3 qubits
to demonstrate the teleportation process.
It uses the Qiskit library for quantum circuit creation and simulation.

It is designed to teleport multiple independent qubits, each prepared in a specific state,
and measures the results after each teleportation step. 

Note: The teleportation process requires a shared entangled state (Bell pair) between the sender and receiver.

Gebru
Aug 20, 2025

"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import math
import cmath

def prepare_arbitrary_state(qc, qubit, alpha, beta):
    """
    Prepare an arbitrary single-qubit state |psi> = alpha|0> + beta|1>
    """
    theta = 2 * math.acos(abs(alpha))
    phi = cmath.phase(beta) - cmath.phase(alpha)
    qc.u(theta, 0, phi, qubit)
    return qc

def teleport_n_qubits(states, shots=1024):
    """
    Teleport multiple independent qubits sequentially using only 3 qubits.    
    states: list of tuples [(alpha1, beta1), (alpha2, beta2), ...]
    """
    n = len(states)
    qc = QuantumCircuit(3, n)  # 3 qubits, n classical bits

    for i, (alpha, beta) in enumerate(states):
        # Prepare qubit 0 with the arbitrary state
        prepare_arbitrary_state(qc, 0, alpha, beta)

        # Create Bell pair between qubit 1 (Alice) and qubit 2 (Bob)
        qc.h(1)
        qc.cx(1, 2)

        # Bell measurement on Alice's qubits
        qc.cx(0, 1)
        qc.h(0)

        # Conditional operations on Bob's qubit
        qc.cx(1, 2)
        qc.cz(0, 2)

        # Measure Bob's qubit into classical bit i
        qc.measure(2, i)

        # Reset qubits 0 & 1 for the next iteration
        if i < n - 1:
            qc.reset(0)
            qc.reset(1)
            qc.reset(2)  # optional: reset Bob’s qubit if you want a fresh qubit each time

    # Simulate
    sim = AerSimulator()
    job = sim.run(qc, shots=shots)
    result = job.result()
    counts = result.get_counts()
    return counts, qc


# -----------------------------

if __name__ == "__main__":

    # Example: teleport 4 qubits sequentially
    states_to_teleport = [
        (0.6, 0.8),
        (1/math.sqrt(2), 1/math.sqrt(2)),
        (0.8, 0.6),
        (1, 0)
    ]

    # Teleport the states
    counts, qc = teleport_n_qubits(states_to_teleport)
    print("Sequential teleportation measurement counts:", counts)
    plot_histogram(counts)

