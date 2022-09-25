"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, commission = 0, bonus = 0, contracts = 0, per_contract = 0):
        self.name = name
        self.bonus = bonus
        self.contracts = contracts
        self.per_contract = per_contract
        self.commission = self.contracts * self.per_contract

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

    def set_commission(self, contracts, per_contract):
        self.contracts = contracts
        self.per_contract = per_contract
        self.commission = contracts * per_contract

    def set_bonus(self, bonus):
        self.bonus = bonus


class Salary_Emp(Employee):
    def __init__(self, name, monthly, commission = 0, bonus = 0, contracts = 0, per_contract = 0):
        super().__init__(name, commission = 0, bonus = 0, contracts = 0, per_contract = 0)
        self.monthly = monthly
        self.salary = self.monthly

    def get_pay(self):
        if self.commission > 0:
            self.salary += self.commission
        elif self.bonus > 0:
            self.salary += self.bonus
        return self.salary

    def __str__(self):
        description = ''
        if self.commission > 0:
            description = f'{self.name} works on a monthly salary of {self.monthly} and receives a commission for {self.contracts} contract(s) at {self.per_contract}/contract.  Their total pay is {self.salary}.'
        elif self.bonus > 0:
            description = f'{self.name} works on a monthly salary of {self.monthly} and receives a bonus commission of {self.bonus}.  Their total pay is {self.salary}.'
        else:
            description = f'{self.name} works on a monthly salary of {self.monthly}.  Their total pay is {self.salary}.'
        return description



class Hourly_Emp(Employee):
    def __init__(self, name, commission = 0, bonus = 0, contracts = 0, per_contract = 0, wage = 0, hours = 0):
        super().__init__(name, commission = 0, bonus = 0, contracts = 0, per_contract = 0)
        self.wage = wage
        self.hours = hours
        self.hourly_wage = self.wage * self.hours

    def __str__(self):
        description = ''
        if self.commission > 0:
            description = f'{self.name} works on a contract of {self.hours} hours at {self.wage}/hour and receives a commission for {self.contracts} contract(s) at {self.per_contract}/contract.  Their total pay is {self.hourly_wage}.'
        elif self.bonus > 0:
            description = f'{self.name} works on a contract of {self.hours} hours at {self.wage}/hour and receives a bonus commission of {self.bonus}.  Their total pay is {self.hourly_wage}.'
        else:
            description = f'{self.name} works on a contract of {self.hours} hours at {self.wage}/hour.  Their total pay is {self.hourly_wage}.'
        return description

    def get_pay(self):
        if self.commission > 0:
            self.hourly_wage += self.commission
        elif self.bonus > 0:
            self.hourly_wage += self.bonus
        return self.hourly_wage



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Salary_Emp(name='Billie', monthly=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Hourly_Emp(name='Charlie', hours=100, wage=25)


# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Salary_Emp(name='Renee', monthly=3000)
renee.set_commission(4, 200)


# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Hourly_Emp(name='Jan', hours=150, wage=25)
jan.set_commission(3, 220)


# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Salary_Emp(name='Robbie', monthly=2000)
robbie.set_bonus(1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Hourly_Emp(name='Ariel', hours=120, wage=30)
ariel.set_bonus(600)
