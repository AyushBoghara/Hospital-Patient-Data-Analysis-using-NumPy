"""

|******************************|
|Hospital Patient Data Analysis|
|******************************|

Project Question:

                A hospital collects data about 20 patients admitted in a month. For each patient, 
                the following details are stored in a NumPy array:
                    Age (in years)      
                    Blood Pressure (mmHg)
                    Heart Rate (bpm)
                    Hospital Stay Duration (in days)
                    
                Your tasks using NumPy:
                    👉 Create the Dataset:
                        1. Generate a (20×4) NumPy array with random integers:
                            Age: 20–80
                            Blood Pressure: 90–160
                            Heart Rate: 60–120
                            Stay Duration: 1–15 days
                        2. Print the dataset.
                    👉 Basic Analysis:
                        3. Find the average age of patients.
                        4. Find the maximum and minimum blood pressure.
                        5. Count how many patients had a heart rate above 100 bpm.
                    👉 Advanced Analysis:
                        6. Identify the patient with the longest hospital stay.
                        7. Normalize all features (columns) between 0 and 1.
                        8. Sort patients by age in ascending order.
                    👉 Extra Challenge:
                        9. Add a new column for Hospital Charges (random values between 5000–50000).
                        10. Save the dataset into a .npy file, then load it back and display.

👉 Your task: Solve all of the above using NumPy only.
"""

import numpy as np
# 1. create a dataset 
patients = np.array([
    [73, 139, 105,  9],
    [46, 140, 102, 11],
    [40, 121, 117,  7],
    [25, 116, 112, 11],
    [38,  99, 102,  7],
    [68, 128, 118,  5],
    [74, 103,  68, 10],
    [74, 125,  64, 11],
    [80, 155,  62,  1],
    [51,  99,  69,  3],
    [31, 160,  62,  6],
    [70,  95,  95,  3],
    [42,  96, 115,  5],
    [57, 103,  88,  6],
    [55, 101,  80,  8],
    [39, 109, 111, 15],
    [48,  97,  72, 13],
    [69, 154,  63,  5],
    [63, 128,  91,  9],
    [80, 106,  99,  3]
])
# 2. Print the dataset.
print(patients)

# 3. Find the average age of patients.
patients_avg = np.mean(patients,axis=0)
print("Average age of patients :",patients_avg[0])

# 4. Find the maximum and minimum blood pressure.
patients_min = np.min(patients,axis=0)
patients_max = np.max(patients,axis=0)

print("Minimum blood pressure :",patients_min[1])
print("Maximum blood pressure :",patients_max[1])

# 5. Count how many patients had a heart rate above 100 bpm.
# Select the Heart Rate column (index 2)
heart_rates = patients[:, 2]

# Count how many are > 100
count_high_hr = np.sum(heart_rates > 100)
print("Number of patients with heart rate above 100 bpm:", count_high_hr)

# 6. Identify the patient with the longest hospital stay.
patients_longest_hospital_stay = patients[:, 3]

longest_stay = np.max(patients_longest_hospital_stay) 
patient_index = np.argmax(patients_longest_hospital_stay)
patient_with_longest_stay = patients[patient_index]

print("Longest Hospital Stay:", longest_stay, "days")
print("Patient details (Age, BP, Heart Rate, Stay):", patient_with_longest_stay)

# 8. Sort patients by age in ascending order.
patients_age = patients[:, 0]
patient_sort = np.sort(patients_age)
print("Sort patients by age in ascending order :" ,patient_sort)

# 9. Add a new column for Hospital Charges (random values between 5000–50000).
hospital_charges = np.random.randint(5000,50000,size=(20,1))
final_patients_lists = np.hstack((patients,hospital_charges))
print("Add new colmn For Hospital Charges \n",final_patients_lists)

# 10. 
np.save('patient_data.npy', final_patients_lists)
loaded_data = np.load('patient_data.npy')
print("\nSuccessfully loaded data from .npy file.")