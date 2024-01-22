**Project: RNA Folding Problem Solver**

# Bioinformatics of RNA GENIOMHE Master - 2023/2024

## Introduction
The RNA Folding Problem is a challenge in bioinformatics that involves determining the native fold of a ribonucleotide chain among a important number of potential conformations. The goal is to identify the conformation with the lowest Gibbs free energy. In this project, you will implement three Python scripts to address different aspects of this problem.

## Scripts Overview
This project comprises four Python scripts:

1. **main_script.py:**
   - Manages training and plotting.
   - Calls `train_objective_function` and `plot_scoring_profiles` from respective scripts.

2. **train_script.py:**
   - Trains the objective function.
   - Takes PDB files' input directory.
   - Computes RNA pseudo-energy, saves scores.

3. **plot_script.py:**
   - Plots scoring profiles.
   - Takes PDB files' input directory.
   - Computes RNA pseudo-energy, plots profiles, saves plots.

4. **all_functions.py:**
   - Common functions for both scripts.
   - Computes RNA pseudo-energy and plots scoring profiles.

**Usage:**
Execute `main_script.py` to automate training and plotting processes. You need to provided the input path containing the PDB files and the output directory for the train script and the plot script.


