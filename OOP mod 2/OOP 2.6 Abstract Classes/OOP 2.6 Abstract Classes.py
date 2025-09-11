#Assignment: Creating a New Abstract Class for a Business

from abc import ABC, abstractmethod

class Service_Plans(ABC):
    def __init__(self, service_plan="Basic", support_level="Standard"):
        self.service_plan = service_plan
        self.support_level = support_level


    @abstractmethod
    def add_in(self):
        pass

    @abstractmethod
    def description(self):
        pass


class Silver_Plan(Service_Plans):
    def __init__(self, service_plan="silver", support_level="mid_priority"):
        super().__init__(service_plan, support_level)

    def add_in(self):
        return """includes license management and premium analytics,
to include maximum 24 hour data recovery in disaster scenarios."""
    
    def description(self):
        return f""" The Service plan selected is {self.service_plan}
and support level selected is {self.support_level}
please read the description of the plan below:\n\n{self.add_in()}"""
    

class Gold_Plan(Service_Plans):
    def __init__(self, service_plan="gold", support_level="Highest_priority"):
        super().__init__(service_plan, support_level)

    def add_in(self):
        return """includes license management, premium analytics,
and a dedicated account manager, to include maximum 2 hour data recovery in disaster scenarios."""

    def description(self):
        return f""" The Service plan selected is {self.service_plan}
and support level selected is {self.support_level}
please read the description of the plan below:\n\n{self.add_in()}
"""



companyB = Silver_Plan()
print(companyB.description())
print("---------------------------------------------------")
companyC = Gold_Plan()
print(companyC.description())

