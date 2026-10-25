# Study Resources Board

## 1. What You Will Build

You will explore a small website called **Study Resources Board**. It stores learning resources in a database and displays them on a home page. You can open an individual resource to see its details.

The starter includes working resource listing and detail pages. You will complete the add-resource form in the Implementation Lab, then try subject filtering and safe deletion in the Engineering Challenge.

## 2. What Is Django?

Django is a Python web framework. It provides tools for handling web requests, displaying HTML pages, validating forms and working with databases. Rather than building these features from scratch, you connect Django's components to create a web application.

This project uses Django views to respond to requests, URL patterns to connect addresses to views, templates to create HTML, and a model to describe saved resources.

## 3. Prerequisites

You will need:

- Python 3.10 or newer.
- Git.
- Visual Studio Code (VS Code).
- A web browser.
- An internet connection to copy the template and install Django.

The command for Python depends on your system. It may be `python`, `python3` or `py`. Use the command that runs Python 3.10 or newer on your computer. On Windows, `py` is often available; on macOS and Linux, try `python3`.

To check the version, run one of these commands:

```text
python --version
python3 --version
py --version
```

## 4. Create Your Own Repository from the GitHub Template

1. Open this project’s GitHub repository in a browser.
2. Select **Use this template**, then **Create a new repository**.
3. Choose a repository name and decide whether it should be public or private.
4. Select **Create repository**.

This creates your own copy so that you can make and save changes without changing the template repository.

## 5. Clone the Repository

On the page for your new repository, select **Code** and copy its HTTPS URL. In a terminal, move to the folder where you keep your projects, then replace the example URL with the one you copied:

