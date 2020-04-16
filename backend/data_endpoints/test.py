data = {
"0": "Sara Parker-141",
"1": "Sara Parker-344",
"2": "Sara Parker-371",
"3": "Sara Parker-570",
"4": "Sara Parker-676",
"5": "Sara Parker-710",
"6": "Sara Parker-761",
"7": "Sara Parker-865",
"8": "Sara Parker-912",
"9": "Sara Parker-934"
}
for key in data:
    survey_date = data[key]


survey = {
"Surveys": [
{
"0": "2020-03"
}
]
}

final_survey = {"abc@123.com": survey}

person = {
"Sara Parker-934": {
"Email": "Sara Parker-934@eficode.com",
"Name": "Sara Parker-934",
"Office": "Helsinki",
"Team": "DB",
"survey": [
{
"level": "Novice",
"name": "Git"
},
{
"level": "Intermediate",
"name": "Docker"
},
{
"level": "Expert",
"name": "Circleci"
},
{
"level": "Intermediate",
"name": "Azure Devops"
},
{
"level": "Expert",
"name": "Robot Framework"
}]}}

survey_item = person["Sara Parker-934"]["survey"]

survey_items = {}
survey_items["Survey"] = []
survey_items["email"] = person["Sara Parker-934"]["Email"]
survey_items["Survey"].append(survey_item)


print(survey_item)