# -*- coding: utf-8 -*-
"""
Created on Mon May 11 12:53:41 2020

@author: wiifr
"""
get_ipython().run_line_magic('matplotlib', 'inline')
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
provider = IBMQ.load_account()


circuit = QuantumCircuit(2,2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure([0,1], [0,1])

simulator = Aer.get_backend('qasm_simulator')
job = execute(circuit, simulator, shots=1024)

result = job.result()
counts = result.get_counts(circuit)
circuit.draw()

plot_histogram(counts)





