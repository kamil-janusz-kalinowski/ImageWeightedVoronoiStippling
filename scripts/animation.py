import io
import matplotlib.pyplot as plt
from PIL import Image
import imageio

def get_current_plot_as_img() -> Image.Image:
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    frame = Image.open(buf)
    return frame

def save_frames_as_gif(frames: list, filename: str, fps: int = 10, loop: int = 0):
    imageio.mimsave(filename, frames, fps=fps, loop=loop)