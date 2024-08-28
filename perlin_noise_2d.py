import numpy as np
import matplotlib.pyplot as plt


def generate_perlin_noise(
    width, height, scale=10, octaves=6, persistence=0.5, lacunarity=2.0
):
    def generate_octave(width, height):
        return np.random.uniform(-1, 1, (height, width))

    def interpolate(a, b, x):
        ft = x * np.pi
        f = (1 - np.cos(ft)) * 0.5
        return a * (1 - f) + b * f

    def smooth_noise(noise, scale):
        smooth = np.zeros_like(noise)
        for y in range(noise.shape[0]):
            for x in range(noise.shape[1]):
                sample_x = x / scale
                sample_y = y / scale
                x0 = int(sample_x) % noise.shape[1]
                x1 = (x0 + 1) % noise.shape[1]
                y0 = int(sample_y) % noise.shape[0]
                y1 = (y0 + 1) % noise.shape[0]
                horizontal_blend = sample_x - int(sample_x)
                vertical_blend = sample_y - int(sample_y)
                top = interpolate(noise[y0, x0], noise[y0, x1], horizontal_blend)
                bottom = interpolate(noise[y1, x0], noise[y1, x1], horizontal_blend)
                smooth[y, x] = interpolate(top, bottom, vertical_blend)
        return smooth

    noise = np.zeros((height, width))
    for i in range(octaves):
        frequency = lacunarity**i
        amplitude = persistence**i
        octave = generate_octave(width, height)
        octave = smooth_noise(octave, scale / frequency)
        noise += octave * amplitude

    noise = (noise - np.min(noise)) / (np.max(noise) - np.min(noise))
    return noise


# Generate and visualize perlin noise
width, height = 1024, 1024
noise = generate_perlin_noise(width, height)

plt.figure(figsize=(10, 10))
plt.imshow(noise, cmap="terrain")
plt.colorbar(label="Elevation")
plt.title("2D Perlin Noise, Terrain-like")
plt.show()
