#import library csv to import the dataset in my python script
import csv

file_direction = 'G:\Mi unidad\Estudis\Data science\CodeAcademy\Portfoli\Medical Insurance Costs Dataset\python-portfolio-project-starter-files\python-portfolio-project-starter-files\insurance.csv'
fieldnames = ['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges']
ages = []
sexs = []
bmis = []
childrens = []
smokers = [] 
regions = []
charges = []
medical_insurance_dict = {}

with open(file_direction, 'r', encoding='utf8') as insurance_data:
    reader = csv.DictReader(insurance_data, fieldnames=fieldnames)
    line_for = 0
    id=0
    for insurance_row in reader:
        if line_for != 0:
            ages.append(insurance_row['age'])
            sexs.append(insurance_row['sex'])
            bmis.append(insurance_row['bmi'])
            childrens.append(insurance_row['children'])
            smokers.append(insurance_row['smoker'])
            regions.append(insurance_row['region'])
            charges.append(insurance_row['charges'])
            medical_insurance_dict[id]=insurance_row
            id+=1
        else:
            line_for+=1

def totalSex(list_sexs):
    male = 0
    female = 0
    for sex in list_sexs:
        if sex == 'male':
            male += 1
        else:
            female +=1
    print ('There are {male} male and {female} female.'.format(male=male, female = female))
    return male, female

def totalSmoker(list_smokers):
    smoker = 0
    nonSmoker = 0
    for person in list_smokers:
        if person == 'yes':
            smoker += 1
        else:
            nonSmoker +=1
    print ('There are {smoker} smokers and {nonSmoker} non smokers.'.format(smoker=smoker, nonSmoker = nonSmoker))
    return smoker, nonSmoker

def numberAverage (list_int):
    total=0
    average = 0
    for age in list_int:
        average += float(age)
    average = round(average/len(list_int),2)
    print('The average es {average}'.format(average=average))
    return average

def personsForRegions(list_regions):
    people_for_region = {}
    unique_regions = []
    for region in list_regions:
        if not unique_regions.count(region):
            unique_regions.append(region)
    for unique_region in unique_regions:
        people_for_region[unique_region] = list_regions.count(unique_region)
        print(people_for_region[unique_region])
    print (people_for_region)
    return people_for_region

def averageBMIforSex(dictionary):
    count_male = 0
    count_female = 0
    bmi_male = 0
    bmi_female = 0
    for insurance_user in dictionary.values():        
        if insurance_user['sex'] == 'female':
            count_female+=1
            bmi_female+= float(insurance_user['bmi'])
        else:
            count_male+=1
            bmi_male+= float(insurance_user['bmi'])
    average_bmi_male = round(bmi_male/count_male,2)
    average_bmi_female = round(bmi_female/count_female,2)
    print('The bmi male average is {average_bmi_male} and the bmi female average is {average_bmi_female}.'.format(average_bmi_female=average_bmi_female, average_bmi_male=average_bmi_male))
    return average_bmi_male, average_bmi_female

def averageChargesforSex(dictionary):
    count_male = 0
    count_female = 0
    charge_male = 0
    charge_female = 0
    for insurance_user in dictionary.values():        
        if insurance_user['sex'] == 'female':
            count_female+=1
            charge_female+= float(insurance_user['charges'])
        else:
            count_male+=1
            charge_male+= float(insurance_user['charges'])
    average_charge_male = round(charge_male/count_male,2)
    average_charge_female = round(charge_female/count_female,2)
    print('The charge male average is {average_charge_male} and the charge female average is {average_charge_female}.'.format(average_charge_female=average_charge_female, average_charge_male=average_charge_male))
    return average_charge_male, average_charge_female

def averageSmokerforSex(dictionary):
    count_male = 0
    count_female = 0
    smoker_male = 0
    smoker_female = 0
    non_smoker_male = 0
    non_smoker_female = 0
    for insurance_user in dictionary.values():        
        if insurance_user['sex'] == 'female':
            count_female+=1
            if insurance_user['smoker']=='yes':
                smoker_female+= 1
            else :
                non_smoker_female+=1
        else:
            count_male+=1
            if insurance_user['smoker']=='yes':
                smoker_male+= 1
            else :
                non_smoker_male+=1
    average_smoker_male = round(smoker_male/count_male,2)*100
    average_smoker_female = round(smoker_female/count_female,2)*100
    print('The smoker male average is {average_smoker_male}% and the bmi female average is {average_smoker_female}%.'.format(average_smoker_female=average_smoker_female, average_smoker_male=average_smoker_male))
    return average_smoker_male, average_smoker_female

def averageBmiforSmoker(dictionary):
    count_smoker = 0
    count_non_smoker = 0
    non_smoker_bmi = 0
    smoker_bmi = 0
    for insurance_user in dictionary.values():        
        if insurance_user['smoker'] == 'yes':
            count_smoker+=1
            smoker_bmi += float(insurance_user['bmi'])
        else:
            count_non_smoker+=1
            non_smoker_bmi += float(insurance_user['bmi'])
           
    average_smoker_bmi = round(smoker_bmi/count_smoker,2)
    average_non_smoker_bmi = round(non_smoker_bmi/count_non_smoker,2)
    print('The smoker bmi average is {average_smoker_bmi} and the non skmoker bmi average is {average_non_smoker_bmi}.'.format(average_non_smoker_bmi=average_non_smoker_bmi, average_smoker_bmi=average_smoker_bmi))
    return average_smoker_bmi, average_non_smoker_bmi

def calcPercentage(val1,val2):
    percentage = round((float(val1)/float(val2)*100)-100,2)
    print('The percentatge betwen {val1} and {val2} is {percentage}'.format(val1=val1, val2=val2, percentage=percentage))
    return percentage

total_male, total_female = totalSex(sexs)
# There are 676 male and 662 female. This is a good samble because we have more less the same amount of male a female.
age_average = numberAverage(ages)
# The age average is 39.21 years
bmi_average = numberAverage(bmis)
# The age average is 30.66 years
total_smoker, total_nonSmoker = totalSmoker(smokers)
#There are 274 smokers and 1064 non smokers. We only have 1/4 part of smokers on all samble
users_region = personsForRegions(regions)
#There are 325 users in southwest, 364 in southeast, 325 in northwest and 324 in notheast. This is a good samble because we have the same amount of people divided in the 4 regions
average_bmi_male, average_bmi_female = averageBMIforSex(medical_insurance_dict)
#The bmi male average is 30.94 and the bmi female average is 30.38. The bmis average are the same for male and female. There aren't significant diferences between this two targets.
average_charge_male, average_charge_female = averageChargesforSex(medical_insurance_dict)
#The charge male average is 13956.75 and the bmi female average is 12569.58.
percentage_charges_sex = calcPercentage(average_charge_male, average_charge_female)
#The charges in males is over 11.04 more than female. This value means than males spends more in medical insurance than female
average_smoker_male, average_smoker_female = averageSmokerforSex(medical_insurance_dict)
#The smoker male average is 24.0% and the bmi female average is 17.0%. The male smokes more than female, the difference between this two targets is 7%. It's possible that this was the reason because the chargers are highers for male.
average_smoker_bmi, average_non_smoker_bmi = averageBmiforSmoker(medical_insurance_dict)
#The smoker bmi average is 30.71 and the non skmoker bmi average is 30.65. The difference between bmi's smokers and non smokers is too low for make a difference in charges.