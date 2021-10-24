
class Profil():

    def __init__(self, weight, height, age, sex, activity):
        self.weight = weight
        self.height = height
        self.age = age
        self.sex = sex
        self.activity = activity #A B C D E

def CPM(self, sex, activity):
    if sex == "F":
        bmr = 655 + 9.6 * self.weight + 1.8 * self.height - 4.7 * self.age
        if activity == "A":
            cpm = bmr * 2
        if activity == "B":
            cpm = bmr * 1.7
        if activity == "C":
            cpm = bmr * 1.5
        if activity == "D":
            cpm = bmr * 1.3
        if activity == "E":
            cpm = bmr * 1.2

    else:
        bmr = 66 + 13.7 * self.weight + 5 * self.height - 6.8 * self.age
        if activity == "A":
            cpm = bmr * 2
        if activity == "B":
            cpm = bmr * 1.7
        if activity == "C":
            cpm = bmr * 1.5
        if activity == "D":
            cpm = bmr * 1.3
        if activity == "E":
            cpm = bmr * 1.2

    return cpm


def BMI(self):
    bmi = self.weight / (self.height) ^ 2
    return bmi
