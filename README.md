# Insta-Helper
InstaHelper is an Instagram bot🤖 designed to automate interactions and manage your account efficiently.

## Installing dependencies

After cloning the repository, install the dependencies by running the following command:

```sh
pip install -r requirements.txt

```
## Usage
Entry point of the program is `main.py`. Run the following command to start the program:

```sh
python main.py
```

## Important note
User data such as login and password are located in `user_data.py`. Make sure to fill in the required fields before running the program.
And when this data changes, it is necessary that their changes are not tracked

And this is how it should be done using commands:

Excluding a file from tracking:
```sh
git update-index --assume-unchanged user_data.py
```

Return to tracking changes:
```sh
git update-index --no-assume-unchanged user_data.py
```