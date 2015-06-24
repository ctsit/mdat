# Change Log
All notable changes to the MDAT project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [0.3.0] - 2015-06-24
### Added
- Add setup.py and revise README.md to match (Philip Chase)
- Add main function and test_data.json to assist in testing (Philip Chase)
- Write BestAlternative class (Philip Chase and Alex Loiacano)

### Changed
- Relocate test data to 'sample_data' folder and add test data sets (Philip Chase)
- Refactor to simplify calling on command line (Philip Chase)
- Add 'jsonschema' to modules installed by travis during testing (Philip Chase)


## [0.2.0] - 2015-06-09
### Changed
- Turned mdat into a package (Alex Loiacono)
- Rename project from Mefdas to mdat (Philip Chase)
- Move unit tests into tests/ folder (Philip Chase)

### Added
- Add travis CI testing (Philip Chase)
- Stub out new class BestAlternative and provide example JSON input code (Philip Chase)
- Add ChoquetIntegral class
- Add whiteboard image of a fuzzy measure calculation with 3-4 criteria (Philip Chase)
- Add whiteboard image of shapley value calculation (Philip Chase)

## [0.1.1] - 2015-05-22
### Changed
- Added project name to readme

## [0.1.0] - 2015-05-22
### Added

- Initial release
- Add FuzzyMeasure class to compute a fuzzy measure given a dictionary of criteria and values
