import random
import csv

data = []

header_names = ['Gender', 'Race', 'Financial Aid', 'Age', 'Year']


for i in range(0,1000):
    dict_temp = {}

    rand_num = random.randrange(0,100)

    # Gender
    if rand_num <= 21:
        dict_temp['Gender'] = 'Male'
    elif rand_num <= 100:
        dict_temp['Gender'] = 'Female'

    rand_num = random.randrange(0, 100)

    # Race

    if rand_num <= 3:
        dict_temp['Race'] = 'Black or African American'
    elif rand_num <= 20:
        dict_temp['Race'] = 'Asian'
    elif rand_num <= 48:
        dict_temp['Race'] = 'Hispanic or Latino'
    else:
        dict_temp['Race'] = 'White'

    rand_num = random.randrange(0, 100)

    # Financial Aid
    if rand_num <= 65:
        dict_temp['Financial Aid'] = 'Yes'
    elif rand_num <= 100:
        dict_temp['Financial Aid'] = 'No'

    #rand_num = random.randrange(0, 100)

    # Convict
    # if rand_num <= 70:
    #     dict_temp['Convict'] = 'True'
    # elif rand_num <= 100:
    #     dict_temp['Convict'] = 'False'

    rand_num = random.randrange(18, 23)

    # Age
    dict_temp['Age'] = rand_num

    rand_num = random.randrange(0, 100)

    # Year

    if rand_num <= 10:
        dict_temp['Year'] = 'Freshmen'
    elif rand_num <= 30:
        dict_temp['Year'] = 'Sophomore'
    elif rand_num <= 60:
        dict_temp['Year'] = 'Junior'
    else:
        dict_temp['Year'] = 'Senior'

   # rand_num = random.randrange(0, 100)

    # Continent

    # if rand_num <= 10:
    #     dict_temp['Continent'] = 'Antarctica'
    # elif rand_num <= 30:
    #     dict_temp['Continent'] = 'Africa'
    # elif rand_num <= 60:
    #     dict_temp['Continent'] = 'Europe'
    # else:
    #     dict_temp['Continent'] = 'Asia'
    #
    data.append(dict_temp)


with open('unbiased_graduation.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=header_names)
    writer.writeheader()
    writer.writerows(data)













