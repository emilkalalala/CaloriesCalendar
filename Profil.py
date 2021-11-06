
def male_cpm_small(Weight, Heigh, Age):
        # Calculate male bmr
    return (66 + 13.7 * Weight + 5 * Heigh - 6.8 * Age)*1.2

def female_cpm_small(Weight, Heigh, Age):
        # Calculate female BMR
    return (655 + 9.6 * Weight + 1.8 * Heigh - 4.7 * Age)*1.2

def male_cpm_medium(Weight, Heigh, Age):
        # Calculate male bmr
    return (66 + 13.7 * Weight + 5 * Heigh - 6.8 * Age)*1.5

def female_cpm_medium(Weight, Heigh, Age):
        # Calculate female BMR
    return (655 + 9.6 * Weight + 1.8 * Heigh - 4.7 * Age)*1.5

def male_cpm_big(Weight, Heigh, Age):
        # Calculate male bmr
    return (66 + 13.7 * Weight + 5 * Heigh - 6.8 * Age)*2

def female_cpm_big(Weight, Heigh, Age):
        # Calculate female BMR
    return (655 + 9.6 * Weight + 1.8 * Heigh - 4.7 * Age)*2



def BMI(Weight, Height):
    return Weight / (Height/100)  ** 2

