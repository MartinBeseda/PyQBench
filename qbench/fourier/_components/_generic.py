"""Generic implementation of Fourier _components not tailored for any specific device.

Note that using _components from this module on physical device typically requires compilation.

For detailed description of functions in this module refer to the documentation of
FourierComponents class.
"""

import numpy as np
from qiskit.circuit import Instruction, Parameter, QuantumCircuit


def state_preparation() -> Instruction:
    circuit = QuantumCircuit(2, name="state-prep")
    circuit.h(0)
    circuit.cx(0, 1)
    return circuit.to_instruction()


def u_dag(phi: float | Parameter) -> Instruction:
    circuit = QuantumCircuit(1, name="U-dag")
    circuit.h(0)
    circuit.p(-phi, 0)
    circuit.h(0)
    return circuit.to_instruction()


def v0_dag(phi: float | Parameter) -> Instruction:
    circuit = QuantumCircuit(1, name="v0-dag")
    circuit.rz(-np.pi / 2, 0)
    circuit.ry(-(phi + np.pi) / 2, 0)
    return circuit.to_instruction()


def v1_dag(phi: float | Parameter) -> Instruction:
    circuit = QuantumCircuit(1, name="v1-dag")
    circuit.rz(-np.pi / 2, 0)
    circuit.ry(-(phi + np.pi) / 2, 0)
    circuit.rx(-np.pi, 0)
    return circuit.to_instruction()


def v0_v1_direct_sum(phi: float | Parameter) -> Instruction:
    circuit = QuantumCircuit(2, name="v0 ⊕ v1-dag")
    circuit.p(np.pi, 0)
    circuit.append(v0_dag(phi), [1])
    circuit.cx(0, 1)
    return circuit.decompose(["v0-dag"]).to_instruction()
