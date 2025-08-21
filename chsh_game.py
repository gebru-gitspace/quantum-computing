"""
CHSH Game Simulation using Qiskit
This script simulates the CHSH game, demonstrating quantum entanglement and non-locality.
It uses Qiskit for quantum circuit creation and simulation.

Author: Gebru
Date: Aug 22, 2025
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import numpy as np
from itertools import product


def create_chsh_circuit(x, y):
    """
    Create a CHSH circuit for a given input pair (x, y).
    
    Parameters:
        x (int): Alice's input (0 or 1)
        y (int): Bob's input (0 or 1)
    
    Returns:
        QuantumCircuit: CHSH quantum circuit with measurements
    """
    qc = QuantumCircuit(2, 2)
    
    # Create Bell pair
    qc.h(0)
    qc.cx(0, 1)
    
    # Rotate based on inputs
    qc.ry(0 if x == 0 else np.pi/4, 0)  # Alice
    qc.ry(np.pi/8 if y == 0 else -np.pi/8, 1)  # Bob
    
    # Measure both qubits
    qc.measure([0, 1], [0, 1])
    
    return qc

def simulate_chsh(shots=1024):
    """
    Simulate CHSH game for all input combinations.
    
    Returns:
        dict: Measurement counts for each (x, y) input
    """
    sim = AerSimulator()
    results = {}
    
    for x, y in product([0, 1], repeat=2):
        qc = create_chsh_circuit(x, y)
        tqc = transpile(qc, sim)
        job = sim.run(tqc, shots=shots)
        counts = job.result().get_counts()
        results[(x, y)] = counts
    
    return results

def compute_win_probability(results):
    """
    Compute the CHSH game winning probability from measurement results.
    
    Returns:
        float: Winning probability
    """
    wins, total = 0, 0
    for (x, y), counts in results.items():
        for outcome, n in counts.items():
            a, b = int(outcome[1]), int(outcome[0])  # Qiskit bit order
            if (a ^ b) == (x & y):
                wins += n
            total += n
    return wins / total

def print_results(results):
    """
    Print measurement counts for each input combination.
    """
    for (x, y), counts in results.items():
        print(f"Inputs (x={x}, y={y}): {counts}")



if __name__ == "__main__":
    shots = 1024
    results = simulate_chsh(shots)
    
    print("CHSH Game Simulation Results:\n")
    print_results(results)
    
    win_prob = compute_win_probability(results)
    print(f"\nCHSH Winning Probability: {win_prob:.3f}")

    # Example: choose inputs x=0, y=0 to draw just the circuit
    x, y = 0, 0
    qc = create_chsh_circuit(x, y)

    # Print the circuit as text
    print(qc.draw())

