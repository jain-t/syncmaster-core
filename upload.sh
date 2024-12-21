rm -rf dist build
python setup.py sdist bdist_wheel
twine upload dist/*
git add .
git commit -m "update"
git push origin main
