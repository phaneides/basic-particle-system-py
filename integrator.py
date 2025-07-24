
def euler(positions, velocities, masses, dt, *force_funcs):
    """
    Método de Euler explícito general:
      1) r <- r + v * dt
      2) para cada f in force_funcs: (r, v) <- f(r, v, masses, ...)
    Devuelve (positions, velocities) actualizados.
    """
    # 1) paso de Euler para posiciones
    positions += velocities * dt

    # 2) aplicar correcciones “fisicales” (choques, reflexiones…)
    for f in force_funcs:
        positions, velocities = f(positions, velocities, masses)

    return positions, velocities
