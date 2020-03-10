

# Spirit


[![codecov](https://codecov.io/gh/danieldavidmeltzer/spirit/branch/master/graph/badge.svg)](https://codecov.io/gh/danieldavidmeltzer/spirit)
[![Build Status](https://travis-ci.com/danieldavidmeltzer/spirit.svg?branch=master)](https://travis-ci.com/danieldavidmeltzer/spirit)
<br>  
Spirit Project For Advanced System Design.

## Documentation
 See [full documentation](https://readthedocs.org/projects/spirit-daniel/).

## Installation

1. Clone the repository and enter it:

    ```shell script
    $ git clone git@github.com:danieldavidmeltzer/spirit.git
    ...
    $ cd spirit/
    ```

2. Run the installation script and activate the virtual environment:

    ```shell script
    $ ./scripts/install.sh
    ...
    $ source .env/bin/activate
    [spirit] $
    ```

3. To check that everything is working as expected, run the tests:
    ```shell script
    $ pytest tests/
    ```

## Running

```shell script
run_pipline.sh
```
this should start all the dockers and install everything
after that you can just use spirit.client and it should work fine.

it could take some time to run. 
#Basic
## Usage

   The `spirit` package provides a command-line interface,use flag --help to start:
   ```shell script
    $ python -m spirit.client --help
   ```

# Advanced

## parsing(generally not snapshots) utility

generally parsing means a way to handle item when there are
few 'parsers' to handle it. we use this for 3 main things in the project:
1. encoders - encode representation into protobuf 
which you can then convert to bytes and send.
2. constructors - given a protobuf item we want to create a representation for
us to work with
3. parsers - in the meaning of parsing a result which parse results.



## Adding a parser

in order to add a parser all you need is to add a parser under 
`parsers` package. 
you can either write a class which receives the item, context
 in the init, and the
other elements in the parse part , or you can write a function 
like the pose parser.
you of course will need to add an encoder for the new result but the saver
should be able to pick it up with no change, make sure to change the cli+gui 
accordingly.

### Known issues

- the website has a problematic pagination which if stays on the snapshots of 
the users for too long can download all he's images unrequiredly.
- no way to auto create parser
- lack of tests, due to time limitations
- bad web design, again time limitations

