"# employeemanagement"
Assignment

Entity:- Manager
Properties: email, firstname,lastname,password,address,dob,company etc.

Entity:- Employee
Properties: empId,firstname,lastname,address,dob,mobile,city etc.

Front End :
Instructions:

1. You can use any UI framework you know e.g. Angularjs or Reactjs or any Other.
2. Commit the code on github on regular basis and provide the link
3. Signup for Codegrip and scan your project for code quality, provide us a report of same as a final deliverable(can take a screenshot of Project Dashboard and attach with email along with github link)
4. Please write clear & clean code with proper comments.
5. Your code will be reviewed on code style, best practices, exception handling and code management.
6. Feel free to use other UI frameworks like jquery, bootstrap, material, etc.

Contains three screens:

1. Manager sign up
2. Manager login
3. Home Screen
   Manager signs up :  
    The manager should be able to signup using his properties.
   Manager login :  
    The manager should be able to login using his email and password and should redirect to the home screen. Should handle error scenarios.
   Home Screen :

- The home screen should contain a list of employees and add the employee button on the top right corner.
- On clicking add employee button popup should open where the manager can fill employee details and to submit details should be sent to the server and should be stored in the DB and error scenarios should be handled.
  -The manager can update and delete employees from the list.
  -Provide a button to update employee records. On clicking the update button pop up should be open with employee details in edit mode.
  -The confirmation model should show before the update and delete employees.
  Back End :
  Instructions:

1. Must use Python with the Django framework.
2. Commit the code on github on regular basis and provide the link
3. Signup for Codegrip and scan your project for code quality, provide us a report of same as final deliverable(can take a screenshot of Project Dashboard and attach with email along with github link)
4. Please write clear & clean code with proper comments.
5. Your code will be reviewed on code style, best practices, exception handling and code management.
6. Attach schemas after completion of the assignment.

Develop web services using the Django framework which can be used for the front end.

1. Manager Signup:
   a. Insert manager details in tables.
   b. manager records should be unique based on email, which means duplicates records should not able to enter in DB.
2. Manager Login:
   a. The manager can log in based on email and password.
3. Create Employee:
   a. The manager can create employee.
4. Retrieve all Employee:
   a. Retrieve all employees in order of first name and last name.
5. Update Employee:
   a. Employee records should be able to update.
6. Delete Employee:
   a. Employee records should be able to delete.

Create the DB table(s) accordingly.
