# Github API Testing
Some simple scripts to learn how to use the Github API. 

## Aims
From this, I aim to be more familiar with the API and using APIs in general.

## Project Setup (Python)
1. Create a Virtual Environment using `python3 -m venv <venv_name>`. Make sure this is done within the project's folder.
2. Activate the Environment using `source <venv_name>/bin/activate` (MacOS/Linux) or `<venv_name>\Scripts\activate.bat` (Windows).
3. Install the project's prerequisits using `pip3 install -r python/requirements.txt`.
4. Create a .env file containing a TOKEN and USERNAME variable. A Personal Access Token can be generated on Github.

You can now execute and modify the Python code.

To exit the Virtual Environment, use `deactivate`.

## Project Setup (JavaScript)
1. Run `npm install`.
2. Create a .env file containing a TOKEN and USERNAME variable. A Personal Access Token can be generated on Github.

You can now execute and modify the JS script.

## Findings
After experimenting with the API's basic functionality, I feel like JavaScript is the better option for the task. I think the Octocat module used made it much easier than using the Requests library in Python.
Although, I believe Python does have some alternatives to the Requests library so they may be better and more user friendly.

Also, in practice, the API calls would have extensive error handling using the response status. For example, if a status 404 (not found) is thrown, throw an error message.

## Resources Used
- [JavaScript API Documentation](https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api?apiVersion=2022-11-28)
- [Octokit.js](https://docs.github.com/en/rest/guides/scripting-with-the-rest-api-and-javascript?apiVersion=2022-11-28)
- [Python API Guide](https://thepythoncode.com/article/using-github-api-in-python)
