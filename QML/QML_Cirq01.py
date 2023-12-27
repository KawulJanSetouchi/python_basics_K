import cirq

a =cirq.NamedQubit('a')
b =cirq.NamedQubit('b')
c =cirq.NamedQubit('c')
circuit =cirq.Circuit([cirq.CZ(a,b), cirq.H(a)])
circuit.append([cirq.H(b), cirq.CZ(b,c), cirq.H(a), cirq.H(a)],
               strategy=cirq.InsertStrategy.NEW_THEN_INLINE)
print(circuit)