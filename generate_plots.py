"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np
import matplotlib.pyplot as plt


def generate_data(seed):
    """Generate synthetic temperature sensor data.

    Parameters
    ----------
    seed : int
        Seed value for the random number generator.

    Returns
    -------
    sensor_a : numpy.ndarray
        Array of 200 temperature readings for Sensor A, sampled from a
        normal distribution with mean 25 °C and standard deviation 3 °C.
    sensor_b : numpy.ndarray
        Array of 200 temperature readings for Sensor B, sampled from a
        normal distribution with mean 27 °C and standard deviation 4.5 °C.
    timestamps : numpy.ndarray
        Array of 200 time values sampled uniformly from 0 to 10 seconds.
    """
    rng = np.random.default_rng(seed)
    timestamps = rng.uniform(0, 10, 200)
    sensor_a = rng.normal(25, 3, 200)
    sensor_b = rng.normal(27, 4.5, 200)
    return sensor_a, sensor_b, timestamps

# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.


def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Draw a scatter plot of sensor temperature readings on an Axes.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Array of temperature readings from Sensor A.
    sensor_b : numpy.ndarray
        Array of temperature readings from Sensor B.
    timestamps : numpy.ndarray
        Array of timestamps corresponding to each reading.
    ax : matplotlib.axes.Axes
        Axes object to draw the scatter plot on.

    Returns
    -------
    None
        The function modifies the provided Axes in place.
    """
    ax.scatter(timestamps, sensor_a, color='blue', label='Sensor A', alpha=0.7)
    ax.scatter(timestamps, sensor_b, color='orange', label='Sensor B', alpha=0.7)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Sensor Temperature Readings Over Time')
    ax.legend()
    ax.grid(True)


# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.


def plot_histogram(sensor_a, sensor_b, ax):
    """Draw overlaid histograms of sensor temperature distributions.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Array of temperature readings from Sensor A.
    sensor_b : numpy.ndarray
        Array of temperature readings from Sensor B.
    ax : matplotlib.axes.Axes
        Axes object to draw the histogram on.

    Returns
    -------
    None
        The function modifies the provided Axes in place.
    """
    ax.hist(sensor_a, bins=30, alpha=0.5, color='blue', label='Sensor A')
    ax.hist(sensor_b, bins=30, alpha=0.5, color='orange', label='Sensor B')
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Frequency')
    ax.set_title('Temperature Distributions of Sensors A and B')
    ax.axvline(sensor_a.mean(), color='blue', linestyle='--', linewidth=2, label='Sensor A Mean')
    ax.axvline(sensor_b.mean(), color='orange', linestyle='--', linewidth=2, label='Sensor B Mean')
    ax.legend()


# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

#Create plot_histogram(sensor_a, sensor_b, ax) that draws the histogram from the
# notebook onto the given Axes object. 
# NumPy-style docstring. Modifies ax in place, returns None.


def plot_boxplot(sensor_a, sensor_b, ax):
    """Draw side-by-side box plots comparing sensor temperature distributions.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Array of temperature readings from Sensor A.
    sensor_b : numpy.ndarray
        Array of temperature readings from Sensor B.
    ax : matplotlib.axes.Axes
        Axes object to draw the box plot on.

    Returns
    -------
    None
        The function modifies the provided Axes in place.
    """
    ax.boxplot([sensor_a, sensor_b], tick_labels=['Sensor A', 'Sensor B'])
    ax.set_xlabel('Sensor')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Box Plot Comparison of Sensor A and B Temperatures')
    overall_mean = np.concatenate([sensor_a, sensor_b]).mean()
    ax.axhline(overall_mean, color='red', linestyle='--', linewidth=2, label=f'Overall Mean: {overall_mean:.2f}°C')
    ax.legend()

# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

#Create plot_histogram(sensor_a, sensor_b, ax) that draws the histogram from the
# notebook onto the given Axes object. 
# NumPy-style docstring. Modifies ax in place, returns None.

#Create a plot_box(sensor_a, sensor_b, ax) function that draws the box plot from the 
# notebook onto the given Axes object. 
# NumPy-style docstring. Modifies ax in place, returns None.

def main():
    """Generate data, render plots, and save the resulting figure.

    The function generates synthetic sensor data using a reproducible seed,
    creates a 1x3 subplot figure, plots the scatter, histogram, and box
    plot visualizations onto the provided Axes objects, and saves the
    figure to disk.

    Returns
    -------
    None
        The function saves the figure as a PNG file and does not return a value.
    """
    seed = 389
    sensor_a, sensor_b, timestamps = generate_data(seed)

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes = axes.flatten()

    plot_scatter(sensor_a, sensor_b, timestamps, axes[0])
    plot_histogram(sensor_a, sensor_b, axes[1])
    plot_boxplot(sensor_a, sensor_b, axes[2])

    summary_ax = axes[3]
    summary_ax.axis('off')
    summary_text = (
        f"Sensor A: mean={sensor_a.mean():.2f} °C, std={sensor_a.std():.2f} °C\n"
        f"Sensor B: mean={sensor_b.mean():.2f} °C, std={sensor_b.std():.2f} °C\n"
        f"Combined mean={np.concatenate([sensor_a, sensor_b]).mean():.2f} °C"
    )
    summary_ax.text(0.5, 0.5, summary_text, ha='center', va='center', fontsize=12)

    fig.tight_layout()
    fig.savefig('sensor_analysis.png', dpi=150, bbox_inches='tight')
    plt.close(fig)


if __name__ == '__main__':
    main()
