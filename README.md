Smart Store - Brandon J

📁 Project Setup Steps

✅ 1. Cloned Repository
git clone https://github.com/brandonjbbb/smart-store-brandon.git
cd smart-store-brandon
✅ 2. Created Virtual Environment (Mac)
python3 -m venv .venv
✅ 3. Activated Virtual Environment
source .venv/bin/activate
✅ 4. Installed Requirements
python3 -m pip install --upgrade -r requirements.txt
✅ 5. Verified Project Files in VS Code
Opened project in VS Code
Confirmed presence of:
README.md
.gitignore
requirements.txt
data/raw/ folder with CSV files
utils/logger.py
scripts/data_prep.py
✅ 6. Ran Initial Script
python3 scripts/data_prep.py
or if needed:

python3 -m scripts.data_prep
✅ 7. Git Workflow Commands Used
git add .
git commit -m "Add starter files and setup project"
git push -u origin main
✅ 8. Cleaned Up Large Files
Added .venv/ to .gitignore
Removed .venv from tracking:
git rm -r --cached .venv
git commit -m "Removed .venv from repository tracking"
git push
✅ Project Setup Complete!
