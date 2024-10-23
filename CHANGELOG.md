# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.4] - 2024-10-23

### Added

- Exception `ApiKeyTypeError`
- Mock API for test endpoints

### Changed

- Changed to pyproject.toml instead of setup.py

### Fixed

- Fixed passing boolean values as strings

### Removed

- `setup.cfg`.
- `setup.py`.

## [1.0.3.4] - 2024-10-17

### Added

- python-publish.yml
- __init__.py in tests

## [1.0.3.3] - 2024-10-15

### Added

- Badges in README files.

## Changed

- Uncommented `install_requires` line in setup.py.

## [1.0.3.2] - 2024-10-13

### Added

- The tests have been supplemented.

### Fixed

- `Predictions` model.

### Changed

- `Timezones` model renamed to `Timezone`.

## [1.0.3] - 2024-10-11

Updated to API [3.9.3](https://www.api-football.com/documentation-v3#section/Changelog) version.

### Added

- CHANGELOG.md.
- Tests.
- Field `extra` in `Fixtures` endpoint.
- Parameter `dates` in `Fixtures/Rounds` endpoint.
- Parameter `half` in `Fixtures/Statistics` endpoint.
- Parameter `ids` in `Injuries` endpoint.
- Edit `Fixtures/Rounds` model.
- Edit `Fixtures/Statistics` model.
- New endpoint `Players/Profiles`.
- New endpoint `Players/Teams`.
- New model `Players/Profiles`.
- New model `Players/Teams`.

[1.0.3.4]: https://github.com/h3ave/apisports_football/tree/db22e0ddda891a19cf9ee622e41cf700b2dbd2f3
[1.0.3.3]: https://github.com/h3ave/apisports_football/tree/12a7599b60eff91c14034fe1aa862cf196ea1965
[1.0.3.2]: https://github.com/h3ave/apisports_football/tree/bd64c34ed2588046d55222ec5817a7e139118b67
[1.0.3]: https://github.com/h3ave/apisports_football/tree/db68dd3e55b79e5afca3faa1edc43ee9b6623f5e
