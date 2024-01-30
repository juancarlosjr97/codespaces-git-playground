# Codespaces Git Playground

This project is a guide on how to spin up a fully configured dev environment in the cloud ready for development using the blank canvas provided by GitHub using Codespaces.

## Prerequisites

GitHub account created.

- [GitHub](https://docs.github.com/en/get-started/quickstart/creating-an-account-on-github)

## Codespace Benefits: Elevate Your Development Experience 🚀

- Instant, customizable development environment
- Accessible from any device with Internet
- Facilitates real-time collaboration
- Seamless Git and GitHub integration
- Scalable with adjustable resources
- Supports Visual Studio Code extensions
- Container-based isolation for consistency
- Efficient onboarding with time and resource savings
- Disposable environments for testing and experimentation
- GitHub manages underlying infrastructure
- Integrated with GitHub Actions for automation

## Codespace Quickstart using Template

The link below provides a quickstart to spin up an environment using this template as a base project.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/juancarlosjr97/codespaces-git-playground?quickstart=1)

## Creating a repository from a template

Follow this [guide](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) to create a repository from this template.

After creating a project from this template, navigate to the README.md file and switch to code view. Then update the [line 29](#codespace-quickstart-using-template) by replacing `juancarlosjr97/codespaces-git-playground` with the path of the project created. It will be a combination of the GitHub username joined with the name of the GitHub repository as `${GITHUB_USERNAME}/${GITHUB_REPOSITORY}`.

## Developing in Codespace

When a Codespace is created it comes with Git automatically authenticated with the credentials of the associated GitHub account. Additionally it comes with basic tools such as `python` ready to start development. For more information, read the official [GitHub Documentation](https://docs.github.com/en/codespaces/developing-in-a-codespace/developing-in-a-codespace).

## Git Exercise from Codespaces

### Git and Python Version

After you have the Codespace up and running, run the following code from the terminal. Ensure you use capital V for the python version command:

```bash
git -v
python -V
```

The result should be similar to the below code, but it might differ from the versions on each Codespace:

```bash
git version 2.43.0
Python 3.10.13
```

### Running Python script

Execute the below script to run the Python code located in [`main.py`](./src/main.py):

```bash
python -m src.main
```

Upon successful execution, the script will return: `Congratulations, you are running the python script from a GitHub Codespace environment. Now, it is 29-01-2024 22:29 and time for further development.`

Please note that the date and time will vary depending on when the script is run.

### Updating the Script

1. Open the python file located on `./src/main.py`
2. Update the line [4](./src/main.py#L4) by updating the `strftime` to `%d-%m-%Y %H:%M:%S`. This update will format the date to include seconds.
3. Run the Python script again and should return the date as string with seconds. For example, `29-01-2024 22:35:35`.

Congratulations, you have updated the python script!

### Committing and Pushing the changes

After doing the changes, the next steps is to commit and push the changes to your GitHub repository.

_In order to do this step, the project needs to be created from the template in order to have permission to do changes to the project. Follow this steps [Creating a repository from a template](#creating-a-repository-from-a-template)_

1. Stage the changes

   ```bash
   git add src/main.py
   ```

2. Commit the changes

   ```bash
   git commit -m "Adding seconds to date time formatting:"
   ```

3. Push the changes

   ```bash
   git push
   ```

Congratulations! You have successfully staged, committed, and pushed the changes to the remote repository. The dynamic date and time formatting feature has been added to the[`main.py`](./src/main.py) script. Now, it is ready for further collaboration and development.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file.

## Support Information

- [CODESPACES DOCUMENTATION](https://docs.github.com/en/codespaces)
- [LICENSE](./LICENSE.md)
