def company_policy(experience, base_pay):
    result = 0
    if 0 <= experience < 5:
        if base_pay > 1000:
            result += 1        # Label 1
        if base_pay > 5000:
            result += 2        # Label 2
        elif base_pay > 9000:
            result += 2        # Label 3
        if experience > 3:
            result += 3        # Label 4
    elif 5 <= experience <= 10:
        if base_pay <= 10000:
            result += 4        # Label 5
        if base_pay > 25000:
            result += 5        # Label 6
        if base_pay > 50000:
            result += 2        # Label 7
        elif experience > 7:
            result += 6        # Label 8
    elif experience > 10:
        if base_pay < 30000:
            result += 4        # Label 9
            result += 7        # Label 10
    if experience > 15:
        if base_pay > 50000:
            result += 5        # Label 11
            result += 8        # Label 12
        else:
            result += 8        # Label 13
    else:
        result += 1            # Label 14
        result += 7            # Label 15
    return result              # Label 16


# Main part of program starts here.
experience_test = 18
base_pay_test = 26000

print('Calling company_policy() with experience = ' + str(experience_test) +
      ' base_pay = ' + str(base_pay_test) + ': '+
      str(company_policy(experience_test, base_pay_test)))

