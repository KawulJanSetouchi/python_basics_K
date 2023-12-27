import cirq

# Create a qubit register with 2 qubits
qubits = cirq.LineQubit.range(2)

# Create a quantum circuit
circuit = cirq.Circuit(
    cirq.H(qubits[0]),  # Apply Hadamard gate to the first qubit
    cirq.CNOT(qubits[0], qubits[1])  # Apply CNOT gate between qubit 0 and qubit 1
)

print("Circuit:")
print(circuit)

# Simulate the circuit
simulator = cirq.Simulator()
result = simulator.simulate(circuit)

print("\nSimulation result:")
print(result)