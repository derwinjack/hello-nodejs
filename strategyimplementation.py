# Define the Strategy interface
class CoursePlanStrategy:
    def generate_course_plan(self, student, program_requirements, available_courses):
        pass

# Concrete Strategy 1: Fastest Graduation
class FastestGraduationStrategy(CoursePlanStrategy):
    def generate_course_plan(self, student, program_requirements, available_courses):
        # Implementation to generate course plan for fastest graduation
        # ...

# Concrete Strategy 2: Easy Courses
class EasyCoursesStrategy(CoursePlanStrategy):
    def generate_course_plan(self, student, program_requirements, available_courses):
        # Implementation to generate course plan prioritizing easy courses
        # ...

# Concrete Strategy 3: Prioritize Electives
class PrioritizeElectivesStrategy(CoursePlanStrategy):
    def generate_course_plan(self, student, program_requirements, available_courses):
        # Implementation to generate course plan prioritizing electives
        # ...

# Context class that will use the selected strategy
class CoursePlanGenerator:
    def __init__(self, strategy):
        self.strategy = strategy

    def generate_course_plan(self, student, program_requirements, available_courses):
        return self.strategy.generate_course_plan(student, program_requirements, available_courses)

# REST API Endpoints
# These endpoints can be part of your web framework (e.g., Flask, Django)

# Endpoint for confirming courses to be offered
@app.route('/confirm-courses', methods=['POST'])
def confirm_courses():
    # Implementation to confirm courses
    # ...

# Endpoint for specifying program requirements
@app.route('/specify-program-requirements', methods=['POST'])
def specify_program_requirements():
    # Implementation to specify program requirements
    # ...

# Endpoint for populating course history
@app.route('/populate-course-history', methods=['POST'])
def populate_course_history():
    # Implementation to populate course history
    # ...

# Endpoint for auto-generating course plan
@app.route('/generate-course-plan', methods=['POST'])
def generate_course_plan():
    # Get request data
    strategy_type = request.json.get('strategy_type')
    
    # Create the appropriate strategy based on the request
    if strategy_type == 'fastest_graduation':
        strategy = FastestGraduationStrategy()
    elif strategy_type == 'easy_courses':
        strategy = EasyCoursesStrategy()
    elif strategy_type == 'prioritize_electives':
        strategy = PrioritizeElectivesStrategy()
    else:
        return jsonify({'error': 'Invalid strategy type'}), 400

    # Create the context with the selected strategy
    course_plan_generator = CoursePlanGenerator(strategy)

    # Generate the course plan
    course_plan = course_plan_generator.generate_course_plan(student, program_requirements, available_courses)

    # Return the generated course plan
    return jsonify({'course_plan': course_plan})
