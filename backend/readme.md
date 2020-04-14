# Backend 
## Directory Structure

`web/`: http functions, handle http request.
## Database
We use Google Firestore as database

### DB structure
- **Collection**: MM/YYYY (The month that the data is being updated), each collection contains responses from all user in one survey.
    - **Document**: Email or name of the user, each document contains the answer of each user in this survey.

## API endpoints:
### Upload survey result
* **URL:** 
    
    `\sonar_survey`

* **Method:**
    
     `POST` 
  
*  **URL Params**

    None

* **Data Params**

    Content-Type: `multipart/form-data`

    `{'data': <*.csv file>}`

* **Success Response:**


  * **Code:** 200 <br />
    **Content:** 
    ```
    {
        "msg":"Successfully wrote to storage",
        "names":["Sara Parker-934","Sara Parker-570"],
        "survey-date":"042020"
    }
    ````
 
* **Error Response:**

  * **Code:** 400 Bad Request <br />
    **Content:** 
    ```
    {
        "msg":"File format error, *.csv file required",
        "names":[],
        "survey-date":"042020"
    }
    ```

* **Sample Call:**

  curl -F data=@data.csv <root_url>/sonar_survey

* **Notes:**

* **Cloud Run:**
  gcloud builds submit --tag gcr.io/sonar-272913/sonar-survey .

  gcloud run deploy --image gcr.io/sonar-272913/sonar-survey --platform managed