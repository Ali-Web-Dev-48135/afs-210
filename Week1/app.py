from payrollClass import Payroll

#HELPER METHOD TO VERIFY THE TYPE
def verifyUserInput(userInput, condition, expectedType, message):

    try:
        if(isinstance(expectedType(userInput),expectedType)):
            return userInput
    except:
        while(condition != True):
            userInput = input(message)
            try:
                condition = isinstance(expectedType(userInput), expectedType)
                if(condition == True):
                    return userInput
            except:
                condition = False
                continue    

# RETURNS THE EMPLOYEES ID.
def returnEmployeeId():

        employeeIdInput = input("Please enter the Employee's ID (only numbers are accepted): ")
        validUserInput = verifyUserInput(employeeIdInput,isinstance(employeeIdInput, int), int,'Please re-enter the Id as a number: ')
        return validUserInput
# RETURNS THE EMPLOYEES FIRST NAME.

def returnEmployeeFirstName():
        employeeFirstName = input("Please enter the Employee's First Name: ")
        validUserInput = verifyUserInput(employeeFirstName,isinstance(employeeFirstName, str), str,
                                         """Please re-enter the Employee's First Name: """)
        return validUserInput

# RETURNS THE EMPLOYEES LAST NAME.
def returnEmployeeLastName():
    
    employeeLastName = input("Please enter the Employee's Last Name: ")
    validUserInput = verifyUserInput(employeeLastName,isinstance(employeeLastName, str),str,
                                     """Please re-enter the Employee's Last Name: """)
    return validUserInput

# RETURNS THE HOURLY RATE FOR THE EMPLOYEE.
def returnEmployeeHourlyRate():
    
    employeeHourlyRate = input("Please enter the Employee's Hourly Rate: ")
    validUserInput = verifyUserInput(employeeHourlyRate,isinstance(employeeHourlyRate, float),float,
                                     """Please re-enter the Employee's hourly rate as a float: """)
    return validUserInput


# RETURNS THE HOURS WORKED BY THE EMPLOYEE.
def returnEmployeeHoursWorked(employeeName):
    
    employeeHourswWorked = input("How many hours did % s work this week? " % employeeName)
    validUserInput = verifyUserInput(employeeHourswWorked,isinstance(employeeHourswWorked, float),float, 
                                     """Please re-enter the Employee's hours worked as a float: """)
    return validUserInput


#STARTING POINT OF THE PROGRAM.
def init():
    userEmployeeId = returnEmployeeId()
    userFirstName = returnEmployeeFirstName()
    userLastName = returnEmployeeLastName()
    userHourlyRate = returnEmployeeHourlyRate()
    userHourswWorked = returnEmployeeHoursWorked(userFirstName)
    Employee = Payroll(userEmployeeId, userFirstName, userLastName, userHourlyRate)
    print(userFirstName, "'s paycheck amount is $" ,format(Employee.pay(float(userHourswWorked)),',.2f'))

init()
