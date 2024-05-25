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
