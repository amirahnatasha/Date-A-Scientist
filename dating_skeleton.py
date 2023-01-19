import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#Create your df here:
df = pd.read_csv("profiles.csv")

print(df.job.head())

# Dsitribution of age
# plt.hist(df.age, bins= 20)
# plt.xlabel("Age")
# plt.ylabel("Frequency")
# plt.xlim(16, 80)
# plt.show()

# possible values of zodiac signs
df.sign.value_counts()

drink_mapping = {"not at all":0, "rarely":1, "socially": 2, "often": 3, "very often": 4, "desperately": 5}

df["drinks_code"] = df.drinks.map(drink_mapping)

# print(df.drinks_code.head())
# print(df.smokes.value_counts())

smokes_mapping = {"no" : 0, "sometimes": 1, "when drinking": 2, "yes": 3, "trying to quit": 4}
df["smokes_code"] = df.smokes.map(smokes_mapping)

# print(df.smokes_code.head())
print(df.drugs.value_counts())

drugs_mapping = {"never": 0, "sometimes": 1, "often": 2}
df["drugs_code"] = df.drugs.map(drugs_mapping)

# print(df.drugs_code.head())
# Need to remove NaN in drugs_code

# print(df.sex.value_counts())

sex_mapping = {"m": 0, "f" : 1}
df["sex_code"] = df.sex.map(sex_mapping)

#print(df.sex_code.head())
# print(df.income.value_counts())
# print(df.height.value_counts())
# print(df.religion.value_counts())
# print(df.status.value_counts())
# print(df.education.value_counts())
# print(df.pets.value_counts())
# print(df.diet.value_counts())
# print(df.sign.value_counts())


status_mapping = {"unknown" : 0, "available": 1, "single": 2, "seeing someone": 3, "married": 4}
df["status_code"] = df.status.map(status_mapping)

# print(df.status_code.head())


