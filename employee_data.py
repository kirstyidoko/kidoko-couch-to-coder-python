employees = [
    {
        "first_name":"Jose",
        "last_name":"Lopez",
        "email":"joselopez0944@example.com",
        "age":25,
        "job_title":"Project Manager",
        "years_of_experience":1,
        "salary":8500,
        "department":"Product"
    },
    {
        "first_name":"Diane",
        "last_name":"Carter",
        "email":"dianecarter1228@example.com",
        "age":26,
        "job_title":"Machine Learning Engineer",
        "years_of_experience":2,
        "salary":7000,
        "department":"Product"
    },
    {
        "first_name":"Shawn",
        "last_name":"Foster",
        "email": None,
        "age":37,
        "job_title":"Customer Service Rep",
        "years_of_experience":14,
        "salary":17000,
        "department":"Business"
    },
    {
        "first_name":"Brenda",
        "last_name":"Fisher",
        "email":"brendafisher3185@example.com",
        "age":31,
        "job_title":"Web Developer",
        "years_of_experience":8,
        "salary":10000,
        "department":"Product"
    },
    {
        "first_name":"Sean",
        "last_name":"Hunter",
        "email": None,
        "age":35,
        "job_title":"Project Manager",
        "years_of_experience":11,
        "salary":14500,
        "department":"Product"
    },
    {
        "first_name":"Joshua",
        "last_name":"Jacobs",
        "email":"joshuajacobs5904@example.com",
        "age":28,
        "job_title":"Project Manager",
        "years_of_experience":3,
        "salary":10500,
        "department":"Business"
    },
    {
        "first_name":"Brianna",
        "last_name":"Marshall",
        "email":None,
        "age":33,
        "job_title":"Machine Learning Engineer",
        "years_of_experience":10,
        "salary":11000,
        "department":"Product"
    },
    {
        "first_name":"John",
        "last_name":"Tate",
        "email":"johntate7881@example.com",
        "age":33,
        "job_title":"Mobile Developer",
        "years_of_experience":10,
        "salary":11000,
        "department":"Product"
    },
    {
        "first_name":"Jillian",
        "last_name":"Byrd",
        "email":None,
        "age":34,
        "job_title":"Business Analyst",
        "years_of_experience":10,
        "salary":11000,
        "department":"Business"
    },
    {
        "first_name":"Melanie",
        "last_name":"Sharp",
        "email":"melaniesharp9256@example.com",
        "age":41,
        "job_title":"Web Developer",
        "years_of_experience":15,
        "salary":14500,
        "department":"Product"
    },
    {
        "first_name":"Brandy",
        "last_name":"Mckee",
        "email":None,
        "age":37,
        "job_title":"Marketing Manager",
        "years_of_experience":14,
        "salary":14000,
        "department":"Business"
    },
    {
        "first_name":"Robert",
        "last_name":"Simpson",
        "email":"robertsimpson11778@example.com",
        "age":36,
        "job_title":"Marketing Manager",
        "years_of_experience":12,
        "salary":15000,
        "department":"Business"
    },
    {
        "first_name":"George",
        "last_name":"Mckenzie",
        "email":"georgemckenzie12384@example.com",
        "age":28,
        "job_title":"Machine Learning Engineer",
        "years_of_experience":4,
        "salary":10000,
        "department":"Product"
    },
    {
        "first_name":"Joseph",
        "last_name":"Smith",
        "email":None,
        "age":40,
        "job_title":"Machine Learning Engineer",
        "years_of_experience":14,
        "salary":14000,
        "department":"Product"
    },
    {
        "first_name":"Dana",
        "last_name":"Crawford",
        "email":"danacrawford14310@example.com",
        "age":32,
        "job_title":"Project Manager",
        "years_of_experience":8,
        "salary":12000,
        "department":"Product"
    },
    {
        "first_name":"Christopher",
        "last_name":"Benson",
        "email":None,
        "age":29,
        "job_title":"Web Developer",
        "years_of_experience":5,
        "salary":7500,
        "department":"Product"
    },
    {
        "first_name":"Nicole",
        "last_name":"Smith",
        "email":"nicolesmith16360@example.com",
        "age":26,
        "job_title":"Designer",
        "years_of_experience":4,
        "salary":10000,
        "department":"Product"
    },
    {
        "first_name":"Peter",
        "last_name":"Jimenez",
        "email":"peterjimenez17791@example.com",
        "age":28,
        "job_title":"UX Designer",
        "years_of_experience":3,
        "salary":6500,
        "department":"Business"
    },
    {
        "first_name":"Sergio",
        "last_name":"Boyle",
        "email":"sergioboyle18425@example.com",
        "age":31,
        "job_title":"Tester",
        "years_of_experience":6,
        "salary":9000,
        "department":"Product"
    },
    {
        "first_name":"Brianna",
        "last_name":"Moss",
        "email":None,
        "age":31,
        "job_title":"Designer",
        "years_of_experience":5,
        "salary":10500,
        "department":"Product"
    },
    {
        "first_name":"Taylor",
        "last_name":"Garner",
        "email":"taylorgarner20196@example.com",
        "age":32,
        "job_title":"Machine Learning Engineer",
        "years_of_experience":6,
        "salary":11000,
        "department":"Product"
    },
    {
        "first_name":"Michael",
        "last_name":"Padilla",
        "email":"michaelpadilla21381@example.com",
        "age":29,
        "job_title":"Customer Service Rep",
        "years_of_experience":5,
        "salary":9500,
        "department":"Business"
    },
    {
        "first_name":"Yvette",
        "last_name":"Walker",
        "email":None,
        "age":26,
        "job_title":"Designer",
        "years_of_experience":2,
        "salary":7000,
        "department":"Product"
    },
    {
        "first_name":"Kristina",
        "last_name":"Pena",
        "email":"kristinapena23750@example.com",
        "age":34,
        "job_title":"Business Analyst",
        "years_of_experience":11,
        "salary":12500,
        "department":"Business"
    }
]

