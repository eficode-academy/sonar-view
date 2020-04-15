# Backend 
## Directory Structure

`data_endpoints/`: http functions, handle http request.
## Database
We use Google Firestore as database

### DB structure
- **Collection**: YYYY-MM (The month that the data is being updated), each collection contains responses from all user in one survey.
    - **Document**: Email or name of the user, each document contains the answer of each user in this survey.

## API endpoints:
### Upload survey result
* **URL:** 
    
    `/surveys`

* **Method:**
    
     `POST` 
  
*  **URL Params**

    None

* **Data Params**

    Content-Type: `multipart/form-data`

    ```
    
    {
      'name': <YYYY-MM>
      'data': <*.csv file>
      }
    
    ```

* **Success Response:**


  * **Code:** 200 <br />
    **Content:** 
    ```
    {
        "msg":"Successfully wrote to storage",
        "persons":["johndone@eficode.com"],
        "collection":"2020-04"
    }
    ````
 
* **Error Response:**

  * **Code:** 400 Bad Request <br />
    **Content:** 
    ```
    {
        "msg":"File format error, *.csv file required",
        "persons":[],
        "collection":"2020-04"
    }
    ```
  * **Code:** 400 Bad Request <br />
    **Content:** 
    ```
    {
        "msg":"Collection name should be named by survey date (YYYY-MM)",
        "persons":[],
        "collection":"2020-04"
    }
    ```

* **Sample Call:**

  `curl -F data=@data.csv -F name=<YYYY-MM> <root_url>/surveys`

* **Notes:**

## Cloud Run Deployment
  `gcloud builds submit --tag gcr.io/sonar-272913/sonar-survey .`

  `gcloud run deploy --image gcr.io/sonar-272913/sonar-survey --platform managed`