import unittest
from unittest.mock import patch, MagicMock
import matplotlib.pyplot as plt
import json
from empire_chain.visualizer import (
    DataAnalyzer, ChartFactory, LineChart, PieChart, 
    BarGraph, ScatterChart, Histogram, BoxPlot
)

class TestVisualizer(unittest.TestCase):
    def setUp(self):
        self.sample_data = {
            "title": "Test Chart",
            "x-axis": "Categories",
            "y-axis": "Values",
            "datapoints": {"A": 1, "B": 2, "C": 3}
        }
        self.sample_data_json = json.dumps(self.sample_data)

    def test_data_analyzer_success(self):
        analyzer = DataAnalyzer()
        with patch.object(analyzer.client, 'generate') as mock_generate:
            mock_generate.return_value = json.dumps({
                "title": "Analysis",
                "x-axis": "X",
                "y-axis": "Y",
                "datapoints": {"test": 1}
            })
            result = analyzer.analyze("test data")
            self.assertIsInstance(result, dict)
            self.assertIn("title", result)
            self.assertIn("datapoints", result)

    def test_data_analyzer_failure(self):
        analyzer = DataAnalyzer()
        with patch.object(analyzer.client, 'generate') as mock_generate:
            mock_generate.return_value = "invalid json"
            result = analyzer.analyze("test data")
            self.assertIsNone(result["result"])
            self.assertIn("error", result)

    def test_line_chart(self):
        chart = LineChart(self.sample_data)
        fig = chart.plot()
        self.assertIsNotNone(fig)
        plt.close()

    def test_pie_chart(self):
        chart = PieChart(self.sample_data)
        fig = chart.plot()
        self.assertIsNotNone(fig)
        plt.close()

    def test_bar_graph(self):
        chart = BarGraph(self.sample_data)
        fig = chart.plot()
        self.assertIsNotNone(fig)
        plt.close()

    def test_scatter_chart(self):
        chart = ScatterChart(self.sample_data)
        fig = chart.plot()
        self.assertIsNotNone(fig)
        plt.close()

    def test_histogram(self):
        chart = Histogram(self.sample_data)
        fig = chart.plot()
        self.assertIsNotNone(fig)
        plt.close()

    def test_box_plot(self):
        chart = BoxPlot(self.sample_data)
        fig = chart.plot()
        self.assertIsNotNone(fig)
        plt.close()

    def test_chart_factory_valid_type(self):
        chart = ChartFactory.create_chart('Line Chart', self.sample_data)
        self.assertIsInstance(chart, LineChart)

    def test_chart_factory_invalid_type(self):
        chart = ChartFactory.create_chart('Invalid Chart', self.sample_data)
        self.assertIsNone(chart)

    def test_invalid_data_format(self):
        invalid_data = {
            "title": "Test Chart",
            "x-axis": "Categories",
            "y-axis": "Values",
            "datapoints": {"A": "invalid", "B": "invalid2"}  # Non-numeric values
        }
        chart = LineChart(invalid_data)
        self.assertIsNone(chart.plot())
        plt.close()

    def test_error_result_handling(self):
        error_data = {
            "result": None,
            "error": "Test error message"
        }
        chart = LineChart(error_data)
        self.assertIsNone(chart.plot())
        plt.close()

if __name__ == "__main__":
    unittest.main()