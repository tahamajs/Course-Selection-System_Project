import pathlib
import sys

if input("ARE YOU SURE ? (Yes/no)") != 'Yes':
    print('Good Decision.')
    sys.exit()

for path in list(pathlib.Path('.').glob('**/*.py')):
    if ('venv' not in path.parts) and ('migrations' in path.parts) and ('__init__.py' not in path.parts):
        # print(path.absolute())
        print(path.relative_to('.'))
        try:
            path.unlink()
            print('deleted.')
        except FileNotFoundError as e:
            print('not found!')

try:
    db = pathlib.Path('db.sqlite3')
    print(db.relative_to('.'))
    db.unlink()
    print('deleted.')
except FileNotFoundError as e:
    print('not found!')

print('EVERYTHING IS ON FIRE !')
