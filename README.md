# Setup Instructions for Machine Learning Project

## 1. Clone the Repository
If you haven't already cloned the repository, run:
```sh
git clone git@github.com:JBrink8/MSCG_IllitchW25.git
cd MSCG_IllitchW25
```

## 2. Set up Data
Download the Illitch csv files via MSCG Shared Drive. Create a directory titled 'data'
at the top of the MSCG_IllitchW25 directory. Move csv files into the data directory.

## 3. Set Up a Virtual Environment

### 🔹 Create a Virtual Environment
```sh
python3 -m venv venv
```

### 🔹 Activate the Virtual Environment
- **Windows (Command Prompt):**
  ```sh
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```sh
  source venv/bin/activate
  ```

## 4. Install Dependencies
Once the virtual environment is activated, install the required dependencies:
```sh
pip install -r requirements.txt
```

## 5. Launch Jupyter Notebook
To start JupyterLab and begin working on the project:
```sh
jupyter lab
```

## 6. Deactivate the Virtual Environment
When finished, deactivate the virtual environment:
```sh
deactivate
```

## Notes
- Ensure you have Python installed (recommended: Python 3.8+).
- If `pip` or `venv` is not found, make sure Python is properly installed and added to your system path.
- If using `conda`, replace `venv` setup with:
  ```sh
  conda create --name ml_project python=3.8
  conda activate ml_project
  pip install -r requirements.txt
  ```

