# PyTestor

PyTestor is a little tool to help refactoring python UnitTests to Pytest tests. The project is still under development 
but can already be used hence taking account of the fact there will be some errors, but it will still spare you much 
time.

## Installation

There is no installation procedure yet, just unzip or clone the repository and you can start working with it.

## Usage

To use the tool you run it with the folder to refactor as an argument. Keep in mind the original test files will be 
replaced, so keep a backup at hand.

    python3.4 pytestor.py <directory>
    
The application will output all test-files followed bu all found assertions:
 * green: refactored (but at the moment not guaranteed to be 100% working)
 * red: not recognised by the application, please let me know or do a pull request.
 