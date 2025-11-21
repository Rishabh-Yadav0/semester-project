# CME Detection Project

This project is designed to analyze and visualize Coronal Mass Ejections (CMEs) using data parsed from Cactus files. It includes Jupyter notebooks for data processing and analysis, Python scripts for loading and plotting data, and a set of test cases to ensure functionality.

## Project Structure

- **notebooks/**: Contains Jupyter notebooks for data analysis.
  - `01-parse-cactus-cmes.ipynb`: Demonstrates the detection of CME occurrences and includes code for parsing data and generating plots.
  - `02-analysis.ipynb`: Further analysis of the CME data, building on the results from the first notebook.

- **scripts/**: Contains Python scripts for data handling.
  - `load_plot_cactus_data.py`: Functions for loading and plotting data from Cactus files.
  - `utils.py`: Utility functions that support the main functionality of the project.

- **data/**: Contains CME data files.
  - `cmesept2024.txt`: CME data for September 2024.
  - `cmeoct2024.txt`: CME data for October 2024.
  - `cmenov2024.txt`: CME data for November 2024.
  - `cmedec2024.txt`: CME data for December 2024.

- **tests/**: Contains unit tests for the project.
  - `test_load_plot_cactus_data.py`: Unit tests for the functions defined in `load_plot_cactus_data.py`.

- **.gitignore**: Specifies files and directories to be ignored by Git.

- **requirements.txt**: Lists the Python packages required for the project.

- **environment.yml**: Defines the environment configuration for the project.

- **pyproject.toml**: Configuration file for the project and its dependencies.

## Installation

To set up the project, clone the repository and install the required packages:

```bash
git clone <repository-url>
cd cme-detection
pip install -r requirements.txt
```

Alternatively, you can create a conda environment using the `environment.yml` file:

```bash
conda env create -f environment.yml
```

## Usage

1. Open the Jupyter notebooks in the `notebooks/` directory to explore the CME data and visualizations.
2. Use the scripts in the `scripts/` directory for data loading and plotting.
3. Run the tests in the `tests/` directory to ensure everything is functioning correctly.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.