assessment_value_percent = 0.6
tax_rate = 72 / 100 / 100


def assessment_value(a):
    return a*assessment_value_percent


def property_tax(a):
    return assessment_value(a) * tax_rate


def main():
    value = float(input('Enter the actual value: '))
    print('Assessment value: %.2f dollars' % assessment_value(value))
    print('Property Tax: %.2f dollars' % property_tax(value))


main()
