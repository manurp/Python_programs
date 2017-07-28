import logging

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('employee.log')

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info('Created employee: {} - {}'.format(self.fullname, self.email))

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)


emp1 = Employee('Manoj', 'Poojari')
emp2 = Employee('Ravi', 'Kumar')
emp3 = Employee('Shamantha', 'Ravi')
emp4 = Employee('Bhoomika', 'Poojari')

# print(emp1)
