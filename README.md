#Taskwarrior CLI Tests

This project contains automated tests for Taskwarrior using Python and pytest. Thes tests cover common Taskwarrior functionalities such as adding, listing, completing or deleting tasks. 

### Prerequisites ###

- Python 3.8+
- Taskwarrior
- 'pip'

### Installation ###

- Taskwarrior:
  Follow the instructions on the [Taskwarrior download page](https://taskwarrior.org/download/) to install Taskwarrior on your system.

### Python Dependencies ###

1. Clone the repository:
   git clone https://github.com/hroonr/taskwarrior.git 
   cd taskwarrior-cli-tests
2. Install VisualStudioCode or any other IDE.
3. Install the required Python packages:
   pip install -r requirements.txt

### Running the Tests ###

Ensure Taskwarrior is installed and properly configured on your system and run the tests using pytest:

'''bash
pytest pytest_taskwarrior.py
'''

### Test scenarios ###

The automated tests cover the following scenarios:

1. Adding a Task:
   - adds a task with a description and cerifies the task added.
2. Listing Tasks:
   - Lists all tasks and verifies the output contains the added task.
  
### Example 'pytest_taskwarrior.py' ###

Here is an example how the test 'pytest_taskwarrior.py' might look:

'''python
import subprocess
import pytest

# Utility function to run a Taskwarrior command
def run_task_command(command):
    result = subprocess.run(['task'] + command.split(), capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip()

# Test creating a new task
def test_create_task():
    # Create a new task
    stdout, stderr = run_task_command('add Test task for pytest')
    assert 'Created task' in stdout

    # Verify the task is in the list
    stdout, stderr = run_task_command('list')
    assert 'Test task for pytest' in stdout

# Test listing all tasks
def test_list_tasks():
    # List all tasks
    stdout, stderr = run_task_command('list')
    assert 'Test task for pytest' in stdout

if __name__ == '__main__':
    pytest.main()


### FUTURE IMPROVEMENTS ###

Following improvements could be made if additional time and resources were available:

1. Enhanced Test Coverage: Expand the test coverage to include more edges cases, e.g. error scenarios, and integration tests to ensure robustness.
2. Performance Optimization: Analyze and optimize the performance to improve the overall scalability of the application.
3. User Interfaec Refinement: Refine the user interface to enhance usability and overall user experience.
4. Parallel Execution: Implement parallel execution of automated tests to reduce test execution time and improve efficiency, especially for large test suites, e.g. Selenium.
5. Continuous Learning and Skill Development: Stay updated on the latest advancements in automation testing tools, frameworks, and techniques through continuous learning and skill development. 
