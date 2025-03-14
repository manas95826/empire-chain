"""
This is a simple example of how to use the DataAnalyzer and ChartFactory classes to visualize data.
Please run the following command to install the necessary dependencies and store keys in .env:
!pip install empire-chain matplotlib

_chart_types = {
        'Line Chart': LineChart,
        'Pie Chart': PieChart,
        'Bar Graph': BarGraph,
        'Scatter Plot': ScatterChart,
        'Histogram': Histogram,
        'Box Plot': BoxPlot
    }
Please adhere to the naming convention for the chart type.
"""
from empire_chain.cool_stuff.visualizer import DataAnalyzer, ChartFactory

data = """
Empire chain got a fund raise of $100M from a new investor in 2024 and $50M from a new investor in 2023.
"""
    
analyzer = DataAnalyzer()
analyzed_data = analyzer.analyze(data)
        
chart = ChartFactory.create_chart('Bar Graph', analyzed_data)
chart.show()
