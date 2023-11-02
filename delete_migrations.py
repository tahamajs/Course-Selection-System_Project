import pathlib

for path in pathlib.Path('.').glob('**/*.py'):
    if ('venv' not in path.parts) and path.name.endswith('_initial.py'):
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
