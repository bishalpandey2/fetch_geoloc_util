## Installation Guide

### Prerequisites
Ensure you have Python **3.8+** installed. You can check your Python version by running:
```bash
python --version
```
If Python is not installed, download it from [Python's official website](https://www.python.org/downloads/).

### Installing Dependencies
Clone this repository and navigate into the project folder:
```bash
git clone git@github.com:bishalpandey2/fetch_geoloc_util.git
cd fetch_geoloc_util
```

Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application
To fetch geolocation data for a city, use:
```bash
python src/main.py "New York"
```

### Running Tests
To run the test suite, execute:
```bash
pytest tests/
```

### Installing as a CLI Tool
To install the project as a command-line utility:
```bash
pip install .
```
Usage:
```bash
geoloc-util --locations “Madison, WI” “12345”
geoloc-util “Madison, WI” “12345” “Chicago, IL” “10001”
```

### Uninstalling
To remove the installed package:
```bash
pip uninstall geoloc_util
```

### Troubleshooting
- Ensure all dependencies are installed.
- If issues persist, try upgrading pip:
  ```bash
  pip install --upgrade pip
  ```
- For API-related errors, ensure your API key in `src/config.py` is valid.

For further assistance, refer to the documentation or raise an issue in the repository.
