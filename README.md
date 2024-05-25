#Taskwarrior CLI Tests

This project contains automated tests for Taskwarrior ising Python and pytest. Thes tests cover common Taskwarrior functionalities such as adding, listing, completing or deleting tasks. 

### Prerequisites ###

- Python 3.8+
- Taskwarrior
- 'pip'

### Installation ###

- Taskwarrior:
  Follow the instructions on the [Taskwarrior download page](https://taskwarrior.org/download/) to install Taskwarrior on your system.

### PYthon Dependencies ###

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
