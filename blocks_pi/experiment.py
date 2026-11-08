import argparse
import math

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Rectangle


def simulate(digits):
    m1 = 1.0
    m2 = float(100 ** (digits - 1))
    w1, w2 = 0.55, 1.25
    x1, x2 = 1.5, 4.5           # left edges
    v1, v2 = 0.0, -1.0         # big block approaches wall
    states = [(x1, x2, 0, 'Start')]
    count = 0

    while True:
        # Time until the small block hits the wall.
        t_wall = x1 / -v1 if v1 < 0 else math.inf

        # Time until the large and small block meet.
        closing_speed = v1 - v2
        gap = x2 - (x1 + w1)
        t_blocks = max(0.0, gap) / closing_speed if closing_speed > 0 else math.inf

        if math.isinf(t_wall) and math.isinf(t_blocks):
            break

        dt = min(t_wall, t_blocks)
        x1 += v1 * dt
        x2 += v2 * dt

        if t_wall < t_blocks:
            x1 = 0.0
            v1 = -v1
            what = 'Small block ↔ wall'
        else:
            x2 = x1 + w1
            # 1D perfectly elastic collision, conserving momentum and energy.
            old_v1, old_v2 = v1, v2
            v1 = ((m1 - m2) * old_v1 + 2 * m2 * old_v2) / (m1 + m2)
            v2 = (2 * m1 * old_v1 + (m2 - m1) * old_v2) / (m1 + m2)
            what = 'Small block ↔ large block'

        count += 1
        states.append((x1, x2, count, what))

        # Guard against a numerical stall for extreme mass ratios.
        if count > 100000:
            raise RuntimeError('Too many collisions; try fewer digits.')

    return states, m2, w1, w2


def main():
    parser = argparse.ArgumentParser(description='Pi from elastic collisions')
    parser.add_argument('--digits', type=int, choices=[1, 2, 3, 4], default=3,
                        help='Number of initial digits of pi (default: 3)')
    parser.add_argument('--speed', type=int, default=1,
                        help='Collision events per animation frame (default: 1)')
    args = parser.parse_args()
    if args.speed < 1:
        parser.error('--speed must be at least 1')

    states, mass, w1, w2 = simulate(args.digits)
    total = len(states) - 1
    print(f'Large-block mass: {mass:g} kg; small-block mass: 1 kg')
    print(f'Total collisions: {total} (pi begins 3.14159265...)')

    fig, ax = plt.subplots(figsize=(10, 4))
    fig.subplots_adjust(top=0.79, bottom=0.18)
    ax.set_xlim(-0.45, 6.3)
    ax.set_ylim(-0.25, 1.8)
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')

    ax.plot([-0.02, 6.3], [0, 0], color='black', lw=2)
    ax.plot([0, 0], [0, 1.65], color='black', lw=5)
    small = Rectangle((states[0][0], 0), w1, 0.55, color='#4C9FE6')
    big = Rectangle((states[0][1], 0), w2, 1.05, color='#E6A24C')
    ax.add_patch(small)
    ax.add_patch(big)
    ax.text(0.01, 0.90, 'Wall', transform=ax.transAxes, fontsize=10)
    ax.text(0.03, -0.02, 'Frictionless surface • perfectly elastic impacts',
            transform=ax.transAxes, fontsize=10, color='#555555')

    title = ax.text(0.5, 1.48, '', transform=ax.transAxes,
                    ha='center', fontsize=17, fontweight='bold')
    subtitle = ax.text(0.5, 1.24, '', transform=ax.transAxes,
                       ha='center', fontsize=11)
    event_label = ax.text(0.5, 1.06, '', transform=ax.transAxes,
                          ha='center', fontsize=10, color='#555555')
    ax.text(0.77, 0.25, f'Large mass = {mass:g} kg\nSmall mass = 1 kg',
            transform=ax.transAxes, ha='left', fontsize=10)

    nframes = math.ceil(total / args.speed) + 1

    def update(frame):
        index = min(frame * args.speed, total)
        x1, x2, count, what = states[index]
        small.set_x(x1)
        big.set_x(x2)
        title.set_text(f'Collisions: {count}')
        subtitle.set_text(f'π digits demonstrated: {total} collisions'
                          if index == total else 'Counting impacts...')
        event_label.set_text(what if index < total else 'Finished: blocks separate')
        return small, big, title, subtitle, event_label

    ani = FuncAnimation(fig, update, frames=nframes, interval=35,
                        repeat=False, blit=False)
    plt.show()


if __name__ == '__main__':
    main()
