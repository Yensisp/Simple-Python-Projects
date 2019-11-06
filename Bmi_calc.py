def bmi_calulator(height, weight):
    bmi = (weight / height / height) * 703
    print('BMI: ' + str(bmi))
    if bmi < 18:
        print('BMI is low')
    elif bmi < 25:
        print('BMI is good')
    else:
        print('BMI is too high')
