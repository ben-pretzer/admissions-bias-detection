import random
import csv

UT_enrollement = {"White Male": 16.4, "White Female": 20.3, "Asian Male": 9.8, "Asian Female": 10.8, "Black or African American Male": 1.5, "Black or African American Female": 2.8, "Hispanic or Latino Male": 9.6, "Hispanic or Latino Female": 14.5, "Two or More Races Male": 1.5, "Two or More Races Female": 2.2, "American Indian or Alaskan Native Male": 0.1, "American Indian or Alaskan Native Female": 0.05}
UT_graduation = {"White Male": 20.3, "White Female": 23.1, "Asian Male": 9.56, "Asian Female": 9.47, "Black or African American Male": 1.47, "Black or African American Female": 2.33, "Hispanic or Latino Male": 8.31, "Hispanic or Latino Female": 11.8, "Two or More Races Male": 1.52, "Two or More Races Female": 1.65, "American Indian or Alaskan Native Male": 0.1, "American Indian or Alaskan Native Female": 0.03}

def create_csv(csv_name,UT_dict,num_rows):

    data = []

    header_names = ['Gender', 'Race']



    for i in range(0,num_rows):
        dict_temp = {}
        rand_num = random.uniform(0,100)
        sum = 0

        if rand_num <= UT_dict['American Indian or Alaskan Native Female']:
            dict_temp['Gender'] = 'Female'
            dict_temp['Race'] = 'American Indian or Alaskan Native'
            data.append(dict_temp)
            continue
        sum += UT_dict['American Indian or Alaskan Native Female']
        if rand_num <= (sum + UT_dict['American Indian or Alaskan Native Male']):
            dict_temp['Gender'] = 'Male'
            dict_temp['Race'] = 'American Indian or Alaskan Native'
            data.append(dict_temp)
            continue
        sum += UT_dict['American Indian or Alaskan Native Male']
        if rand_num <= (sum + UT_dict['Two or More Races Male']):
            dict_temp['Gender'] = 'Male'
            dict_temp['Race'] = 'Two or More Races'
            data.append(dict_temp)
            continue
        sum += UT_dict['Two or More Races Male']
        if rand_num <= (sum + UT_dict['Two or More Races Female']):
            dict_temp['Gender'] = 'Female'
            dict_temp['Race'] = 'Two or More Races'
            data.append(dict_temp)
            continue
        sum += UT_dict['Two or More Races Female']
        if rand_num <= (sum + UT_dict['Black or African American Male']):
            dict_temp['Gender'] = 'Male'
            dict_temp['Race'] = 'Black or African American'
            data.append(dict_temp)
            continue
        sum += UT_dict['Black or African American Male']
        if rand_num <= (sum + UT_dict['Black or African American Female']):
            dict_temp['Gender'] = 'Female'
            dict_temp['Race'] = 'Black or African American'
            data.append(dict_temp)
            continue
        sum += UT_dict['Black or African American Female']
        if rand_num <= (sum + UT_dict['Hispanic or Latino Male']):
            dict_temp['Gender'] = 'Male'
            dict_temp['Race'] = 'Hispanic or Latino'
            data.append(dict_temp)
            continue
        sum += UT_dict['Hispanic or Latino Male']
        if rand_num <= (sum + UT_dict['Hispanic or Latino Female']):
            dict_temp['Gender'] = 'Female'
            dict_temp['Race'] = 'Hispanic or Latino'
            data.append(dict_temp)
            continue
        sum += UT_dict['Hispanic or Latino Female']
        if rand_num <= (sum + UT_dict['Asian Male']):
            dict_temp['Gender'] = 'Male'
            dict_temp['Race'] = 'Asian'
            data.append(dict_temp)
            continue
        sum += UT_dict['Asian Male']
        if rand_num <= (sum + UT_dict['Asian Female']):
            dict_temp['Gender'] = 'Female'
            dict_temp['Race'] = 'Asian'
            data.append(dict_temp)
            continue
        sum += UT_dict['Asian Female']
        if rand_num <= (sum + UT_dict['White Male']):
            dict_temp['Gender'] = 'Male'
            dict_temp['Race'] = 'White'
            data.append(dict_temp)
            continue
        sum += UT_dict['White Male']
        if rand_num <= 100:
            dict_temp['Gender'] = 'Female'
            dict_temp['Race'] = 'White'
            data.append(dict_temp)

    with open(csv_name, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header_names)
        writer.writeheader()
        writer.writerows(data)


create_csv('UT_enrollment.csv',UT_enrollement,10000)
create_csv('UT_grad.csv',UT_graduation,5000)






