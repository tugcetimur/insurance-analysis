{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "c203c5ea-ac8e-4084-96c4-70268cdbbe4d",
   "metadata": {},
   "source": [
    "# U.S. Medical Insurance Costs"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7b93fdc1-8d7a-4f74-b536-38c03329198d",
   "metadata": {},
   "source": [
    "In this project, a **CSV** file with medical insurance costs will be investigated using Python fundamentals. The goal with this project will be to analyze various attributes within **insurance.csv** to learn more about the patient information in the file and gain insight into potential use cases for the dataset."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "f65fa7c1-8ac5-4d26-82f1-c5e3edf8535f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "17782653-2d25-410f-9f21-403df1dfdd30",
   "metadata": {},
   "source": [
    "Key Questions Explored:\n",
    "1-What is the average medical insurance charge?\n",
    "2-How do insurance charges differ between smokers and non-smokers?\n",
    "3-Is there a difference in charges based on gender?\n",
    "4-What is the relationship between age and insurance charges?\n",
    "5-Impact of BMI on Charges\n",
    "6-Effect of Number of Children on Charges\n",
    "7-Charges by Region\n",
    "8-Combine Multiple Factors: Smoker & BMI\n",
    "9-Predict Charges Based on Age and BMI (Mini Model)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f663c840-7adc-482d-9ac1-ca5fa9536c70",
   "metadata": {},
   "source": [
    "📌 1. What is the average medical insurance charge?\n",
    "#In this section, we calculate the average cost of medical insurance across all individuals in the dataset.\n",
    "#This provides a baseline for comparing groups such as smokers vs non-smokers, or males vs females.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 243,
   "id": "ea4e3e13-8c46-48b8-8dd7-29f23dfd5739",
   "metadata": {},
   "outputs": [],
   "source": [
    "class InsuranceAnalysis:\n",
    "    def __init__(self, filepath):\n",
    "        \"\"\"Reads CSV file and assigns all data to lists\"\"\"\n",
    "        self.age = []\n",
    "        self.sex = []\n",
    "        self.bmi = []\n",
    "        self.children = []\n",
    "        self.smoker = []\n",
    "        self.region = []\n",
    "        self.charges = []\n",
    "        self.load_data(filepath)\n",
    "\n",
    "    def load_data(self, filepath):\n",
    "            \"\"\"Loads data from CSV file\"\"\"\n",
    "            with open(filepath, newline='') as file:\n",
    "                reader = csv.DictReader(file)\n",
    "                for row in reader:\n",
    "                    self.age.append(int(row['age']))\n",
    "                    self.sex.append(row['sex'])\n",
    "                    self.bmi.append(float(row['bmi']))\n",
    "                    self.children.append(int(row['children']))\n",
    "                    self.smoker.append(row['smoker'])\n",
    "                    self.region.append(row['region'])\n",
    "                    self.charges.append(float(row['charges'])) \n",
    "                    \n",
    "    def average_medical_charge(self):\n",
    "        \"\"\"Returns the average of insurances.\"\"\"\n",
    "        return round(sum(self.charges) / len(self.charges),2)\n",
    "        \n",
    "    def analyze_ages(self):\n",
    "        \"\"\"Calculate the average of patient ages.\"\"\"\n",
    "        return round((sum(self.age)/len(self.age)), 2) \n",
    "        \n",
    "    def count_total_patients(self):\n",
    "        \"\"\"Returns the total number of patients.\"\"\"\n",
    "        return len(self.age)\n",
    "        \n",
    "    def analyze_sexes(self):\n",
    "        \"\"\"Return the count of genders.\"\"\"\n",
    "        female_count = 0\n",
    "        male_count = 0\n",
    "        for sex in self.sex:\n",
    "            if sex == 'female':\n",
    "                female_count += 1\n",
    "            elif sex == 'male':\n",
    "                male_count += 1\n",
    "        return {\n",
    "            'female_count': female_count,\n",
    "            'male_count': male_count\n",
    "        }\n",
    "        \n",
    "    def charge_by_smoker_status(self):\n",
    "        \"\"\"Return the charge avg according to smokers and non-smokers.\"\"\"\n",
    "        smoker_charges=[]\n",
    "        non_smoker_charges=[]\n",
    "        \n",
    "        for charge, smoker_status in zip(self.charges, self.smoker):\n",
    "            if smoker_status == 'yes':\n",
    "                smoker_charges.append(charge)\n",
    "            else:\n",
    "                non_smoker_charges.append(charge)\n",
    "\n",
    "        return {\n",
    "            'smokers_avg': round(sum(smoker_charges) / len(smoker_charges), 2),\n",
    "            'non_smokers_avg': round(sum(non_smoker_charges) / len(non_smoker_charges), 2)\n",
    "        }\n",
    "\n",
    "    def charges_by_gender(self):\n",
    "        \"\"\"Calculate average insurance cost by gender.\"\"\"\n",
    "        female_charges = []\n",
    "        male_charges = []\n",
    "\n",
    "        for sex, charge in zip(self.sex, self.charges):\n",
    "            if sex == 'female':\n",
    "                female_charges.append(charge)\n",
    "            elif sex == 'male':\n",
    "                male_charges.append(charge)\n",
    "            else:\n",
    "                print(\"No sex data\")\n",
    "        return {\n",
    "            'female_avg': round(sum(female_charges) / len(female_charges), 2),\n",
    "            'male_avg': round(sum(male_charges) / len(male_charges), 2)\n",
    "        }\n",
    "        \n",
    "    def average_charge_by_bmi(self):\n",
    "        \"\"\"Examines the effect of BMI on insurance costs (over 30bmi is considered risky).\"\"\"\n",
    "        low_bmi = [c for c, b in zip(self.charges, self.bmi) if b < 30]\n",
    "        high_bmi = [c for c, b in zip(self.charges, self.bmi) if b >= 30]\n",
    "        return {\n",
    "            \"BMI<30\": sum(low_bmi) / len(low_bmi),\n",
    "            \"BMI>=30\": sum(high_bmi) / len(high_bmi)\n",
    "        }\n",
    "        \n",
    "    def charges_by_region(self):\n",
    "        \"\"\"Return the charge avg according to regions.\"\"\"\n",
    "        region_group = {}\n",
    "        for r, c in zip(self.region, self.charges):\n",
    "            if r not in region_group:\n",
    "                region_group[r] = []\n",
    "            region_group[r].append(c)\n",
    "        return {r: sum(cs)/len(cs) for r, cs in region_group.items()}\n",
    "\n",
    "    def charges_by_smoker_and_bmi(self):\n",
    "        \"\"\"Return average charges for combined smoker & BMI categories.\"\"\"\n",
    "        smoker_high_bmi = []\n",
    "        smoker_low_bmi = []\n",
    "        non_smoker_high_bmi = []\n",
    "        non_smoker_low_bmi = []\n",
    "    \n",
    "        for smoker_status, bmi_value, charge in zip(self.smoker, self.bmi, self.charges):\n",
    "            if smoker_status == 'yes' and bmi_value >= 30:\n",
    "                smoker_high_bmi.append(charge)\n",
    "            elif smoker_status == 'yes' and bmi_value < 30:\n",
    "                smoker_low_bmi.append(charge)\n",
    "            elif smoker_status == 'no' and bmi_value >= 30:\n",
    "                non_smoker_high_bmi.append(charge)\n",
    "            elif smoker_status == 'no' and bmi_value < 30:\n",
    "                non_smoker_low_bmi.append(charge)\n",
    "    \n",
    "        return {\n",
    "            'Smoker & BMI >= 30': round(sum(smoker_high_bmi) / len(smoker_high_bmi), 2),\n",
    "            'Smoker & BMI < 30': round(sum(smoker_low_bmi) / len(smoker_low_bmi), 2),\n",
    "            'Non-smoker & BMI >= 30': round(sum(non_smoker_high_bmi) / len(non_smoker_high_bmi), 2),\n",
    "            'Non-smoker & BMI < 30': round(sum(non_smoker_low_bmi) / len(non_smoker_low_bmi), 2)\n",
    "        }"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 244,
   "id": "f9ddc1fa-4959-4881-b5e7-0b01e129aac1",
   "metadata": {},
   "outputs": [],
   "source": [
    "analyzer = InsuranceAnalysis('insurance.csv')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "28b713a5-ba48-49d9-9cf0-2abcceda40cb",
   "metadata": {},
   "source": [
    "### Question1: What is the average medical insurance cost for patients in the dataset?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 232,
   "id": "ede58e71-6d5b-43f0-ab6c-0feeea0a38ea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Average charge: 13270.42\n"
     ]
    }
   ],
   "source": [
    "print(\"Average charge:\", analyzer.average_medical_charge())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f09517a6-1106-45a8-99e9-c34bd62f263e",
   "metadata": {},
   "source": [
    " The average charge gives an idea of the general cost burden per patient. This is useful to benchmark other subgroup costs."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3e3cb996-1d3c-49c5-9c36-f10431b96ab3",
   "metadata": {},
   "source": [
    "### Question 2: Is there a significant difference in insurance charges between smokers and non-smokers?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 234,
   "id": "6ecf47b3-ad39-4a96-8f39-c0593d2c20de",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Charges by Smoker Status: {'smokers_avg': 32050.23, 'non_smokers_avg': 8434.27}\n"
     ]
    }
   ],
   "source": [
    "print(\"Charges by Smoker Status:\", analyzer.charge_by_smoker_status())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4818814b-1b86-4341-829f-d92da37fade5",
   "metadata": {},
   "source": [
    "This analysis helps demonstrate the financial risk that smoking adds to healthcare costs, often used to justify higher premiums for smokers."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9d896627-122f-4ade-818b-6f3d66b9bb90",
   "metadata": {},
   "source": [
    "### Question 3: Do male and female patients have different average insurance costs?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 235,
   "id": "89152d64-0fac-4667-bb20-10f580beb576",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Average Charges by Gender: {'female_avg': 12569.58, 'male_avg': 13956.75}\n"
     ]
    }
   ],
   "source": [
    "print(\"Average Charges by Gender:\", analyzer.charges_by_gender())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6ff25175-35d5-4a7f-8344-da84df4745de",
   "metadata": {},
   "source": [
    "By comparing male and female averages, we can investigate if gender is a factor influencing medical insurance pricing."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a70c4967-6477-4bc6-91fd-97752e40bfa3",
   "metadata": {},
   "source": [
    "### Question 4: What is the average age of patients, and how does it relate to insurance charges?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 236,
   "id": "381a9941-0c6e-4aa2-93d7-e7104a3354a9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Average Age of Patients: 39.21\n"
     ]
    }
   ],
   "source": [
    "print(\"Average Age of Patients:\", analyzer.analyze_ages())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f91bc616-50e3-41d8-8318-e27288863848",
   "metadata": {},
   "source": [
    "Aging often correlates with higher healthcare needs. Understanding the average age helps relate it to average charges and risk"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "141ded1f-50b5-4c11-a4ed-a2634c6f8854",
   "metadata": {},
   "source": [
    "### Question 5: Do individuals with higher BMI values incur higher insurance costs?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 237,
   "id": "c661afb7-62bc-43b2-8b54-df1be94ef8c4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Average Charges by BMI Category: {'BMI<30': 10713.666900584785, 'BMI>=30': 15552.335468868458}\n"
     ]
    }
   ],
   "source": [
    "print(\"Average Charges by BMI Category:\", analyzer.average_charge_by_bmi())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4b149c0a-df61-49d4-bb5d-7b4bc1aaa171",
   "metadata": {},
   "source": [
    "BMI is an important health indicator. Individuals with BMI ≥ 30 are categorized as obese, often associated with chronic diseases and higher medical expenses."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "18b12927-4414-48c2-a95d-5de30868916e",
   "metadata": {},
   "source": [
    "### Question 6: How do average insurance charges vary by geographical region?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 239,
   "id": "9396db49-3966-412b-9a1a-e49746fddc96",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Average Charges by Region: {'southwest': 12346.937377292308, 'southeast': 14735.41143760989, 'northwest': 12417.575373969232, 'northeast': 13406.384516385804}\n"
     ]
    }
   ],
   "source": [
    "print(\"Average Charges by Region:\", analyzer.charges_by_region())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0183b89f-814c-4926-9c7e-a711f56afd56",
   "metadata": {},
   "source": [
    "Regional analysis may reflect different healthcare access levels, cost of living, or lifestyle patterns affecting insurance pricing."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4bc6a5af-6c5f-43c5-8b82-f8f0f8201271",
   "metadata": {},
   "source": [
    "### Question 7: What are the average insurance charges for people based on both their smoking status and BMI category?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 246,
   "id": "f78eadae-8981-4645-88b9-36027ba5564b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Charges by Combined Smoker & BMI Categories:\n",
      "{'Smoker & BMI >= 30': 41557.99, 'Smoker & BMI < 30': 21363.22, 'Non-smoker & BMI >= 30': 8842.69, 'Non-smoker & BMI < 30': 7977.03}\n"
     ]
    }
   ],
   "source": [
    "print(\"Charges by Combined Smoker & BMI Categories:\")\n",
    "print(analyzer.charges_by_smoker_and_bmi())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ef8962bf-6472-4b31-aab2-44371159a416",
   "metadata": {},
   "source": [
    "Combining both smoker status and BMI provides a deeper understanding of how overlapping health risk factors contribute to insurance costs. Smokers with high BMI are likely to incur the highest charges, making them a high-risk group for insurance providers."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4165b381-a3c0-4887-8eea-09835bea0cf4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
