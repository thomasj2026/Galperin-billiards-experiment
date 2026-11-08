# The Digits of π Through Elastic Collisions

## Overview

This Python simulation demonstrates how the digits of π can emerge from perfectly elastic collisions between two blocks on a frictionless surface.

The experiment involves a small block positioned between a wall and a larger moving block. By increasing the mass of the larger block, the total number of collisions produces the digits of π.

## Requirements

- Python 3
- NumPy
- Matplotlib

Install the required libraries:

```bash
pip install numpy matplotlib
```

## Running the Simulation

To simulate three digits of π (314 collisions):

```bash
python experiments.py --digits 3
```

To simulate four digits of π (3141 collisions) with accelerated animation:

```bash
python experiments.py --digits 4 --speed 20
```

## The Physics Behind the Experiment

The simulation assumes:

- A frictionless horizontal surface.
- Two blocks moving in one dimension.
- A perfectly rigid wall.
- Perfectly elastic collisions.
- Conservation of momentum and kinetic energy.

The heavier block initially moves toward the smaller stationary block, which is positioned near the wall.

The blocks collide repeatedly, and the smaller block also bounces off the wall.

Eventually, both blocks move away from the wall without further collisions.

## How π Appears

The mass ratio between the two blocks is:

$$
\frac{M}{m}=100^{n-1}
$$

where:

- \(M\) is the mass of the heavier block.
- \(m\) is the mass of the lighter block.
- \(n\) is the number of digits of π represented by the collision count.

| Heavy Block Mass (Small Block = 1 kg) | Collisions |
|---|---|
| 1 kg | 3 |
| 100 kg | 31 |
| 10,000 kg | 314 |
| 1,000,000 kg | 3141 |

The number of collisions corresponds to the digits of π, with the decimal point omitted.

## Scientific Background

This experiment is known as **Galperin's billiards**, associated with mathematician Gregory Galperin.

The appearance of π is related to a geometric interpretation of the collision dynamics in velocity space, where conservation of energy constrains the system's motion.

This demonstrates a surprising relationship between classical mechanics, geometry, and mathematics.

## Purpose

This simulation provides a visual demonstration of conservation laws and the unexpected appearance of π in a simple mechanical system.
