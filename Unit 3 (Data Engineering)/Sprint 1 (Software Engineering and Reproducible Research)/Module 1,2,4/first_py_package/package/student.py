'''This file contains a parent class describing students
and a child class describing Bloomtech Students'''

class Student:
    
    def __init__(self, age, gender, months_studing = 1, dedication = 'Full-Time'):
        self.age = age
        self.gender = gender
        self.months_studing = months_studing
        self.dedication = dedication

    def hours_of_study(self):
        '''Return the Total hours of study
        adding 32 hours per month for Full-Time Students
        and 60 hours per month for Part-Time Students'''

        if self.dedication == 'Full-Time':
            total_hours = self.months_studing * 160
        else:
            total_hours = self.months_studing * 60
        return total_hours

    def level(self):
        '''Print Level of expertice of Student
        base on the number of months studied'''
        if self.months_studing <= 6:
            print('Beginner')
        elif self.months_studing <= 12:
            print('Intermediate')
        elif self.months_studing <= 18:
            print('Advanced')
        elif self.months_studing <= 24:
            print('Expert')

class BloomTechStudent(Student):
    def __init__(self, age, gender, carrer_status = 'Studing' , preferred_os = 'Microsoft Windows',
                 months_studing = 1, dedication = 'Full-Time', sent_applications = 0):
        super().__init__(age, gender, months_studing, dedication)
        self.carrer_status = carrer_status
        self.preferred_os = preferred_os
        self.sent_applications = sent_applications

    def send_apps(self, n_apps):
        '''Print number of applications made and update 
        carrer_status and sent_applications'''
        self.carrer_status = 'Job Searching'
        self.sent_applications = self.sent_applications + n_apps
        print(f'Student sent {n_apps} applications')