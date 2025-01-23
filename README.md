# Data Visualization Project

## Overview
A Python-based data visualization tool for creating charts and graphs from various data sources.

## Setup
```bash
git clone https://github.com/username/data-visualization.git
cd data-visualization
pip install -r requirements.txt
```

## Dependencies
- Python 3.7+
- Pandas
- Matplotlib
- Seaborn

## Visualizations Supported
- Bar Charts
- Line Graphs
- Scatter Plots
- Pie Charts
- Heatmaps

## Example Usage
```python
import datavis

# Load data
data = datavis.load_csv('data.csv')

# Create bar chart
datavis.bar_chart(
    data, 
    x='category', 
    y='value', 
    title='Data Distribution'
)
```

## Features
- Easy data import
- Multiple chart types
- Customizable styling
- Export options (PNG, SVG)
