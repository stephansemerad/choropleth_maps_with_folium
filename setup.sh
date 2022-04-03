# Idea from
# https://towardsdatascience.com/mapping-with-matplotlib-pandas-geopandas-and-basemap-in-python-d11b57ab5dac
# https://public.opendatasoft.com/explore/dataset/world-administrative-boundaries/export/

# 1. Set Up Virtual Env
python -m venv venv      
venv\scripts\activate

# 2. Installations 
python -m pip install pyshp 
python -m pip install numpy 
python -m pip install pandas 
python -m pip install matplotlib 
python -m pip install seaborn 
python -m pip install xlrd
python -m pip install openpyxl

# 3 - create requirments.txt
pip freeze > requirements.txt

# 4 - deactivate
deactivate