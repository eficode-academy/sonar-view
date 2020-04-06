# Backend 
## Directory Structure

`web/`: http functions, handle http request.
* `sonar_survey`: Take a csv file from `POST` request, convert to json, save to Firestore.
You could try with:
```
curl -F data=@[path to test csv] [API endpoint]
````

`background/` background tasks, execute the database related background task.