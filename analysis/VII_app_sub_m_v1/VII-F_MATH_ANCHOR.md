\[
\max_{x,z,g,y}\; \sum_{d \in D} W_d z_d + \sum_{a \in A} V_a g_a - \lambda \sum_{d<q} L_{d,q}(1-y_{d,q})
\]
\[
\text{s.t. } z_d \le \sum_{i=1}^{N} M_{i,d}x_i,\quad g_a \le \sum_{i=1}^{N} U_{i,a}x_i,\quad \sum_{i=1}^{N}x_i \le B
\]
\[
y_{d,q}\le z_d,\quad y_{d,q}\le z_q,\quad x_i \in \{0,1\},\quad z_d,g_a,y_{d,q}\in\{0,1\}.
\]

This Anchor-B formulation captures VII-F as a cross-domain selection problem over candidate papers, rather than a single deployment scenario objective. The coverage term uses macro-domain and micro-domain evidence weights from VII-F summary artifacts, while the transfer term uses shared-medium overlap strength across macro domains. As a result, the anchor directly operationalizes VII-F synthesis goals: broad, evidence-backed domain coverage with conservative penalty for weak transferability structure.
