import cirq
import cirq_google


a =cirq.NamedQubit('a')
b =cirq.NamedQubit('b')
c =cirq.NamedQubit('c')
d =cirq.NamedQubit('d')

ops =[cirq.H(a), cirq.H(b), cirq.CNOT(b,c), cirq.H(b), cirq.H(d)]
circuit =cirq.Circuit(ops)
print(circuit)

q0, q1,q2 =cirq.LineQubit.range(3)
opss =[
    cirq.X(q0),
    cirq.Y(q1),
    cirq.Z(q2),
    cirq.CZ(q0,q1),
    cirq.CNOT(q1,q2),
    cirq.H(q0),
    cirq.T(q1),
    cirq.S(q2),
    cirq.CCZ(q0,q1,q2),
    cirq.SWAP(q0,q1),
    cirq.CSWAP(q0,q1,q2),
    cirq.CCX(q0,q1,q2),
    cirq.ISWAP(q0,q1),
]

# print(cirq.Circuit(opss))
#
# for i, moment in enumerate(circuit):
#     print("Moment {}: {}".format(i, moment))
#
#
# for i in enumerate(circuit):
#     print(i)
#


circuit=cirq.Circuit()
circuit.append([cirq.CNOT(a,b)])
circuit.append([cirq.H(c), cirq.H(b),cirq.H(b), cirq.H(a)],)
#print(circuit)

circuit.insert(1,[cirq.Z(b), cirq.Z(c)])

#print(circuit)
