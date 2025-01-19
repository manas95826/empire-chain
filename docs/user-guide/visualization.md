# Visualization

## Overview

Empire Chain provides powerful visualization capabilities through its `visualizer` module. This guide covers how to create various types of visualizations for your data and AI pipeline results.

## Basic Visualizations

### Data Plots

```python
from empire_chain.visualizer import DataVisualizer
import pandas as pd

# Create sample data
data = pd.DataFrame({
    'x': range(10),
    'y': [x**2 for x in range(10)]
})

# Initialize visualizer
viz = DataVisualizer(data)

# Create different types of plots
viz.line_plot('x', 'y', title='Square Function')
viz.scatter_plot('x', 'y', title='Data Points')
viz.bar_plot('x', 'y', title='Bar Chart')
```

### Interactive Plots

```python
# Create interactive plot
viz.interactive_plot(
    'x', 'y',
    plot_type='line',
    hover_data=['x', 'y']
)

# Create dashboard
viz.create_dashboard([
    ('line', {'x': 'x', 'y': 'y'}),
    ('scatter', {'x': 'x', 'y': 'y'})
])
```

## AI Pipeline Visualization

### RAG Visualization

```python
from empire_chain.visualizer import RAGVisualizer

# Initialize RAG visualizer
rag_viz = RAGVisualizer(rag_system)

# Visualize retrieval process
rag_viz.show_retrieval_path()

# Visualize document similarities
rag_viz.plot_document_similarities()

# Show attention heatmap
rag_viz.attention_heatmap()
```

### Model Performance

```python
from empire_chain.visualizer import ModelVisualizer

# Initialize model visualizer
model_viz = ModelVisualizer(model)

# Plot training metrics
model_viz.plot_training_history()

# Show confusion matrix
model_viz.confusion_matrix()

# Plot attention weights
model_viz.attention_weights()
```

## Advanced Features

### Custom Styling

```python
# Set global style
viz.set_style({
    'theme': 'dark',
    'color_palette': ['#FF0000', '#00FF00', '#0000FF'],
    'font_family': 'Arial',
    'font_size': 12
})

# Apply to specific plot
viz.line_plot(
    'x', 'y',
    style={
        'line_color': '#FF0000',
        'line_width': 2,
        'marker_size': 8
    }
)
```

### Animation

```python
# Create animated plot
viz.animate_plot(
    'x', 'y',
    frames=range(10),
    title='Animation'
)

# Save animation
viz.save_animation('animation.gif')
```

### Export Options

```python
# Save as static image
viz.save_plot('plot.png', dpi=300)

# Export as interactive HTML
viz.export_interactive('plot.html')

# Export dashboard
viz.export_dashboard('dashboard.html')
```

## Streamlit Integration

```python
from empire_chain.visualizer import StreamlitVisualizer
import streamlit as st

# Initialize Streamlit visualizer
st_viz = StreamlitVisualizer()

# Create interactive components
st_viz.plot_with_controls(
    data,
    x_column='x',
    y_column='y',
    plot_types=['line', 'scatter', 'bar']
)

# Create metrics dashboard
st_viz.metrics_dashboard({
    'Accuracy': 0.95,
    'Precision': 0.92,
    'Recall': 0.89
})
```

## Best Practices

### Memory Management

```python
# Handle large datasets
viz.enable_chunking(chunk_size=1000)

# Clear memory
viz.clear_cache()
```

### Performance Optimization

```python
# Enable GPU acceleration
viz.enable_gpu()

# Use downsampling for large datasets
viz.downsample(factor=0.1)
```

### Responsive Design

```python
# Make plots responsive
viz.set_responsive(True)

# Set breakpoints
viz.set_breakpoints({
    'sm': 576,
    'md': 768,
    'lg': 992,
    'xl': 1200
})
```

## Examples

### Complex Dashboard

```python
# Create multi-panel dashboard
viz.create_complex_dashboard({
    'top': [
        ('metrics', {'values': {'Accuracy': 0.95}}),
        ('line', {'x': 'x', 'y': 'y'})
    ],
    'bottom': [
        ('heatmap', {'data': correlation_matrix}),
        ('scatter', {'x': 'x', 'y': 'y'})
    ]
})
```

### Custom Visualization

```python
from empire_chain.visualizer import BaseVisualizer

class CustomVisualizer(BaseVisualizer):
    def custom_plot(self, data, **kwargs):
        # Custom visualization logic
        pass

# Use custom visualizer
custom_viz = CustomVisualizer()
custom_viz.custom_plot(data)
``` 