# Sensor Plot Generator

A small Python project that generates synthetic temperature sensor data and saves publication-quality scatter, histogram, and box plot visualizations as a PNG file.

## Installation

1. Activate your `ece105` conda environment:

```bash
conda activate ece105
```

2. Install the required packages with conda or mamba:

```bash
conda install numpy matplotlib
```

or

```bash
mamba install numpy matplotlib
```

## Usage

Run the script from the project directory:

```bash
python generate_plots.py
```

This will generate the synthetic sensor data and save the output image file.

## Example output

The script produces a single PNG file named `sensor_analysis.png` containing three side-by-side plots:

- **Scatter plot:** timestamps versus temperature readings for Sensor A and Sensor B, showing how values change over time.
- **Histogram:** overlaid temperature distributions for Sensor A and Sensor B, with transparency so both distributions are visible and dashed lines marking each sensor mean.
- **Box plot:** side-by-side comparison of Sensor A and Sensor B temperature distributions, with an overall mean line across both sensors.

## AI tools used and disclosure

This README was drafted with the assistance of an AI writing tool. Please update this section with your preferred disclosure language and any additional details.
