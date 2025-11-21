import unittest
from scripts.load_plot_cactus_data import parse_cactus_file, plot_cme

class TestLoadPlotCactusData(unittest.TestCase):

    def test_parse_cactus_file(self):
        # Test parsing a sample Cactus file
        sample_data = parse_cactus_file('../data/cmesept2024.txt')
        self.assertIsInstance(sample_data, list)  # Check if the result is a list
        self.assertGreater(len(sample_data), 0)   # Ensure the list is not empty

    def test_plot_cme(self):
        # Test plotting function with sample data
        sample_data = parse_cactus_file('../data/cmesept2024.txt')
        try:
            plot_cme(sample_data)  # This should not raise an error
        except Exception as e:
            self.fail(f"plot_cme raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()