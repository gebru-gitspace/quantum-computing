# Quantum Algorithms with Qiskit

Quantum computing represents a **new paradigm of computation** that goes beyond the limits of classical systems.  
Instead of relying solely on **bits (0 or 1)**, quantum computers use **qubits**, which can exist in **superposition** and become **entangled**.  
This allows quantum algorithms to solve certain problems **more efficiently** than any classical method.

This repository explores these ideas by implementing **fundamental quantum algorithms** with **Qiskit**,  
demonstrating how computation can be performed in a fundamentally different way.  

The goal is to provide **clear, modular, and educational implementations** for learners, researchers,  
and enthusiasts who want to experiment with the **building blocks of quantum information processing**.


**Implemented Algorithms**:

1. **Quantum Teleportation**  
2. **Superdense Coding**  
3. **CHSH Game Simulation**  
4. **Deutsch–Jozsa Algorithm**

---

## Overview

This repository demonstrates key **quantum computing concepts** including:

- **Entanglement**  
- **Quantum gates and measurements**  
- **Quantum advantage over classical strategies**  

Each algorithm is implemented **modularly**, allowing easy customization and experimentation.

---

## Algorithms Summary

| Algorithm                | Qubits Used | Input                        | Output                        | Quantum Advantage                  |
|---------------------------|------------|-----------------------------|-------------------------------|-----------------------------------|
| Quantum Teleportation     | 3          | Arbitrary qubit state       | Transmitted qubit recovered    | Transmit qubit without sending it physically |
| Superdense Coding         | 2          | 2 classical bits            | 2 bits decoded using 1 qubit  | Send 2 classical bits via 1 qubit |
| CHSH Game                 | 2          | Random bits x, y            | Measured bits a, b             | Winning probability > 0.75 (classical max) |
| Deutsch–Jozsa Algorithm   | n+1        | Oracle function f(x)        | Constant or Balanced           | Determines with a single query   |

---

## 1. Quantum Teleportation

**Purpose**: Transmit an **arbitrary qubit state** from Alice to Bob using **entanglement and classical communication**.

**Steps**:

1. Create a **Bell pair** between Alice and Bob.  
2. Alice performs **Bell measurement** on her qubits.  
3. Send classical bits to Bob.  
4. Bob applies **conditional gates** to recover the original state.

---

## 2. Superdense Coding

**Purpose**: Send **2 classical bits** by transmitting **1 qubit**, leveraging entanglement.

**Steps**:

1. Alice and Bob share a **Bell pair**.  
2. Alice applies a **gate** based on the 2-bit message.  
3. Alice sends her qubit to Bob.  
4. Bob applies **CNOT + Hadamard** and measures to decode the message.

---

## 3. CHSH Game

**Purpose**: Demonstrate **quantum nonlocality** using a Bell inequality game.

**Steps**:

1. Alice and Bob share a **Bell pair**.  
2. Receive random **inputs x and y**.  
3. Apply **rotation gates** based on inputs.  
4. Measure qubits and check if `a XOR b = x AND y`.  
5. Compute **winning probability** over multiple rounds.

---

## 4. Deutsch–Jozsa Algorithm

**Purpose**: Determine if a Boolean function is **constant or balanced** with a single quantum query.

**Steps**:

1. Initialize qubits including **ancilla qubit**.  
2. Apply **Hadamard gates** to create superposition.  
3. Apply the **oracle** implementing `f(x)`.  
4. Apply **Hadamard gates** again.  
5. Measure qubits to determine **constant vs balanced**.

---

