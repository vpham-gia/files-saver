## Scripts to saves modified files from a specific folder

### Setup instructions and run project
This project uses Mac OS X 10.13.6 and Python 3.7.2.
In order to run the code, two options are possible:
1. Use existing virtual environment `.venv/` folder containing installed libraries - must be in `files-saver/` folder
  ```
  cd files-saver/
  source activate.sh
  ```

2. Set up a similar virtual environment (could be automated using `source init.sh`):
  1. Create a python virtual environment: `python3 -m venv .venv`
  2. Activate this newly created venv: `source activate.sh`
  3. Upgrade pip: `pip install --upgrade pip`
  4. Install requirements: `pip install -r requirements.txt`

Once the virtual environment is activated, code could be run using the following command line:  
```
python files-saver/my_script.py
```  
