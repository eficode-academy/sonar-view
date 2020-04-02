# sonar

## Data flow

Data comes in CSV files (From Google forms or Survey pal)
"importer" program runs either A: on the user computer, or B: on a website
Data comes into a data store with the month and year as the ID.
Frontend queries the data for different things like:

* Give me all data, sortet by survey period
* Give me all data by this person, sortet by survey period
* Give me all persons with this keyword in this level