
"""
# superdense_coding.py
This script implements the Superdense Coding protocol using Qiskit.     
It creates a shared Bell pair, encodes 2 classical bits into Alice's qubit, and decodes it on Bob's qubit.
It uses the Qiskit library for quantum circuit creation and simulation.

Gebru
Aug 19, 2025

"""
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


def create_bell_pair():
    """Create a shared Bell pair between Alice (q0) and Bob (q1)."""
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    return qc

def encode_message(qc, bits):
    """Encode 2 classical bits into Alice's qubit (q0)."""
    if bits == "00":
        pass  # Identity
    elif bits == "01":
        qc.x(0)
    elif bits == "10":
        qc.z(0)
    elif bits == "11":
        qc.x(0)
        qc.z(0)
    else:
        raise ValueError("Bits must be '00', '01', '10', or '11'")
    return qc

def decode_message(qc):
    """Apply decoding to retrieve the 2-bit message on Bob's qubit."""
    qc.cx(0, 1)
    qc.h(0)
    qc.measure_all()
    return qc

def superdense_coding(bits):
    """Full protocol: create Bell pair, encode, decode, and simulate."""
    qc = create_bell_pair()
    qc = encode_message(qc, bits)
    qc = decode_message(qc)

    # Simulate
    sim = AerSimulator()
    tqc = transpile(qc, sim)
    result = sim.run(tqc, shots=1).result()
    counts = result.get_counts()
    return counts, qc


if __name__ == "__main__":
    message = "10"  # Alice wants to send these 2 bits
    counts, qc = superdense_coding(message)
    print(f"Message sent: {message}, Measurement result: {list(counts.keys())[0][::-1]}")
    print(qc.draw())
