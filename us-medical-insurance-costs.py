#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs
# 
# In this project, a **CSV** file with medical insurance costs will be investigated using Python fundamentals. The goal with this project will be to analyze various attributes within **insurance.csv** to learn more about the patient information in the file and gain insight into potential use cases for the dataset.

# In[1]:


# import csv library
import csv


# To start, all necessary libraries must be imported. For this project the only library needed is the `csv` library in order to work with the **insurance.csv** data. There are other potential libraries that could help with this project; however, for this analysis, using just the `csv` library will suffice.

# The next step is to look through **insurance.csv** in order to get aquanted with the data. The following aspects of the data file will be checked in order to plan out how to import the data into a Python file:
# * The names of columns and rows
# * Any noticeable missing data
# * Types of values (numerical vs. categorical)

# In[2]:


#Create empty lists for the various attributes in insurance.csv
ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []


# **insurance.csv** contains the following columns:
# * Patient Age
# * Patient Sex 
# * Patient BMI
# * Patient Number of Children
# * Patient Smoking Status
# * Patient U.S Geopraphical Region
# * Patient Yearly Medical Insurance Cost
# 
# There are no signs of missing data. To store this information, seven empty lists will be created hold each individual column of data from **insurance.csv**.
# 

# In[14]:


# helper function to load csv data
def load_list_data(lst, csv_file, column_name):
    # open csv file
    with open(csv_file) as csv_info:
        # read the data from the csv file
        csv_dict = csv.DictReader(csv_info)
        # loop through the data in each row of the csv 
        for row in csv_dict:
            # add the data from each row to a list
            lst.append(row[column_name])
        # return the list
        return lst


# The helper function above was created to make loading data into the lists as efficient as possible. Without this function, one would have to open **insurance.csv** and rewrite the `for` loop seven times; however, with this function, one can simply call `load_list_data()` each time as shown below.

# In[16]:


# look at the data in insurance_csv_dict
load_list_data(ages, 'insurance.csv', 'age')
load_list_data(sexes, 'insurance.csv', 'sex')
load_list_data(bmis, 'insurance.csv', 'bmi')
load_list_data(num_children, 'insurance.csv', 'children')
load_list_data(smoker_statuses, 'insurance.csv', 'smoker')
load_list_data(regions, 'insurance.csv', 'region')
load_list_data(insurance_charges, 'insurance.csv', 'charges')


# Now that all the data from **insurance.csv** neatly organized into labeled lists, the analysis can be started. This is where one must plan out what to investigate and how to perform the analysis. There are many aspects of the data that could be looked into. The following operations will be implemented:
# * find average age of the patients
# * return the number of males vs. females counted in the dataset
# * find geographical location of the patients
# * return the average yearly medical charges of the patients
# * creating a dictionary that contains all patient information
# 
# To perform these inspections, a class called `PatientsInfo` has been built out which contains fives methods:
# * `analyze_ages()`
# * `analyze_sexes()`
# * `unique_regions()`
# * `average_charges()`
# * `create_dictionary()`
# 
# The class has been built out below. 

# In[24]:


class PatientsInfo:
    # init method that takes in each list parameter
    def __init__(self, patients_ages, patients_sexes, patients_bmis, patients_num_children, 
                 patients_smoker_statuses, patients_regions, patients_charges):
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_num_children = patients_num_children
        self.patients_smoker_statuses = patients_smoker_statuses
        self.patients_regions = patients_regions
        self.patients_charges = patients_charges

    # method that calculates the average ages of the patients in insurance.csv
    def analyze_ages(self):
        # initialize total age at zero
        total_age = 0
        # iterate through all ages in the ages list
        for age in self.patients_ages:
            # sum of the total age
            total_age += int(age)
        # return total age divided by the length of the patient list
        return ("Average Patient Age: " + str(round(total_age/len(self.patients_ages), 2)) + " years")

    # method that calculates the number of males and females in insurance.csv
    def analyze_sexes(self):
        # initialize number of males and females to zero
        females = 0
        males = 0
        # iterate through each sex in the sexes list
        for sex in self.patients_sexes:
            # if female add to female variable
            if sex == 'female':
                females += 1
            # if male add to male variable
            elif sex == 'male':
                males += 1
        # print out the number of each
        print("Count for female: ", females)
        print("Count for male: ", males)

    # method to find each unique region patients are from
    def unique_regions(self):
        # initialize empty list
        unique_regions = []
        # iterate through each region in regions list
        for region in self.patients_regions:
            # if the region is not already in the unique regions list
            # then add it to the unique regions list
            if region not in unique_regions: 
                unique_regions.append(region)
        # return unique regions list
        return unique_regions

    # method to find average yearly medical charges for patients in insurance.csv
    def average_charges(self):
        # initialize total_charges variable
        total_charges = 0
        # iterate through charges in patients charges list
        # add each charge to total_charge
        for charge in self.patients_charges:
            total_charges += float(charge)
        # return the average charges rounded to the hundredths place
        return ("Average Yearly Medical Insurance Charges: " +  
                str(round(total_charges/len(self.patients_charges), 2)) + " dollars.")
    
    # method to create dictionary with all patients information
    def create_dictionary(self):
        self.patients_dictionary = {}
        self.patients_dictionary["age"] = [int(age) for age in self.patients_ages]
        self.patients_dictionary["sex"] = self.patients_sexes
        self.patients_dictionary["bmi"] = self.patients_bmis
        self.patients_dictionary["children"] = self.patients_num_children
        self.patients_dictionary["smoker"] = self.patients_smoker_statuses
        self.patients_dictionary["regions"] = self.patients_regions
        self.patients_dictionary["charges"] = self.patients_charges
        return self.patients_dictionary


# The next step is to create an instance of the class called `patient_info`. With this instance, each method can be used to see the results of the analysis.

# In[25]:


patient_info = PatientsInfo(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)


# In[26]:


patient_info.analyze_ages()


# The average age of the patients in **insurance.csv** is about 39 years old. This is important to check in order to ensure the data in **insurance.csv** is representative for a broader population. If it is decided to use the dataset to make inferences about other populations, the data must abundant and broad enough for such use cases.
# 
# A further analysis would have to be done to make sure the [range](https://www.mathsisfun.com/data/range.html#:~:text=The%20Range%20is%20the%20difference,is%209%20%E2%88%92%203%20%3D%206.) and [standard deviation](https://www.mathsisfun.com/data/standard-deviation.html) of the patient age group in **insurance.csv** is indicative of a random sampling of individuals. 

# In[27]:


patient_info.analyze_sexes()


# The next step of the analysis is to check the balance of males vs. females in **insurance.csv**. Similar to above, it is important to check that this dataset is representative of a broader population of individuals. If a person were to use this dataset to create a classification model, it would be imperitive to make sure that the attributes are balanced.
# 
# Quite often in the real-world, data is not balanced; this is an issue because it can lead to statistical issues when performing analysis. This is something that will be explored further in future portfolio projects!

# In[28]:


patient_info.unique_regions()


# There are four unique geographical regions in this dataset, and it is important to note that all the patients come from the United States.

# In[29]:


patient_info.average_charges()


# The average yearly medical insurance charge per individual is 13270 US dollars. Some further analysis could be done to see what patient attributes contribute most strongly to low and/or high medical insurance charges. For example, one could check if patient age correlates with the amount of money they spend yearly.

# In[30]:


patient_info.create_dictionary()


# All patient data is now neatly organized in a dictionary. This is convenient for further analysis if a decision is made to continue making investigations for the attributes in **insurance.csv**.
