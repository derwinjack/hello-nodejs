//Context Class (CoursePlanGenerator):
//This class will maintain a reference to the current strategy and delegate the generation of the course plan to the selected strategy.

class CoursePlanGenerator:
    def __init__(self, strategy):
        self.strategy = strategy

    def generate_course_plan(self, student):
        return self.strategy.generate_course_plan(student)

  //Strategy Interface (CoursePlanStrategy):

//An interface or abstract class that declares the method for generating a course plan.

from abc import ABC, abstractmethod

class CoursePlanStrategy(ABC):
    @abstractmethod
    def generate_course_plan(self, student):
        pass
//Concrete Strategy Classes (FastestGraduationStrategy, EasyCoursesStrategy, ElectivesPriorityStrategy):

//Classes that implement the CoursePlanStrategy interface, providing specific algorithms for generating course plans.

class FastestGraduationStrategy(CoursePlanStrategy):
    def generate_course_plan(self, student):
        # Implementation for generating course plan for fastest graduation
        pass

class EasyCoursesStrategy(CoursePlanStrategy):
    def generate_course_plan(self, student):
        # Implementation for generating course plan with easy courses
        pass

class ElectivesPriorityStrategy(CoursePlanStrategy):
    def generate_course_plan(self, student):
        # Implementation for generating course plan prioritizing electives
        pass

//Client Classes (Student, Staff):
//Classes that interact with the context (i.e., CoursePlanGenerator) to utilize the selected strategy.


class Student:
    def __init__(self, name, course_history):
        self.name = name
        self.course_history = course_history

    def create_course_plan(self, strategy):
        course_plan_generator = CoursePlanGenerator(strategy)
        return course_plan_generator.generate_course_plan(self)

class Staff:
    def confirm_courses(self, courses):
        # Implementation for confirming courses to be offered
        pass

    def specify_programme_requirements(self, requirements):
        # Implementation for specifying program requirements
        pass
//With these classes, you can create instances of Student and Staff, set up different strategies (e.g., FastestGraduationStrategy, EasyCoursesStrategy), 
//and use the CoursePlanGenerator to generate course plans based on the selected strategy.
//The concrete strategy classes will contain the logic for generating course plans according to the specified options.
