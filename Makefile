.PHONY: lint
lint:
  flake8 --exclude=.git,pycache,.venv,*/migrations/ --ignore=E501,F403,F405,E126,W503

.PHONY: clean
clean:
  find . -name '*.pyc' -delete
  find . -name 'pycache' -delete
  rm -rf .coverage .cache .pytest_cache