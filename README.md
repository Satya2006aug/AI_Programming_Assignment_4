# Constraint Satisfaction Problems (CSP) Assignment

This project implements several classical **Constraint Satisfaction Problems (CSPs)** using Python and backtracking search. CSPs involve assigning values to variables while satisfying constraints between them.

The assignment includes implementations for:

- Map Coloring for **Australia**
- Map Coloring for the **33 districts of Telangana**
- **Sudoku Solver**
- **Cryptarithm Puzzle**

---

# Problem 1: Australia Map Coloring

## Objective
Assign colors to the seven principal states and territories of Australia such that **no neighboring states share the same color**.

## States
- WA – Western Australia  
- NT – Northern Territory  
- Q – Queensland  
- SA – South Australia  
- NSW – New South Wales  
- V – Victoria  
- T – Tasmania  

## CSP Formulation
- **Variables:** States  
- **Domain:** `{Red, Green, Blue}`  
- **Constraint:** Adjacent states must have different colors  

The problem is solved using **backtracking search**.

---

# Problem 2: Telangana District Map Coloring

## Objective
Apply the map coloring CSP to the **33 districts of Telangana**, ensuring neighboring districts have different colors.

## CSP Formulation
- **Variables:** Districts  
- **Domain:** `{Red, Green, Blue, Yellow}`  
- **Constraint:** Adjacent districts must not share the same color  

The result is visualized using **NetworkX** and **Matplotlib**, where districts are represented as nodes in a graph.

---

# Problem 3: Sudoku Solver

## Objective
Solve a **9 × 9 Sudoku puzzle** using Constraint Satisfaction.

## CSP Formulation
- **Variables:** 81 cells in the grid  
- **Domain:** `{1,2,3,4,5,6,7,8,9}`  

## Constraints
- No duplicate numbers in a **row**
- No duplicate numbers in a **column**
- No duplicate numbers in each **3 × 3 subgrid**

The puzzle is solved using **backtracking with constraint checking**.

---

# Problem 4: Cryptarithm Puzzle

## Problem

```
  TWO
+ TWO
-----
 FOUR
```

Each letter represents a **distinct digit**.

## Constraints
- Each letter maps to a **unique digit**
- **Leading digits cannot be zero**
- The arithmetic equation must be satisfied

The solution is found by testing **permutations of digits**.

---

# Technologies Used

- Python 3
- NetworkX
- Matplotlib

---

# Installation

Install the required libraries:

```
pip install networkx matplotlib
```

---

# Running the Program

Run the Python script:

```
python assignment.py
```

The program will sequentially solve all four problems and display the results.

---

# Concepts Demonstrated

- Constraint Satisfaction Problems (CSP)
- Backtracking Search
- Constraint Checking
- Graph-based Problem Modeling
- Visualization of Graph Coloring

---

# Author

Satya V
