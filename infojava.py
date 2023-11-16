//Create an interface called CoursePlanningStrategy that declares a method like generateCoursePlan

public interface CoursePlanningStrategy {
    void generateCoursePlan(Student student, ProgramRequirements requirements, List<Course> offeredCourses);
}

//Implement different strategies for auto-generating course plans, such as FastestGraduationStrategy, EasyCoursesStrategy, and ElectivesPriorityStrategy. Each strategy will have its own implementation of the generateCoursePlan method.

public class FastestGraduationStrategy implements CoursePlanningStrategy {
    // Implementation for generating the fastest graduation course plan
}

public class EasyCoursesStrategy implements CoursePlanningStrategy {
    // Implementation for generating a course plan with easy courses
}

public class ElectivesPriorityStrategy implements CoursePlanningStrategy {
    // Implementation for generating a course plan prioritizing electives
}

//Create a context class called CoursePlanner that has a reference to the CoursePlanningStrategy interface. This class will use the selected strategy to generate the course plan.

public class CoursePlanner {
    private CoursePlanningStrategy planningStrategy;

    public void setPlanningStrategy(CoursePlanningStrategy planningStrategy) {
        this.planningStrategy = planningStrategy;
    }

    public void generateCoursePlan(Student student, ProgramRequirements requirements, List<Course> offeredCourses) {
        planningStrategy.generateCoursePlan(student, requirements, offeredCourses);
    }
}

//In your application, when a student wants to generate a course plan, they can select a strategy based on the specified option (fastest graduation, easy courses, electives priority) and set it in the CoursePlanner.

CoursePlanner coursePlanner = new CoursePlanner();

// Set the strategy based on user's choice
coursePlanner.setPlanningStrategy(new FastestGraduationStrategy());
// or coursePlanner.setPlanningStrategy(new EasyCoursesStrategy());
// or coursePlanner.setPlanningStrategy(new ElectivesPriorityStrategy());

// Generate the course plan
coursePlanner.generateCoursePlan(student, programRequirements, offeredCourses);

