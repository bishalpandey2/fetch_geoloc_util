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
python src/main.py "Los Angeles"
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

### Cypress API Tests
Cypress is used to test API responses from OpenWeather's Geolocation API.

#### **Install Cypress**
Make sure you have Node.js installed, then install Cypress:
```bash
npm install cypress --save-dev
```

### Installing TypeScript
Cypress tests are written in **TypeScript**, so TypeScript must be installed. Run the following command:
```bash
npm install typescript @types/node @cypress/webpack-preprocessor --save-dev
```
Additionally, install Cypress type definitions:
```bash
npm install @types/cypress --save-dev
```

### Configuring TypeScript for Cypress
Ensure `tsconfig.json` is present in the root directory with the following configuration:
```json
{
  "compilerOptions": {
    "target": "ES6",
    "lib": ["es2016", "dom"],
    "module": "CommonJS",
    "moduleResolution": "Node",
    "allowJs": true,
    "outDir": "./dist",
    "strict": true,
    "baseUrl": "./",
    "paths": {
      "@/*": ["./src/*"]
    },
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["cypress/**/*.ts"],
  "exclude": ["node_modules", "dist"]
}
```

#### **Run Cypress Tests**
To execute all Cypress API tests in **headless mode**:
```bash
npx cypress run
```
To open Cypress Test Runner for an interactive test run:
```bash
npx cypress open
```
Then select `geolocation.cy.ts` to run the tests.

#### **Cypress Test Cases Include:**
✅ Fetching geolocation data by **city and state**
✅ Fetching geolocation data by **zip code**
✅ Handling **multiple locations**
✅ Testing **invalid inputs** (invalid city, zip code)
✅ Checking **API response time**

### Troubleshooting
- Ensure all dependencies are installed.
- If issues persist, try upgrading pip:
  ```bash
  pip install --upgrade pip
  ```
- For API-related errors, ensure your API key in `src/config.py` is valid.

For further assistance, refer to the documentation or raise an issue in the repository.
