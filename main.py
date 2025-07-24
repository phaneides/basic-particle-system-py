import numpy as np
from vispy import app

import physics
import integrator
import visualizer

# --- Configuración física ---
BOX = {'xmin': 0, 'xmax': 10, 'ymin': 0, 'ymax': 10}
dt = 0.01
N  = 5

# Semilla reproducible
rng = np.random.default_rng(42)

# Posiciones dentro de BOX con margen de 1 unidad
positions = rng.uniform([BOX['xmin']+1, BOX['ymin']+1],
                        [BOX['xmax']-1, BOX['ymax']-1], size=(N,2))
# Velocidades aleatorias
velocities = rng.uniform(-5, 5, size=(N,2))
# Masas y radios constantes (pero podrían ser arrays distintos)
masses  = np.ones(N)
radii   = 0.3 * np.ones(N)
# Colores para visual
colors  = ['red', 'blue', 'green', 'yellow', 'magenta']

# --- Visualización ---
canvas, view = visualizer.setup_canvas(BOX)
box_line     = visualizer.draw_box(view, BOX)
circles      = visualizer.create_particles(view, positions, radii, colors)

# --- Loop de animación ---
def update(event):
    global positions, velocities

    # Euler con reflect_all y collide_all (como “fuerzas”)
    positions, velocities = integrator.euler(
        positions, velocities, masses, dt,
        lambda p, v, m: physics.reflect_all(p, v, radii, BOX),
        lambda p, v, m: physics.collide_all(p, v, masses, radii)
    )

    # Actualizar cada círculo en pantalla
    for circle, r in zip(circles, positions):
        circle.center = r

timer = app.Timer(interval=dt, connect=update, start=True)
app.run()
