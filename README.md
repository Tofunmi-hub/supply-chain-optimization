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

Optimization Results

Optimal Cost

Total Cost: $820.00

Shipment Plan
| From | To | Units | Cost per Unit |
| ---- | -- | ----- | ------------- |
| F1   | C1 | 50    | $4            |
| F1   | C2 | 19    | $6            |
| F1   | C3 | 11    | $9            |
| F2   | C2 | 51    | $4            |
| F2   | C3 | 29    | $7            |

Network Performance Metrics

Total units shipped: 160

Factory Utilization:

F1: 80% (80 / 100)

F2: 100% (80 / 80)

Demand Satisfaction:

C1: 50 / 50

C2: 70 / 70

C3: 40 / 40
