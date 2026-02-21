Supply Chain Transportation Optimization
Overview

This project implements a linear programming transportation model to minimize distribution costs between factories and customers.

Tools

Python

NumPy

CVXPy

Mathematical Model

Minimize:

Total transportation cost

Subject to:

Factory capacity constraints

Customer demand satisfaction

Non-negativity constraints

pip install cvxpy numpy

| Factory | Capacity |
| ------- | -------- |
| F1      | 100      |
| F2      | 80       |
| Customer | Demand |
| -------- | ------ |
| C1       | 50     |
| C2       | 70     |
| C3       | 40     |

==================================================
TRANSPORTATION NETWORK DETAILS
==================================================
Total Cost: $820.00

Shipment Details:
F1 → C1: 50 units @ $4/unit
F1 → C2: 19 units @ $6/unit
F1 → C3: 11 units @ $9/unit
F2 → C1: 0 units @ $5/unit
F2 → C2: 51 units @ $4/unit
F2 → C3: 29 units @ $7/unit

==================================================
NETWORK METRICS
==================================================
Total units shipped: 160
F1 utilization: 80.0% (80/100 units)
F2 utilization: 100.0% (80/80 units)
C1 demand: 50/50 units satisfied
C2 demand: 70/70 units satisfied
C3 demand: 40/40 units satisfied
python supply_chain_model.py
