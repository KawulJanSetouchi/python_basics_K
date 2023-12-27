import cirq

a =cirq.NamedQubit('a')
b =cirq.NamedQubit('b')
def basic_circuit(measure=True):
    yield cirq.H(a)
    yield cirq.H(b)
    if measure:
        yield  cirq.measure(a,b)

circuit =t=cirq.Circuit(basic_circuit())
print(circuit)