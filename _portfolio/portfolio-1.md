---
title: "Immersed Boundary Method for Cilia & Particles using Lattice Spring Method"
excerpt: "A high-performance computational fluid dynamics framework for simulating fluid-structure interactions with cilia and deformable particles.<br/><video class='lazy-play' src='/images/cfd_gallery/video/ibm_ellipse.mp4' poster='/images/cfd_gallery/video/ibm_ellipse.jpg' width='800' height='158' muted loop playsinline preload='none' controls aria-label='Cilia and a deformable particle interacting with the flow'></video>"
collection: portfolio
date: 2022-06-01
---

## Project Overview
The **Immersed Boundary Method for Cilia & Particles (IBMC)** is a Fortran-based computational fluid dynamics framework that simulates the interaction between fluids and immersed structures. This solver implements the Immersed Boundary Method (IBM) to model flexible ciliary structures and elliptical particles within a fluid domain, enabling the study of complex fluid-structure interactions in biological and engineering applications.

## Key Features
- **Fluid-Structure Coupling**: Two-way coupling between incompressible fluid flow and elastic structures using the immersed boundary method.
- **Dynamic Resting Length**: Incorporates time-varying spring properties allowing for active cilia motion and beating patterns.
- **Multi-structure Support**: Simultaneously models both ciliary arrays and deformable elliptical particles in the same fluid domain.
- **High-Performance Computing**: Implements GPU-accelerated pressure solving using NVIDIA AmgX library.
- **Optimized Interactions**: Utilizes cell-based neighbor lists for efficient force calculations between particles.
- **Profiling Integration**: Includes NVTX instrumentation for performance analysis with NVIDIA profiling tools.

## Technical Details
- **Language**: Fortran
- **Core Modules**:
  - `mod_mesh`: Defines computational mesh and staggered grid arrangement
  - `mod_time`: Implements RK2 time integration for Navier-Stokes equations
  - `mod_pressure`: Solves the pressure Poisson equation
  - `mod_amgx`: Provides GPU acceleration for the pressure solver
  - `mod_ibm`: Implements the immersed boundary method force coupling
  - `mod_cilia` & `mod_closed_cilia`: Models ciliary structures and particles
  - `mod_inter_particle_force`: Handles particle-particle interactions
- **Dependencies**: Requires gfortran/NVIDIA HPC SDK, optionally CUDA and AmgX for acceleration

## Implementation Highlights
The solver discretizes the 2D incompressible Navier-Stokes equations on a staggered grid using a projection method. Immersed boundaries are represented as Lagrangian markers connected by springs, which interact with the fluid through discrete delta functions. The custom implementation features support for open ciliary structures and closed elliptical particles, with specialized force calculations for each. Particle interactions are optimized using cell-based neighbor lists, and the pressure solution is accelerated through optional GPU integration.

## Technical Documentation
[GitHub Repository](https://github.com/divyaprakash-iitd/ibmc/tree/dynamicrestinglength)
