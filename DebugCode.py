# Expected Output
# Patient's BMI is: 21.604938271604937
# Patient's BMI is: 22.1606648199446
# Patient's BMI is: 51.90311418685122

patients = [[70, 1.8], [80, 1.9], [150, 1.7]]


def calculate_bmi(patient=[]):
    return patient.append(patient[0] / (patient[1] ** 2))


for patient in patients:
    calculate_bmi(patients[0])
    print("Patient's BMI is: " + str(patient[-1]))