# 1.  Print the name of the person who has the highest salary at the company.

# Step 1: loop through all employees
# Step 2: compare our employees to each other
# Step 3: whichever employee earns the most, we should print out their name

highest_paid_employee = employees[0]

for employee in employees:
    if employee["salary"] > highest_paid_employee["salary"]:
        highest_paid_employee = employee

print("The highest paid employee in the company is " + highest_paid_employee["first_name"] 
      + " " + highest_paid_employee["last_name"])

# 2.  Print the combined years of experience of all employees at the company.

# Step 1: loop through all employees
# Step 2: create running total of years of experience

total_years = 0

for employee in employees:
    total_years += employee["years_of_experience"]
print("The employees have " + str(total_years) + " combined years of experience")

# 3.  Some people don't have an email address - collect their details into a new list!

# Step 1: create new list for employees w/o emails
no_email = []

# Step 2: add each employee w/o email to list
for employee in employees:
    if employee["email"] == None:
        no_email.append(employee)

print(no_email)

# 4.  Which one costs more for the company - Product department salaries or Business department salaries?

# Step 1: create new list for each department

product_employees = []
for employee in employees:
    if employee["department"] == "Product":
        product_employees.append(employee)

business_employees = []
for employee in employees:
    if employee["department"] == "Business":
        business_employees.append(employee)

# Step 2: calculate total salary for each department

product_total_salary = 0
for product_employee in product_employees:
    product_total_salary += product_employee["salary"]
print(product_total_salary)

business_total_salary = 0
for business_employee in business_employees:
    business_total_salary += business_employee["salary"]
print(business_total_salary)

# Step 3: compare salaries

if product_total_salary > business_total_salary:
    print("Product department salaries (£" + str(product_total_salary) + ") cost more than Business department salaries (£"
          + str(business_total_salary) + ")")
else:
    print("Business department salaries (£" + str(business_total_salary) + ") cost more than Product department salaries (£"
          + str(product_total_salary) + ")")

# Ext 5. What is the average salary for people over 30 years of age? 

# Step 1: create new list for employees over 30

employees_over_30 = []
for employee in employees:
    if employee["age"] > 30:
        employees_over_30.append(employee)

total_over_30_salary = 0
for employee_over_30 in employees_over_30:
    total_over_30_salary += employee_over_30["salary"]

# Step 2: calculate avg

avg_over_30_salary = total_over_30_salary / len(employees_over_30)
print(avg_over_30_salary)

# Bonus step: avg is recurring number - round to 2 decimal places

rounded_avg = round(avg_over_30_salary, 2)
print("The average salary for employees over 30 is £" + str(rounded_avg))

# Ext 6. Create a new dict and calculate how many people are working with certain job titles. (HARD) 
# Example: {"Project Manager": 4, "Machine Learning Engineer": 3, ...}

# Step 1: print out all unique job titles in 'employees'

# Code taken from: https://www.geeksforgeeks.org/python-unique-values-of-key-in-dictionary/

# initializing key
highlight_key = "job_title"
 
# Unique Values of Key in Dictionary
# Using loop + set()
job_titles = []
for employee in employees:
    job_titles.append(employee[highlight_key])
job_titles = list(set(job_titles))
 
# printing result
print("The unique job titles are: " + str(job_titles))

# Note to reader: turned out I didn't need to use the previous step, but it did help me understand what job title needed to be
# counted

# Step 2: count no. of times each job title appears

job_title_counter = {}

for employee in employees:
    count_per_job_title = employee["job_title"]
    if count_per_job_title in job_title_counter:
        job_title_counter[count_per_job_title] += 1
    else:
        job_title_counter[count_per_job_title] = 1

print(job_title_counter)