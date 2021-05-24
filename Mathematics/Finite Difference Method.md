## Lax Equivalence Theorem


1. CONSISTENCY: A finite difference approximation is considered consistent if by reducing the mesh and time step size, the LTE could be made to approach zero. In that case, the solution to the equivalent difference equation would approach the true solution to the PDE.

2. STABILITY: A finite difference approximation is stable if the errors (truncation, round-off etc) decay as the computation proceeds from one marching step to the next. Stability of a finite difference approximation is assessed using Von-Neumann stability analysis.

3. CONVERGENCE: means that the solution to the finite difference approximation approaches the true solution of the PDE when the mesh is refined. Of course, the finite difference formulation must have the same set of ICs and BCs.

The important Lax Equivalence Theorem says that a finite difference approximation for a properly posed PDE satisfying **consistency and stability** possesses necessary and sufficient conditions for convergence.


## Reference

[1] [What is the difference between consistency, stability and convergence for the numerical treatment of any PDE?](https://www.researchgate.net/post/What_is_the_difference_between_consistency_stability_and_convergence_for_the_numerical_treatment_of_any_PDE)