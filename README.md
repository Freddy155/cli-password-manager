# CLI Password Manager

The **CLI Password Manager** is a simple command-line tool that allows you to generate, store, and retrieve passwords securely. This tool creates a hidden directory in your home directory to store your passwords and encryption key.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Generate Password](#generate-password)
  - [Store Password](#store-password)
  - [Retrieve Password](#retrieve-password)
- [Contributing](#contributing)

## Getting Started

### Prerequisites

Before you use the CLI Password Manager, you'll need to have the following installed:

- Python
- pip (Python package manager)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Freddy155/cli-password-manager.git
   ```
1.  Navigate to the project directory:

    ```bash
    cd cli-password-manager
    ```

2.  Create a virtual environment (optional but recommended):
     ```bash
     python -m venv venv
     ```
    

3.  Activate the virtual environment:

    -   On Windows:

        ```bash
        venv\Scripts\activate
        ```

    -   On macOS and Linux:

         ```bash
         source venv/bin/activate
         ```

4.  Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

Now, you're ready to use the CLI Password Manager.

Usage
-----

The CLI Password Manager provides the following commands:

### Generate Password

You can generate a secure password with the `generate_password` command. The tool will prompt you to enter the desired password length.

```bash
python app.py generate_password
```

### Store Password

Use the `store_password` command to securely store a password. You will be prompted to provide the service name, username, and password.

```bash
python app.py store_password
```


### Retrieve Password

To retrieve a stored password, use the `retrieve_password` command. You will be asked to enter the service name for which you want to retrieve the password.

```bash
python app.py retrieve_password
```


The tool will display the service name, username, and password for the specified service if it exists in the stored data.

Contributing
------------

Contributions to this project are welcome! You can fork the repository, make changes, and create a pull request. Please follow the contribution guidelines in the repository.
