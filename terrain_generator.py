import numpy as np
import matplotlib.pyplot as plt


def simple_noise(shape, scale=0.1):
    return np.random.rand(*shape) * scale


def normalize_grid(grid):
    # Ensures values on the grid don't fall outside of 0-1 range
    return (grid - grid.min()) / (grid.max() - grid.min())


def generate_terrain(width, height, layers=1, scale=0.1, persistence=0.5):

    grid = simple_noise(shape=(width, height), scale=scale)
    amplitude = 1
    for i in range(1, layers):
        amplitude *= persistence
        scale *= 2  # Increase frequency
        grid += simple_noise((width, height), scale) * amplitude
    return normalize_grid(grid)


def visualize_terrain(grid):
    plt.imshow(grid, cmap="terrain")
    plt.colorbar()
    plt.show()


if __name__ == "__main__":
    width = 32
    height = 32
    layers = 8
    terrain = generate_terrain(width=width, height=height, layers=layers)
    visualize_terrain(terrain)
