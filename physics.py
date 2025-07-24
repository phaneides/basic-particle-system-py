
import numpy as np

def collide_particles(r1, v1, m1, r2, v2, m2):
    delta_r = r1 - r2
    dist2 = np.dot(delta_r, delta_r)
    if dist2 == 0:
        return v1, v2  # evitar división por cero

    n = delta_r / np.sqrt(dist2)
    v_rel_n = np.dot(v1 - v2, n)

    if v_rel_n < 0:
        J = (2 * v_rel_n) / (m1 + m2)
        v1_new = v1 - (J * m2) * n
        v2_new = v2 + (J * m1) * n
        return v1_new, v2_new
    return v1, v2

def collide_all(positions, velocities, masses, radii):
    """Aplica colisión par a par para todas las partículas."""
    N = len(positions)
    for i in range(N):
        for j in range(i+1, N):
            Rsum = radii[i] + radii[j]
            delta_r = positions[i] - positions[j]
            if np.dot(delta_r, delta_r) <= Rsum**2:
                velocities[i], velocities[j] = collide_particles(
                    positions[i], velocities[i], masses[i],
                    positions[j], velocities[j], masses[j]
                )
    return positions, velocities

def reflect_all(positions, velocities, radii, box):
    """Rebota cada partícula contra las paredes definidas en box."""
    for i, (r, v, R) in enumerate(zip(positions, velocities, radii)):
        x, y = r
        vx, vy = v
        if x - R < box['xmin']:
            x = box['xmin'] + R; vx *= -1
        elif x + R > box['xmax']:
            x = box['xmax'] - R; vx *= -1
        if y - R < box['ymin']:
            y = box['ymin'] + R; vy *= -1
        elif y + R > box['ymax']:
            y = box['ymax'] - R; vy *= -1

        positions[i]  = np.array([x, y])
        velocities[i] = np.array([vx, vy])
    return positions, velocities
