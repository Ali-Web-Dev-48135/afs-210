class Payroll:
    def __init__(self,employeeId, fName, lName, hourlyRate):
        self.firstName = fName
        self.lastName = lName
        self.employeeId = employeeId
        self.hourlyRate = hourlyRate

    def pay(self, hoursWorked):
        if(hoursWorked <= 40):
            return float(hoursWorked * float(self.hourlyRate))
        else:
            return float((hoursWorked * float(self.hourlyRate)) + hoursWorked - 40 * 1.5)


    #OPTIONAL GETTERS AND SETTERS COMMENTED OUT.
   # @property
    # def firstName(self):
    #     return self.firstName
    
    # @firstName.setter
    # def firstName(self, value):
    #     self.firstName = value
    
    # @property
    # def lastName(self):
    #     return self.lastName

    # @lastName.setter
    # def lastName(self, value):
    #     self.lastName = value
    
    # @property
    # def employeeId(self):
    #     return self.employeeId

    # @employeeId.setter
    # def employeeId(self, value):
    #     self.employeeId = value
    
    # @property
    # def hourlyRate(self):
    #     return self.hourlyRate

    # @hourlyRate.setter 
    # def hourlyRate(self, value):
    #     self.hourlyRate = value