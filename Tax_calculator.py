# Introduction

print("Welcome to the Net Salary Calculator")
print("\nThis program will calculate an income after state and federal taxes.")

# Setup

federal_standard_deduction = 13200

state_standard_deduction = {
    'California': 4609,
    'New York' : 8000
}

federal_tax_brackets = [
    (10400, 0.10),
    (41225, 0.12),
    (89400, 0.22),
    (174050, 0.24),
    (215400, 0.32),
    (549900, 0.35),
    (1000000, 0.37)
]

state_tax_brackets = {
    'California':[
        (10420, 0.01),
        (24684, 0.02),
        (38959, 0.04),
        (54081, 0.06),
        (68350, 0.08),
        (349137, 0.093),
        (418961, 0.103),
        (698271, 0.113),
        (float('inf'), 0.123)
    ],
    'New York':[
(8500, 0.04),
        (11700, 0.045),
        (13900, 0.0525),
        (21400, 0.059),
        (80650, 0.0645),
        (215400, 0.0685),
        (1077550, 0.0882),
        (5000000, 0.103),
        (float('inf'), 0.103)
    ]
}

fica_cap = 147000
fica_rate = 0.0765

# User Input

try:
    gross_salary = float(input("Enter annual gross salary: $"))
    state = input("Enter state name (California or New York): ").strip()

    if state not in state_tax_brackets:
        print("State not included in calculator")
except:
    print("State not included in calculator")




# Calcualate federal tax

def calculate_tax(income, bracket):
    tax = 0
    prev_limit = 0
    for limit, rate in bracket:
        if income > limit:
            tax += (limit - prev_limit) * rate
            prev_limit = limit
        else:
            tax += (limit - prev_limit) * rate
            break
    return tax

deducted_salary = max(gross_salary - federal_standard_deduction, 0)
federal_tax = calculate_tax(deducted_salary, federal_tax_brackets)

# Calculate state tax

def calculate_state_tax(income, state):
    deducted = max(income - state_standard_deduction[state], 0)
    return calculate_tax(deducted, state_tax_brackets[state])
state_tax = calculate_state_tax(gross_salary, state)

#Calculate FICA

fica_taxable = min(gross_salary, fica_cap)
fica_tax = fica_taxable * fica_rate

# Calculate net salary

total_deductions = federal_tax + fica_tax
net_salary = gross_salary - total_deductions

# Print results

print("Salary Breakdown: ")
print(f"Gross Salary: ${gross_salary}")
print(f"Federal Tax: ${federal_tax}")
print(f"{state} State Tax: ${state_tax}")
print(f"FiCA Tax: ${fica_tax}")
print(f"Total Deductions: ${total_deductions}")
print(f"Net Salary: ${net_salary}")
