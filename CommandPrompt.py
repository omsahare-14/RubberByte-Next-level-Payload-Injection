import subprocess
def execute_command(command):
    try:
        # Execute the command and capture the output
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print("An error occurred while executing the command:")
        print(e.output.decode())

# Specify the command you want to execute
command = 'dir'

# Call the function to execute the command
execute_command(command)
