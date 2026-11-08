# Digits of π from Two Colliding Blocks

This is a beginner-friendly Python animation of a surprising physics experiment: **counting collisions between two blocks and a wall produces the opening digits of π (pi).**

## The setup

- Two blocks slide in a straight line on a **frictionless horizontal surface**.
- A rigid wall is on the **left**.
- The **small blue block** (1 kg) begins at rest between the wall and a larger block.
- The **large orange block** moves left toward the small block.
- Every collision (block–block or small block–wall) is **perfectly elastic**: no kinetic energy is lost.

The small block bounces back and forth until both blocks move away from the wall and cannot collide again. The program counts **every** impact, including impacts with the wall.

## Install and run

You need **Python 3.9 or newer** and the Python packages `matplotlib` and `numpy` is *not* required by the current script (only Matplotlib is used).

1. Place `pi_collisions.py` in a folder on your computer.
2. Open a terminal (Command Prompt or PowerShell on Windows) in that folder.
3. Install Matplotlib:

   ```bash
   python -m pip install matplotlib
   ```

4. Start the animation:

   ```bash
   python pi_collisions.py --digits 3
   ```

A window opens showing the wall, moving blocks, and a collision counter. The terminal also prints the final collision count.

### Choose the number of digits

```bash
python pi_collisions.py --digits 1   # 3 collisions
python pi_collisions.py --digits 2   # 31 collisions
python pi_collisions.py --digits 3   # 314 collisions
python pi_collisions.py --digits 4   # 3141 collisions
```

For runs with many collisions, speed up the animation by skipping to every Nth collision event:

```bash
python pi_collisions.py --digits 4 --speed 20
```

`--speed 20` displays every 20th collision state, **but the simulation still computes and counts all collisions**. The animation therefore shows representative positions, not every impact individually. Supported digit choices are 1 through 4.

If `python` is not recognized on Windows, try `py` instead (for example, `py pi_collisions.py --digits 3`).

## Why does π appear?

Let the small block have mass **m = 1 kg** and the large block mass **M**. Choose their mass ratio as

\[M/m = 100^{n-1}\]

where **n** is the number of digits of π you want to demonstrate.

| Desired digits (n) | Large mass (M) | Total collisions | Opening digits of π |
| --- | ---: | ---: | --- |
| 1 | 1 kg | 3 | 3 |
| 2 | 100 kg | 31 | 3.1 |
| 3 | 10,000 kg | 314 | 3.14 |
| 4 | 1,000,000 kg | 3,141 | 3.141 |

The decimal point is not part of the physical count. For example, 314 collisions represent the digits **3.14**.

**Physics intuition:** Each perfectly elastic collision transfers momentum between the blocks while conserving the total kinetic energy. If you represent the velocities using appropriately mass-scaled coordinates, the collision sequence acts like repeated reflections through a fixed angle. The angle depends on the square root of the mass ratio. When **M/m = 100^(n−1)**, the number of reflections follows the first digits of π. This is often called *Galperin's billiards* or the *pi collisions experiment*.

## What the code actually calculates

Rather than guessing when a collision happened from small animation time steps, the script **calculates the time until the next possible impact**, advances the blocks to that moment, then updates their velocities using the one-dimensional elastic-collision equations:

```text
v1_new = ((m1 - m2) * v1 + 2*m2*v2) / (m1 + m2)
v2_new = (2*m1*v1 + (m2 - m1)*v2) / (m1 + m2)
```

At the wall, the small block reverses its velocity (`v1_new = -v1`). The simulation stops when there can be no more collisions.

The wall is drawn farther left for readability. The block positions are shifted by the **same amount in the plot only**, so this visual adjustment does not change the physics or collision counts.

## Notes and troubleshooting

- **The blocks do not continuously glide at every moment:** the animation shows states at successive collision events. The time spacing between displayed frames is for viewing, not physical time.
- **Matplotlib window does not appear?** Run the script from a local terminal in a graphical desktop environment, rather than a headless server.
- **Animation too slow?** Increase `--speed` (such as `--speed 30`).
- **`ModuleNotFoundError: matplotlib`?** Run `python -m pip install matplotlib` in the same Python environment used to run the script.

This is an idealized 1D model: real blocks would lose energy from friction, deformation, and sound, so the exact π pattern requires the assumed perfectly elastic collisions and frictionless motion.
