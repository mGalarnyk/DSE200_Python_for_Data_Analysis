class PERSON:
    def __init__(self,name='john',ssn=0,sex='female',address='',birth_date=0):
        self._name=Name
        self._ssn=ssn
        self._sex=sex
        self._address=address
        self._birth_date=birth_date
    def get_name(self):
        return

class EMPLOYEE(PERSON):
    def __init__(self,salary=0,**kwargs):
        super().__init__(**kwargs)
        self._salary=salary

class STUDENT(PERSON):
    def __init__(self,major_dept='cse',**kwargs):
        super().__init__(**kwargs)
        self._major_dept=major_dept

class STUDENT_ASSISTANT(STUDENT,EMPLOYEE):
    def __init__(self,percent_time=10,**kwargs):
        super().__init__(**kwargs)
        self._percent_time=percent_time

###  Main program that uses the class Student_assistant
if __name__ == '__main__':
    A=STUDENT_ASSISTANT(name='beth',percent_time=30)
    print A.get_name()

        
        
