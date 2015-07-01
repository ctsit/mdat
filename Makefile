
help:
	@echo
	@echo "Available tasks:"
	@echo "  test           : execute python setup.py test"
	@echo "  sdist          : execute python setup.py sdist"
	@echo "  pypi_register  : register the mdat PyPI package"
	@echo "  pypi_upload    : upload the mdat package to PyPI"
	@echo "  clean          : remove generated files"
	@echo

test:
	python setup.py test

sdist:
	python setup.py sdist

pypi_config:
	@test -f ~/.pypirc || echo "Please create the ~/.pypirc file first. Here is a template: \n"
	@test -f ~/.pypirc || (cat pypirc && exit 1)

pypi_register: pypi_config
	python setup.py register -r mdat

pypi_upload: pypi_config
	@# use secure submission: https://packaging.python.org/en/latest/distributing.html
	which twine || pip install twine
	@#python setup.py sdist --formats=zip upload -r mdat
	python setup.py sdist --formats=zip
	twine upload dist/* -r mdat
	@echo "Done. To test please execute:"
	@echo "virtualenv venv && . venv/bin/activate && pip install mdat && mdat -h"

clean:
	find . -type f -name "*.pyc" -print | xargs rm -f
	@rm -rf out dist build *.egg-info *.egg
