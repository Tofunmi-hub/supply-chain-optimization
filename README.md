Supply Chain Transportation Optimization
Overview

This project implements a linear programming transportation model to minimize distribution costs between multiple factories and customer locations.

The objective is to determine the optimal shipment quantities that:

Minimize total transportation cost

Respect factory production capacities

Fully satisfy customer demand

The model is implemented in Python using CVXPy.


Tools

Python

NumPy

CVXPy

(Optional) NetworkX & Matplotlib for visualization


Problem Data
Factory Capacities

| Factory | Capacity |
| ------- | -------- |
| F1      | 100      |
| F2      | 80       |


Customer Demand

| Customer | Demand |
| -------- | ------ |
| C1       | 50     |
| C2       | 70     |
| C3       | 40     |


Mathematical Formulation
Objective

Minimize total transportation cost:

min ∑_f,c cost_fc .x_fc

Subject to

Factory capacity constraints

Customer demand satisfaction

Non-negativity constraints


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

Factory Utilization

F1: 80% (80 / 100)

F2: 100% (80 / 80)

Demand Satisfaction

C1: 50 / 50

C2: 70 / 70

C3: 40 / 40


Business Interpretation

Factory F2 operates at full capacity, indicating that it provides a cost advantage on key transportation routes. Factory F1 retains spare capacity, suggesting flexibility to absorb potential future demand increases.

All customer demand is satisfied at minimum total cost, demonstrating the effectiveness of linear optimization for operational planning and logistics decision-making.
