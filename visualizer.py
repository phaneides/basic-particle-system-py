from vispy import scene
from vispy.scene import visuals
import numpy as np

def setup_canvas(box):
    canvas = scene.SceneCanvas(keys='interactive', show=True, bgcolor='black')
    view   = canvas.central_widget.add_view()
    view.camera = scene.cameras.PanZoomCamera(aspect=1)
    view.camera.set_range(x=(box['xmin'], box['xmax']),
                          y=(box['ymin'], box['ymax']))
    return canvas, view

def draw_box(view, box):
    # rectángulo de líneas
    corners = np.array([
        [box['xmin'], box['ymin']],
        [box['xmax'], box['ymin']],
        [box['xmax'], box['ymax']],
        [box['xmin'], box['ymax']],
        [box['xmin'], box['ymin']],
    ], dtype=float)
    return visuals.Line(pos=corners, color='white', parent=view.scene)

def create_particles(view, positions, radii, colors):
    """
    Crea y retorna lista de Ellipse visual para N partículas.
    `colors` debe ser iterable de largo N.
    """
    circles = []
    for r, R, c in zip(positions, radii, colors):
        circle = visuals.Ellipse(center=r, radius=R,
                                 color=c, border_color='white',
                                 parent=view.scene)
        circles.append(circle)
    return circles
