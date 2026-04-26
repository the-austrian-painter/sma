# Algorithm: Structure-Based Social Media Analytics (Network Analysis)

## Experiment 5 — Structure Based SMA

---

### Part A: Basic Graph Creation & Centrality Measures

```
1. START

2. Import required libraries:
      networkx, matplotlib

3. CREATE GRAPH:
      a. Initialize empty undirected Graph G
      b. Add nodes: ['A', 'B', 'C', 'D', 'E']
      c. Add edges representing user interactions:
         - (A, B), (A, C), (B, D), (C, D), (D, E)

4. COMPUTE CENTRALITY MEASURES:
      a. Degree Centrality       → nx.degree_centrality(G)
      b. Betweenness Centrality  → nx.betweenness_centrality(G)
      c. Closeness Centrality    → nx.closeness_centrality(G)
      d. Eigenvector Centrality  → nx.eigenvector_centrality(G)

5. VISUALIZE NETWORK:
      a. Draw graph with node labels using nx.draw()
      b. Display using matplotlib

6. END (Part A)
```

---

### Part B: Complex Network with Hub-and-Spoke + Dense Cluster

```
7. CREATE COMPLEX GRAPH:
      a. Initialize empty undirected Graph G

      b. LEFT CLUSTER (Hub P — Star topology):
         - Hub node: P
         - Spoke nodes: J, G, K, L, N, M, I, H
         - Add edges: (P, J), (P, G), (P, K), (P, L),
                      (P, N), (P, M), (P, I), (P, H)
         - Add chain edges: (J, K), (K, L), (L, M)

      c. BRIDGE:
         - Add edge: (P, F)

      d. RIGHT CLUSTER (Dense group around F):
         - F connects to: Q, O, C, A, B
         - Q connects to: O, C, D, E
         - O connects to: C
         - C connects to: D, B
         - D connects to: A, E, B
         - A connects to: E
         - E connects to: B

8. DEFINE NODE POSITIONS:
      a. Manually assign (x, y) coordinates for each node
      b. Store in pos dictionary

9. DRAW NETWORK:
      a. Draw nodes (light gray, size=1600, black border)
      b. Draw edges (black, width=1.5)
      c. Draw labels (font_size=12)
      d. Disable axes, add margins

10. ANALYZE NETWORK:

      10a. COMPUTE DEGREE OF EACH NODE:
         - G.degree() → dictionary of {node: degree}
         - Print each node and its degree

      10b. COMPUTE DEGREE CENTRALITY:
         - nx.degree_centrality(G)
         - Sort by score descending
         - Print node and score

      10c. COMPUTE BETWEENNESS CENTRALITY:
         - nx.betweenness_centrality(G)
         - Sort by score descending
         - Print node and score

      10d. IDENTIFY TOP 3 INFLUENTIAL USERS:
         - Top 3 by Degree (Popularity)
         - Top 3 by Betweenness (Control/Bridge)

      10e. FIND CLIQUES:
         - nx.find_cliques(G)
         - Print all maximal cliques

11. END (Part B)
```

---

### Part C: Netflix vs JioHotstar Network Comparison

```
12. DEFINE CENTRALITY CALCULATION FUNCTION:
      INPUT: Graph G, title string
      a. Compute 4 centrality measures:
         - Degree Centrality
         - Eigenvector Centrality (max_iter=1000)
         - Betweenness Centrality
         - Closeness Centrality
      b. Create DataFrame with all 4 measures
      c. Print centrality values table
      d. Print top 3 users by Eigenvector centrality
      RETURN: DataFrame

13. BUILD NETFLIX NETWORK:
      a. Nodes: N1, N2, N3, N4, N5, N6
      b. Edges:
         (N1,N2), (N1,N3), (N2,N3),
         (N2,N4), (N3,N5), (N4,N5),
         (N5,N6), (N4,N6)
      c. Compute centralities → df_netflix
      d. Visualize (spring_layout, lightgreen nodes)

14. BUILD JIOHOTSTAR NETWORK:
      a. Nodes: J1, J2, J3, J4, J5, J6
      b. Edges:
         (J1,J2), (J1,J3), (J2,J3),
         (J3,J4), (J4,J5), (J5,J6),
         (J2,J6), (J1,J5)
      c. Compute centralities → df_jiohotstar
      d. Visualize (spring_layout, orange nodes)

15. BUILD COMBINED NETWORK:
      a. Include all Netflix and JioHotstar nodes
      b. Include all Netflix and JioHotstar edges
      c. Add bridge users: B1, B2
      d. Add bridge edges:
         - (B1, N2), (B1, J3)  — bridges Netflix cluster 1 to JioHotstar
         - (B2, N5), (B2, J4)  — bridges Netflix cluster 2 to JioHotstar
      e. Compute centralities → df_combined
      f. Visualize (spring_layout, lightblue nodes)

16. END (Part C)
```

---

### Centrality Measures Explained

| Measure            | Formula Concept                      | Interpretation                         |
|--------------------|--------------------------------------|----------------------------------------|
| **Degree**         | `connections / (n-1)`               | How many direct connections a node has |
| **Eigenvector**    | Proportional to sum of neighbor scores | Influence based on neighbor influence |
| **Betweenness**    | Fraction of shortest paths through node | Control over information flow       |
| **Closeness**      | Reciprocal of sum of shortest paths  | How quickly a node reaches all others  |

### Key Components

| Component                | Description                                            |
|--------------------------|--------------------------------------------------------|
| **Library**              | NetworkX for graph creation and analysis               |
| **Visualization**        | Matplotlib + NetworkX drawing functions                |
| **Layout Algorithm**     | Spring layout (force-directed)                         |
| **Clique Detection**     | nx.find_cliques() — Bron-Kerbosch algorithm            |
| **Bridge Analysis**      | Manual bridge edges connecting separate clusters       |

### Network Comparison Summary

```
Netflix Network          JioHotstar Network         Combined Network
┌──────────────┐         ┌──────────────┐          ┌─────────────────────────┐
│  N1──N2      │         │  J1──J2      │          │  N1──N2    J1──J2       │
│  │╲  │       │         │  │╲  │       │          │  │╲  │    │╲  │        │
│  N3  N4      │         │  J3  J6      │          │  N3  N4──J3  J6        │
│  │   │       │         │  │   │       │          │  │   │    │   │        │
│  N5──N6      │         │  J4──J5      │          │  N5──N6──J4──J5        │
└──────────────┘         └──────────────┘          │       B1    B2         │
                                                   │      ╱  ╲  ╱  ╲       │
                                                   │    N2   J3 N5   J4    │
                                                   └─────────────────────────┘
```
