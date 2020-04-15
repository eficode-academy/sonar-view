# sonar
![](https://github.com/praqma-training/sonar/workflows/Frontend/badge.svg)

![](https://github.com/praqma-training/sonar/workflows/Cloud%20Functions/badge.svg)

## Data flow

Data comes in CSV files (From Google forms or Survey pal)
"importer" program runs either A: on the user computer, or B: on a website
Data comes into a data store with the month and year as the ID.
Frontend queries the data for different things like:

* Give me all data, sorted by survey period
* Give me all data by this person, sorted by survey period
* Give me all persons with this keyword in this level


## Starting with project
This project uses [venv](https://www.freecodecamp.org/news/manage-multiple-python-versions-and-virtual-environments-venv-pyenv-pyvenv-a29fb00c296f/)

### Creating mock data
This is the mock-data to work with frontend. The real app will replace this data from other source in future

    cd sonar/
    test-data/convert-to-json.py

*data.json* file is created *under test-data*
