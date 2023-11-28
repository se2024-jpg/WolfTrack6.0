# Code Description
## Functions

1. **index()**: 
   - Description: Renders the index.html template.
   - Parameters: None
   - Returns: HTML template for the index page.

2. **logout()**:
   - Description: Logs out the user by clearing session variables.
   - Parameters: None
   - Returns: Redirects to the login page.

3. **login()**:
   - Description: Handles user login.
   - Parameters: None
   - Returns: Renders the login.html template or redirects to admin or student pages based on user type after successful login.

4. **signup()**:
   - Description: Handles user registration.
   - Parameters: None
   - Returns: Renders the signup.html template or redirects to the login page after successful registration.

5. **admin()**:
   - Description: Renders the admin_landing.html template with user information.
   - Parameters: None
   - Returns: HTML template for the admin landing page.

6. **student()**:
   - Description: Renders the home.html template for students with user information and job applications.
   - Parameters: None
   - Returns: HTML template for the student home page.

7. **get_job_application_status(status)**:
   - Description: Retrieves job applications by status for a student.
   - Parameters: status (string) - status of job application
   - Returns: HTML template for the student home page with filtered job applications.

8. **send_email()**:
   - Description: Sends an email notification to a specified email address.
   - Parameters: None
   - Returns: HTML response for admin landing page after sending the email.

9. **tos()**:
   - Description: Renders a PDF file stored in the 'static/files/' directory.
   - Parameters: None
   - Returns: PDF file for download.

10. **add_job_application()**:
    - Description: Adds a job application to the database.
    - Parameters: None
    - Returns: Redirects to the student page after adding the job application.

11. **update_job_application()**:
    - Description: Updates a job application in the database.
    - Parameters: None
    - Returns: Redirects to the student page after updating the job application.

12. **delete_job_application(company)**:
    - Description: Deletes a job application from the database by company name.
    - Parameters: company (string) - name of the company
    - Returns: Redirects to the student page after deleting the job application.

13. **add_New()**:
    - Description: Adds new details to the database.
    - Parameters: None
    - Returns: Renders the home.html template.

14. **send_Profile()**:
    - Description: Sends a user profile via email.
    - Parameters: None
    - Returns: Renders the home.html template with data and upcoming events.

15. **job_profile_analyze()**:
    - Description: Analyzes job profile text for skills extraction.
    - Parameters: None
    - Returns: Renders the job_profile_analyze.html template with extracted skills.

16. **upload()**:
    - Description: Uploads a file (resume) and saves it to the 'Controller/resume/' directory.
    - Parameters: None
    - Returns: Renders the home.html template.

17. **view_ResumeAna()**:
    - Description: Renders the resume_analyzer.html template.
    - Parameters: None
    - Returns: Renders the resume_analyzer.html template.

18. **analyze_resume()**:
    - Description: Analyzes the uploaded resume.
    - Parameters: None
    - Returns: Renders the resume_analyzer.html template with analysis output.

19. **display()**:
    - Description: Displays the uploaded resume file for download.
    - Parameters: None
    - Returns: Resume file for download.

20. **chat_gpt_analyzer()**:
    - Description: Performs analysis on a resume using chatGPT and extracts different sections.
    - Parameters: None
    - Returns: Renders the chat_gpt_analyzer.html template with resume sections.

21. **job_search()**:
    - Description: Renders the job_search.html template.
    - Parameters: None
    - Returns: Renders the job_search.html template.

22. **search()**:
    - Description: Searches for job listings using Adzuna API based on the job role.
    - Parameters: None
    - Returns: Renders the job_search_results.html template with job listings.
