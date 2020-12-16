# senator_fec_data 

![](https://github.com/bam2231/senator_fec_data/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/bam2231/senator_fec_data/branch/main/graph/badge.svg)](https://codecov.io/gh/bam2231/senator_fec_data) ![Release](https://github.com/bam2231/senator_fec_data/workflows/Release/badge.svg) [![Documentation Status](https://readthedocs.org/projects/senator_fec_data/badge/?version=latest)](https://senator_fec_data.readthedocs.io/en/latest/?badge=latest)

Python package to obtain the FEC data of current US senators.

## Installation

```bash
$ pip install -i https://test.pypi.org/simple/ senator_fec_data
```

## Features

This package returns data on U.S. Senators from the FEC API (https://api.open.fec.gov/developers/). Users can obtain a dataset of the current senators and receive the FEC candidate ID associated with those senators. Users are able to search facts about senator FEC filings, visualize their FEC results, and even produce a full report on their senators.

## Dependencies

- bs4
- os
- requests
- json
- pandas as pd
- matplotlib.pyplot
- xml.etree.ElementTree

## Usage

Find more information about this package and its use at `./senator_fec_data/Extended_Tutorial`. 

## Documentation

The official documentation is hosted on Read the Docs: https://senator_fec_data.readthedocs.io/en/latest/

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/bam2231/senator_fec_data/graphs/contributors).

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
