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
  ### **Build Image**
    gcloud builds submit --tag gcr.io/sonar-272913/sonar-survey .
  ### **Deploy image to Cloud Run**
    gcloud run deploy --image gcr.io/sonar-272913/sonar-survey --platform managed

### **URL:** 
    
    `/surveys`

* **Method:**
    
     `GET` 
  
*  **URL Params**

    None

* **Success Response:** <br />
    ***Get all the survey dates***
  * **Code:** 200 <br />
    **Content:** 
    ```
    {
        "0": "042020",
        "1": "2020-03",
        "2": "2020-04"
    }
    ````

  *  **URL Params** <br />
    /surveys/survey-id/persons <br />
     ***Example:*** <br />
     /surveys/2020-04/persons<br />
     It gives all the person who participated in survey 2020-04


     * **Success Response:**

        * **Code:** 200 <br />
          **Content:** 
          ```
            {"Persons":[
              {
                "email": "Sara Parker-304@eficode.com",
                "name": "Sara Parker-304"
              },
              {
                "email": "Sara Parker-858@eficode.com",
                "name": "Sara Parker-858"
              }]}
          ````
  *  **URL Params** <br />
    /surveys/survey-id/persons/person-id <br />
     ***Example:*** <br />
     /surveys/2020-04/persons/Sara%20Parker-304@eficode.com <br />
     It gives detail of the person with email at particular survey date of 2020-04
     
     * **Success Response:**

        * **Code:** 200 <br />
          **Content:** 
          ```
          {"Sara Parker-304@eficode.com": 
            {
              "Email": "Sara Parker-304@eficode.com",
              "Name": "Sara Parker-304",
              "Office": "Helsinki",
              "Team": "DB",
              "survey": [
                {"level": "Novice",
                "name": "Git"
                },
                {"level": "Intermediate",
                "name": "Docker"
                },
                {"level": "Expert",
                "name": "Circleci"
                },
                {"level": "Intermediate",
                "name": "Azure Devops"
                },
                {"level": "Expert",
                "name": "Robot Framework"}
              ]
            }
          }

          ````    

### **URL:** 
    
    `/persons`

* **Method:**
    
     `GET` 
  
*  **URL Params**

    None

* **Success Response:**<br />
    ***List all the person participated in all survey***


  * **Code:** 200 <br />
    **Content:** 
    ```
    {"Persons":[
                  {
                    "email": "Sara Parker-242@eficode.com",
                    "name": "Sara Parker-242"
                  },
                  {
                    "email": "Sara Parker-328@eficode.com",
                    "name": "Sara Parker-328"
                  }
                ]}
    ````
  *  **URL Params** <br />
    /persons/person-id/surveys <br />
     ***Example:*** <br />
     r/persons/Sara-Parker-484@eficode.com/surveys <br />
     List all surveys a given person have entered


     * **Success Response:**

        * **Code:** 200 <br />
          **Content:** 
          ```
            {
              "Sara Parker-484@eficode.com": {
              "Surveys": [{
              "0": "2020-03"
              }]}
            }
          ````
  *  **URL Params** <br />
    /persons/person-id/surveys/survey-id <br />
     ***Example:*** <br />
     r/persons/Sara-Parker-484@eficode.com/surveys/2020-03 <br />
     List all the survey data for the given person and the given survey

     * **Success Response:**

          * **Code:** 200 <br />
          **Content:** 
              ```
              {
                "Survey": [
                [
                {
                "level": "Fundamental Awareness",
                "name": "Docker"
                },
                {
                "level": "Novice",
                "name": "Jenkins"
                },
                {
                "level": "Intermediate",
                "name": "Circleci"
                },
                {
                "level": "Fundamental Awareness",
                "name": "Azure Devops"
                },
                {
                "level": "Expert",
                "name": "Artifactory"
                },
                {
                "level": "Intermediate",
                "name": "Robot Framework"
                }
                ]
                ],
                "email": "Sara Parker-484@eficode.com"
                }
              ````     
* **Error Response:** <br /> An Error Occured: {e} //e: error message