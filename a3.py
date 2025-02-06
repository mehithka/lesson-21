student_data = {'id1' :
                {"name" : ['sara'],
                 'class':['V'],
                 'subject_integration':['english, maths , science']},

                 'id2': {'name': ['David'],
                         'class':['V'],
                         'subject_integration':['english,literature,science']},
                
                 'id3': {'name': ['David'],
                         'class':['V'],
                         'subject_integration':['english,literature,science']},
                 'id4': {'name':['mohith'],
                         'class':['VI'],
                         'subject_integration':'maths,computer science,physics,english'}}
result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)