import io
import csv
import matplotlib.pyplot as plt

total_female = []
female_live_year = []

# this is to open the file
file_to_open = io.open("TotalCitizen.csv", 'r', encoding="utf-8-sig")
input_file = csv.reader(file_to_open, delimiter=",")

for row in input_file:
    if row[0] == "year" and row[1] == "level_1" and row[2] == "level_2" and row[3] == "value":
        print("Header row: ", row)
    else:
        if row[1] == "Total Female Citizens" and row[2] == "40 - 44 Years":
            female_live_year.append(int(row[0]))
            total_female.append(int(row[3]))
        #else:
            female_live_year.append(int(row[0]))
            if row[3] == "na":
                total_female.append(0)
            else:
                total_female.append(int(row[3]))

plt.bar(female_live_year,total_female,color='r')
plt.xlabel('year')
plt.ylabel('value')
plt.title('Total Female Citizen Aged 40-44 by Year')
plt.show()