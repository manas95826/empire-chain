# empire chain
.PHONY: clean build publish

clean:
	rm -rf dist empire_chain.egg-info

build: clean
	python3 -m build

publish: build
	twine upload dist/*

.DEFAULT_GOAL := publish 