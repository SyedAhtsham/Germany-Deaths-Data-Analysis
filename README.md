# Germany's Death Statistics Analysis using Python

This project analyzes the projected population of each state in Germany, exploring various trends, regional disparities, and demographic patterns. It was developed as part of the Research Software Engineering course at the University of Potsdam.

## Introduction

Understanding population projections is essential for policy development, resource allocation, and healthcare planning. Germany's unique historical context and diverse regional characteristics make it particularly interesting for population analysis. By examining population trends and projections, we aim to gain insights into future demographic changes and their implications.

## Problem Description

The project addresses several key questions:

1. **Population Increase in City States:** Analyze differences in population growth between city states from 2022 to 2070.
2. **State with Largest Population Change:** Identify the state with the largest increase and decrease in population from 2022 to 2070, both in absolute numbers and relative to the current population.
3. **Trends in East and West Germany:** Investigate population trends from 2022 to 2070 in former East and West German states.
4. **Gender-Based Population Growth:** Determine if there's a difference in population growth between genders from 2022 to 2070 and assess the variations between East and West Germany.
5. **Population Changes in Berlin:** Examine population changes in Berlin, separated by gender, from 2022 to 2040 and from 2040 to 2070.
   
## Getting Started and Requirements

To run the program, follow these steps:

1. Download the repository and install required dependencies (e.g., pandas, matplotlib).
2. Ensure you have Python 3.11.3 or later installed.
3. Use Jupyter Notebook or any compatible editor to open the program files.
4. Execute the scripts or interact with the program via the command-line interface.

## Running the Program

The project includes Python scripts and Jupyter Notebooks for analysis. You can run the scripts directly or interact with the program using the command-line interface. Detailed instructions for running the program are provided in the respective sections.

## Dataset

The dataset used in this analysis is sourced from [Genesis](https://www-genesis.destatis.de/genesis/online), a statistical data service provided by the German government. Specifically, we utilized the GENESIS table: 12421-0004, which contains population projections with moderate life expectancy and net migration. The dataset is split into two CSV files to overcome size restrictions for free users. 

### Data Preprocessing
- Merged and cleaned CSV files.
- Renamed headers and converted numerical values.
- Translated German headers to English equivalents.
- Added global variables for easier data access.

## Command-Line Interface

To interact with the program via the command line, use the provided Python scripts and specify the required parameters (e.g., input CSV files). Follow the provided examples to execute specific analyses.

## License

This project is licensed under the [MIT License](https://gitup.uni-potsdam.de/hassan4/de-deaths-eda/-/blob/main/LICENSE.txt?ref_type=heads).

## Citation

To cite this project, refer to the information provided in the [CITATION file](https://gitup.uni-potsdam.de/hassan4/de-deaths-eda/-/blob/main/CITATION.cff?ref_type=heads).