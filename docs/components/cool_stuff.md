# Cool Stuff

Empire Chain includes some exciting features that push the boundaries of what's possible with AI.

## Data Visualization

Analyze and visualize data using natural language:

```python
from empire_chain.cool_stuff.visualizer import DataAnalyzer, ChartFactory

# Example data
data = """
Empire chain got a fund raise of $100M from a new investor in 2024
and $50M from a new investor in 2023.
"""

# Analyze data
analyzer = DataAnalyzer()
analyzed_data = analyzer.analyze(data)

# Create and display chart
chart = ChartFactory.create_chart('Bar Chart', analyzed_data)
chart.show()
```

Supported chart types:
- Line Chart
- Pie Chart
- Bar Graph
- Scatter Plot
- Histogram
- Box Plot

## Text to Podcast

Convert text into engaging podcast-style audio:

```python
from empire_chain.cool_stuff.podcast import GeneratePodcast

# Create podcast generator
podcast = GeneratePodcast()

# Generate podcast from topic
podcast.generate(topic="About boom of meal plan and recipe generation apps")
```

## Features

- **Data Visualization**:
  - Natural language data analysis
  - Multiple chart types
  - Automatic data formatting
  - Interactive visualizations

- **Text to Podcast**:
  - Natural-sounding voices
  - Topic-based generation
  - Customizable output
  - Background music support

## Installation

```bash
# Base installation
pip install empire-chain

# Text to Podcast dependencies
pip install kokoro_onnx  # Note: Model download may take time
```

For more examples and advanced usage, check out the cool stuff cookbooks in the repository. 