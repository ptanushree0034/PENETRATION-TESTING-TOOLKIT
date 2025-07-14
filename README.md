# PENETRATION-TESTING-TOOLKIT

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: TANUSHREE PATRA

*INTERN ID*: CT08DG608

*DOMAIN*: CYBER SECURITY & ETHICAL HACKING

*DURATION*: 8 WEEKS

*MENTOR*: NEELA SANTOSH KUMAR

*DESCRIPTION*:

This task involved developing a Python-based penetration testing toolkit consisting of two independent modules: a port scanner and a brute-force password tester. The toolkit runs through a command-line interface and is structured as a single, modular Python script. Once the program is launched, the user is prompted with a menu to choose between scanning ports, performing a brute-force test, or exiting the tool.

The port scanner module accepts a target IP address, starting port, and ending port as user inputs. It uses Python's socket library to attempt TCP connections to each port in the specified range. If a connection is successful, the port is considered open and displayed in the output. A default timeout is applied to each connection attempt to ensure efficiency. This scanning logic is implemented using a simple loop and exception handling for responsiveness.

The brute-force tester module prompts the user to enter a username and a known password (for simulation). A small list of common passwords is predefined within the script. Using a loop, each password from the list is compared against the correct one provided by the user. If a match is found, the password is printed as found, and the loop stops. If not, the loop continues until all options are exhausted. The getpass module is used to keep the actual password input hidden for realism, and the time module introduces a delay between attempts to simulate actual brute-force behavior.

To complete the task, the following steps were followed:

A new folder was created to organize all files related to the task.

The code was written and executed using Visual Studio Code with Python 3.12.

Built-in libraries used: socket, time, and getpass.

Testing was done locally using the loopback IP 127.0.0.1 and a small range of ports (1 to 100).

Sample passwords such as admin, 1234, and password were used in the brute-force module for demonstration.

*OUTPUT*:

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/c229fa60-0209-441d-84e5-debdc63d1c18" />
