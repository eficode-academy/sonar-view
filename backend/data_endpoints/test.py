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

namedata = {
"Persons": [
{
"email": "Sara Parker-141",
"name": "Sara Parker-141"
},
{
"email": "Sara Parker-344",
"name": "Sara Parker-344"
},
{
"email": "Sara Parker-371",
"name": "Sara Parker-371"
},
{
"email": "Sara Parker-570",
"name": "Sara Parker-570"
},
{
"email": "Sara Parker-676",
"name": "Sara Parker-676"
},
{
"email": "Sara Parker-710",
"name": "Sara Parker-710"
},
{
"email": "Sara Parker-761",
"name": "Sara Parker-761"
},
{
"email": "Sara Parker-865",
"name": "Sara Parker-865"
},
{
"email": "Sara Parker-912",
"name": "Sara Parker-912"
},
{
"email": "Sara Parker-934",
"name": "Sara Parker-934"
},
{
"email": "Sara Parker-484@eficode.com",
"name": "Sara Parker-484"
},
{
"email": "Sara Parker-721@eficode.com",
"name": "Sara Parker-721"
},
{
"email": "Sara Parker-192@eficode.com",
"name": "Sara Parker-192"
},
{
"email": "Sara Parker-304@eficode.com",
"name": "Sara Parker-304"
},
{
"email": "Sara Parker-404@eficode.com",
"name": "Sara Parker-404"
},
{
"email": "Sara Parker-500@eficode.com",
"name": "Sara Parker-500"
},
{
"email": "Sara Parker-608@eficode.com",
"name": "Sara Parker-608"
},
{
"email": "Sara Parker-858@eficode.com",
"name": "Sara Parker-858"
},
{
"email": "jane@doe.com",
"name": "Jane Doe"
},
{
"email": "john@doe.com",
"name": "John Doe"
},
{
"email": "jane@doe.com",
"name": "Jane Doe"
},
{
"email": "john@doe.com",
"name": "John Doe"
},
{
"email": "jane@doe.com",
"name": "Jane Doe"
},
{
"email": "john@doe.com",
"name": "John Doe"
},
{
"email": "Sara Parker-242@eficode.com",
"name": "Sara Parker-242"
},
{
"email": "Sara Parker-328@eficode.com",
"name": "Sara Parker-328"
},
{
"email": "Sara Parker-798@eficode.com",
"name": "Sara Parker-798"
},
{
"email": "Sara Parker-850@eficode.com",
"name": "Sara Parker-850"
}
]
}


abc = list({v['email']:v for v in namedata["Persons"]}.values())
abcd = {
"surveys": [
{
"0": "2020-04"
},
{
"1": "2020-11"
},
{
"2": "2021-04"
}
]
}

for item in abcd['surveys']:
    coll_list = item.values()
    coll_name = ''.join(coll_list)
    print(coll_name)
