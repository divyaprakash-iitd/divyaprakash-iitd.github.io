---
title: "OpenFOAM Integration with Fortran Solid Solver using Immersed Boundary Method"
excerpt: "A custom OpenFOAM solver that integrates a Fortran-based 3D solid mechanics solver for fluid-structure interaction simulations using the Immersed Boundary Method.<br/><video class='lazy-play' src='/images/cfd_gallery/video/3d_particle.mp4' poster='/images/cfd_gallery/video/3d_particle.jpg' width='800' height='474' muted loop playsinline preload='none' controls aria-label='Immersed boundary method in OpenFOAM, lid-driven cavity with a particle'></video>"
collection: portfolio
date: 2023-01-15
---

## Project Overview
This project focuses on the development of a custom solver for OpenFOAM that enables fluid-structure interaction (FSI) simulations by coupling it with an external, Fortran-based 3D solid mechanics solver. The integration is achieved through the Immersed Boundary Method (IBM), allowing for the simulation of deformable solids within a fluid flow. The project is a work in progress, with a functional implementation that can be further improved.

## Key Features
- **Fluid-Solid Coupling**: Implements a continuous forcing Immersed Boundary Method to couple a Fortran solid solver with the OpenFOAM fluid solver.
- **Custom OpenFOAM Solver**: The standard `icoFoam` solver is modified to include the IBM source term, enabling the interaction between the fluid and the immersed solid.
- **Interoperability**: Demonstrates the ability to link Fortran subroutines with C++ code in OpenFOAM, creating a shared library for the solid solver.
- **3D Simulation**: The solver is designed for 3D simulations, handling the complexities of force and velocity interpolation in a 3D domain.
- **Advanced Implementation**: The implementation includes features like creating a list of neighboring cells to optimize the force spreading and interpolation steps.

## Technical Details
- **Fluid Solver**: OpenFOAM (modified `icoFoam`)
- **Solid Solver**: Custom Fortran-based 3D solver
- **Coupling Method**: Immersed Boundary Method (Continuous Forcing)
- **Core Components**:
  - `icoFoam.C`: Modified main solver file.
  - `createFields.H`: Modified to include the IBM force field.
  - `fem3d.f90`: Fortran source code for the 3D solid solver.
  - `soft_particles.f90`: Fortran source for the interface between OpenFOAM and the solid solver.

## Implementation Highlights
The implementation involves modifying the momentum predictor step in the `icoFoam` solver to include a source term representing the force exerted by the immersed boundary. A shared library is created from the Fortran code, which is then linked with the OpenFOAM solver. The communication between the two solvers is handled by a set of Fortran subroutines that exchange position, force, and velocity data. The code is still under development, with opportunities for improvement in efficiency and accuracy.

## Technical Documentation
[GitHub Repository](https://github.com/divyaprakash-iitd/ciliaparticlefoam)
