import subprocess
# Import the subprocess module to run external commands (like running your CLI script)
# and capture their output programmatically.

def test_add_user():
    # Defines a test function named 'test_add_user'.
    # Pytest will automatically detect and run functions prefixed with 'test_'.

    # Run: python cli.py add-user John
    result = subprocess.run(
        ['python', 'cli.py', 'add-user', 'John'],  # Command and its arguments as a list.
        capture_output=True,                       # Capture stdout and stderr in the result object.
        text=True                                 # Return output as a string (not bytes).
    )
    # After running the command, 'result' holds the output, errors, and return code.

    # Check that output contains confirmation message
    assert "User 'John' added." in result.stdout
    # Assert that the string confirming user addition is present in standard output.
    # If this fails, pytest will report the test as failed.

def test_list_users():
    # Defines a second test function to check the list-users command.

    # Run: python cli.py list-users
    result = subprocess.run(
        ['python', 'cli.py', 'list-users'],       # Command to list all users.
        capture_output=True,                       # Capture the output.
        text=True                                 # Return output as string.
    )
    # 'result.stdout' now contains the output of the list-users command.

    # Check that output lists the user 'John' added previously
    assert "John" in result.stdout
    # Assert that the output contains the string "John".
    # This confirms that the user added in the previous test appears in the list.
