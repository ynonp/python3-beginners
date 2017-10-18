# We use input print a message to
# the user and get a value,
# saving the value into variable named: age_in_years
age_in_years = input("Please tell me your age (in years): ")

# age_in_years holds the age but as text.
# Python won't let you perform calculations on texts,
# unless you tell it it's really a number. That's what
# the int(...) is for.
#
# This next line treats age_in_years as a number,
# and that allows to multiply it by 12.
# The result is saved in a new variable called age_in_months
age_in_months = int(age_in_years) * 12

# Now we can print age_in_months
print("Your age in months is:", age_in_months)