```text
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

`git clone` downloads your repository to your computer. Move into its new folder:

```text
cd YOUR-REPOSITORY
```

Replace `YOUR-REPOSITORY` with the folder name created by Git.

## 6. Open the Project in VS Code

From the project folder, run:

```text
code .
```

The dot means “open the current folder”. If the `code` command is not available, open VS Code, choose **File > Open Folder**, and select the cloned project folder.

## 7. Create a Virtual Environment

In the VS Code terminal, make sure the current folder contains `manage.py`. Create a virtual environment:

```text
python -m venv .venv
```

If your system uses a different Python command, replace `python` with `python3` or `py`, for example:

```text
py -m venv .venv
```

A virtual environment keeps this project’s Python packages separate from other projects on your computer.

## 8. Activate the Virtual Environment on Windows PowerShell

In the VS Code terminal, choose **PowerShell**, then run:

```powershell
.\.venv\Scripts\Activate.ps1
```

The terminal prompt should begin with `(.venv)` when activation succeeds. If PowerShell says that the script cannot be run, do not change or disable your computer’s security settings. Instead, choose **Command Prompt** as the VS Code terminal and run:

```text
.venv\Scripts\activate.bat
```

## 9. Activate the Virtual Environment on macOS/Linux

In the VS Code terminal, run:

```bash
source .venv/bin/activate
```

The terminal prompt should begin with `(.venv)` when activation succeeds.

## 10. Install Dependencies

With the virtual environment active, run:

```text
python -m pip install -r requirements.txt
```

This installs the packages listed in `requirements.txt` into the active environment. The project currently needs Django only.

If `python` is not the command for your system, use the matching command from the earlier version check, such as `python3 -m pip install -r requirements.txt` or `py -m pip install -r requirements.txt`.

## 11. Apply Database Migrations

Run:

```text
python manage.py migrate
```

Migrations create the database tables Django needs. The local SQLite database file is created automatically and is not included in Git.

## 12. Start the Development Server

Run:

```text
python manage.py runserver
```

Django starts a development web server on your computer. Keep this terminal open while you use the site.

## 13. Open the Application in a Browser

Visit this address:

```text
http://127.0.0.1:8000/
```

The home page will show an empty-state message until resources have been added. The add-resource page is intentionally unfinished in this starter.

## 14. Stop the Server

Return to the terminal that is running the server and press **Ctrl+C**. This stops the web server.

Closing the browser tab only closes the page in your browser; it does not stop the server. Stop the server in its terminal when you have finished.

## 15. Run Automated Tests

With the virtual environment active, run:

```text
python manage.py test
```

Django runs the automated checks in `resources/tests.py` and reports whether they pass.

## 16. Understand the Project Structure

```text
manage.py                          Runs Django management commands
requirements.txt                   Lists the Python dependencies
studyboard/                        Project settings and top-level URLs
resources/                         Resource model, views, URLs and tests
resources/migrations/              Database schema history
resources/templates/resources/     HTML templates
resources/static/resources/        CSS stylesheet
```

The `StudyResource` model defines the fields saved for each resource. A URL pattern sends a browser request to a view. The view retrieves data and renders a template, which supplies the HTML page.

## 17. Guided Code Exploration

During the guided exploration, try to find:

1. The fields on the `StudyResource` model in `resources/models.py`.
2. The URL patterns in `studyboard/urls.py` and `resources/urls.py`.
3. The view that displays the resource list in `resources/views.py`.
4. The template used by that view in `resources/templates/resources/resource_list.html`.
5. How `base.html` is extended by the other templates.
6. The initial database migration in `resources/migrations/0001_initial.py`.
7. The tests that check the working starter pages in `resources/tests.py`.

Follow one request from its URL, to its view, to the template that produces the page.

## 18. Implementation Lab TODOs

Complete `add_resource()` in `resources/views.py` and the form page in `resources/templates/resources/resource_form.html`. The URL `/resources/add/` already displays a safe placeholder.

Use the provided `StudyResourceForm` in `resources/forms.py`. Your implementation should handle GET and POST requests, display and validate the form, save valid resources, redirect after a successful save, and show validation errors when the submitted data is invalid.

The starter intentionally does not include the completed view or form template.

## 19. Engineering Challenge TODOs

### Filter resources by subject

Add optional subject filtering to the home page using a GET query parameter, for example `/?subject=Python`. Follow the TODO markers in `resources/views.py` and `resource_list.html`. The starter displays the submitted filter value but does not filter the resources.

### Delete a resource safely

Complete `delete_resource()` and create the confirmation interaction in `resource_confirm_delete.html`. GET must only show a confirmation page; deletion should only happen after a valid POST. Use Django’s CSRF protection and return a 404 for a resource that does not exist. The starter’s delete view does not delete data.

## 20. Common Problems and Solutions

### Django is not installed

Activate the virtual environment, then install the requirements:

```text
python -m pip install -r requirements.txt
```

If the command cannot find `python`, use the Python command that worked on your system, such as `python3` or `py`.

### VS Code is using the wrong Python interpreter

In VS Code, open the Command Palette with **Ctrl+Shift+P** (Windows/Linux) or **Cmd+Shift+P** (macOS). Choose **Python: Select Interpreter**, then select the interpreter inside this project’s `.venv` folder. Open a new terminal afterwards and activate the environment.

### Virtual environment activation fails

Check that `.venv` exists and that the terminal is in the folder containing `manage.py`. On Windows, use the PowerShell command in section 8, or select Command Prompt and use its activation command. On macOS/Linux, use the command in section 9. Do not disable operating system security settings.

### Migrations have not been applied

If Django reports missing database tables, run:

```text
python manage.py migrate
```

### The port is already in use

Stop another development server that is using the port, or start this server on a different port:

```text
python manage.py runserver 8001
```

Then visit `http://127.0.0.1:8001/`.

### A template cannot be found

Check the spelling of the template name and confirm it is in `resources/templates/resources/`. Keep the server terminal open and read the error details printed there.

### You see an HTTP 404 page

Check that the URL is typed correctly. Resource detail and delete pages need a resource ID that exists in the database. The home page is at `/`.

### The browser says it cannot connect

Check that the development server is running in the terminal and that you opened the correct local address. If you stopped the server with Ctrl+C, start it again with `python manage.py runserver`.

### The browser was closed but the server is still running

Closing a browser tab does not stop Django. Return to the terminal running `runserver` and press **Ctrl+C**.

## 21. Commit and Push Your Work

See which files have changed:

```text
git status
```

Stage your work:

```text
git add .
```

Create a commit with a short description:

```text
git commit -m "Complete Django study resources exercises"
```

Push your commit to your GitHub repository:

```text
git push
```

The first push on a new branch may show a command to set an upstream branch. Follow the command Git prints, then push again. Never add your `.venv` folder or local `db.sqlite3` file to the repository.
