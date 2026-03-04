Supply Chain Transportation Optimization
Overview

This project implements a linear programming transportation model to minimize distribution costs between multiple factories and customer locations.

The objective is to determine the optimal shipment quantities that:

- Minimize total transportation cost

- Respect factory production capacities

- Fully satisfy customer demand

- The model is implemented in Python using CVXPy.


Tools:

- Python

- NumPy

- CVXPy

- (Optional) NetworkX & Matplotlib for visualization


Project Structure

- supply_chain_model.py  → optimization model & visualization
- requirements.txt       → dependencies

Model Assumptions

- Transportation cost is linear per unit.
- All demand must be satisfied.
- Production capacities are fixed.
- No storage or intermediate warehouses are included.


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

Subject to:

- Factory capacity constraints

- Customer demand satisfaction

- Non-negativity constraints


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


Business Interpretation:

- Factory F2 operates at full capacity, indicating that it provides a cost advantage on key transportation routes. Factory F1 retains spare capacity, suggesting flexibility to absorb potential future demand increases.

- All customer demand is satisfied at minimum total cost, demonstrating the effectiveness of linear optimization for operational planning and logistics decision-making.

Real-World Relevance

Transportation optimization models like this form the foundation of advanced route planning and logistics systems used in industries such as energy distribution and supply chain management. Extensions of this model can incorporate traffic data, fuel consumption metrics, and environmental impact constraints to support sustainable operational decision-making.


Fuel Cost Sensitivity Analysis

To simulate real-world fuel price fluctuations, transportation costs were scaled by multipliers ranging from 1.0 to 1.3. As fuel cost increases, total operational cost rises proportionally, illustrating the impact of energy price volatility on logistics planning.


Scenario Analysis: Fuel Price Sensitivity

To evaluate the robustness of the transportation network under energy price volatility, a fuel cost sensitivity analysis was conducted.

Fuel-related transportation costs were increased using a multiplier applied heterogeneously across factories:

- F1 assumed lower fuel exposure (0.8)
- F2 assumed higher fuel exposure (1.2)

The fuel multiplier was varied from 1.0 to 1.3.
Results Summary
| Fuel Multiplier | Total Cost ($) |
| --------------- | -------------- |
| 1.0             | 820            |
| 1.1             | 820            |
| 1.2             | 860            |
| 1.3             | ~970           |

Interpretation of Results
1. Does routing change when fuel rises? No.

For small fuel increases (1.0 → 1.1), the routing structure remains unchanged.

This indicates:

The baseline solution is structurally stable.

Minor fuel fluctuations do not justify rerouting.

However, as fuel costs increase further (≥ 1.2), total cost rises significantly, showing growing economic pressure on the network. The system becomes increasingly sensitive to cost shocks.

Because F2 operates at full capacity in the baseline solution, the model has limited flexibility to drastically reroute flows without structural changes (e.g., capacity expansion or new facilities).

2. Does F1 utilization increase? No.

F1 utilization remains at 80% (80 / 100 units) across the tested scenarios.

This indicates:

F1 is already serving the lowest-cost demand allocations available to it.

Additional rerouting toward F1 is not economically optimal under current cost differentials.

Spare capacity at F1 exists but is not competitive enough to absorb more demand.

This reveals a structural inefficiency: unused capacity does not automatically imply economic flexibility.

3. Does F2 become too expensive? Progressively, yes.

Because F2 has higher fuel exposure:

- Its effective transportation costs increase more rapidly.
- The total network cost rises non-linearly as fuel multiplier increases.
- At higher fuel multipliers (1.3), the system becomes significantly more expensive (~18% increase over baseline).

This indicates vulnerability to fuel price volatility and suggests that:
- The network is sensitive to energy shocks.
- Strategic mitigation may require capacity expansion at F1, cost restructuring, alternative routing strategies, or infrastructure redesign.

This sensitivity analysis demonstrates that:
- The network is stable under minor fuel variations.
- It becomes increasingly cost-sensitive under sustained fuel increases.
- Structural capacity constraints limit rerouting flexibility.
- Energy price volatility materially impacts total operational cost.
This type of analysis is essential in energy-intensive supply chains and logistics networks, where fuel prices can significantly affect operational resilience.


Extensions

- Add warehouse layer (multi-echelon network)
- Introduce variable transportation scenarios
- Consider demand uncertainty

