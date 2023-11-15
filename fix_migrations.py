import pathlib
import config.settings as django_settings

for app_name in django_settings.INSTALLED_APPS:
    folder_path = pathlib.Path(app_name)
    if folder_path.exists() and folder_path.is_dir():
        models_file_path = folder_path / 'models.py'
        models_folder_path = folder_path / 'models'
        if models_file_path.exists() or models_folder_path.exists():
            (migrations_folder := folder_path / 'migrations').mkdir(parents=True, exist_ok=True)
            (init_file := migrations_folder / '__init__.py').touch(exist_ok=True)
            print(f'{init_file.relative_to(".")} created.')
