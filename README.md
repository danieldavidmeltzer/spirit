

# Spirit

###Stats
[![codecov](https://codecov.io/gh/danieldavidmeltzer/spirit/branch/master/graph/badge.svg)](https://codecov.io/gh/danieldavidmeltzer/spirit)
[![Build Status](https://travis-ci.com/danieldavidmeltzer/spirit.svg?branch=master)](https://travis-ci.com/danieldavidmeltzer/spirit)
<h4>Spirit Project For Advanced System Design class.</h4>


## Installation

1. Clone the repository and enter it:

    ```shell script
    $ git clone git@github.com:danieldavidmeltzer/spirit.git
    ...
    $ cd spirit/
    ```

### optional steps(you can skip to running)

- Run the installation script and activate the virtual environment:

    ```shell script
    $ ./scripts/install.sh
    ...
    $ source .env/bin/activate
    [spirit] $
    ```

- To check that everything is working as expected, run the tests:
    ```shell script
    $ pytest tests/
    ```

## Running

```shell script
./run_pipline.sh
```
this should start all the dockers and install everything
after that you can just use spirit.client and it should work fine.

it could take some time to run. 
#Basics
## Usage

   The `spirit` package provides a command-line interface,use flag --help to start:
   ```shell script
    $ python -m spirit.client --help
   ```

## Client

this is the only part not automated by the `run_pipeline.sh`. to make 
sure this works please run client. use 
`python -m spirit.client upload-sample <path>`

this should work with the system you ran through the pipline.
## Website:

go to http://127.0.0.1:8080/users to see all the users, if it's blank is 
because, well there are no users... see Client section. 

select a user, you could see users snapshots than and well.. view them.

 
# Advanced

## Documentation
 See [full documentation](https://readthedocs.org/projects/spirit-daniel/).
 it's not much, but it's something.
 
## Parsing (generally, not snapshots) utility

generally parsing means a way to handle item when there are
few 'parsers' to handle it. we use this for 3 main things in the project:
1. encoders - encode representation into protobuf 
which you can then convert to bytes and send.
2. constructors - given a protobuf item we want to create a representation for
us to work with
3. parsers - in the meaning of parsing a result which parse snapshots 
and create results.


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


## run_pipline.sh 

the script does the following steps:
1. generate random keys
2. create network 
3. run minio 
4. create minio main bucket
5. run rabbitmq 
6. halt till rabbitmq setup completes
7. run mongodb
8. creates project image from python 3
9. creates & runs all the images required form the said image
10. enjoy

### website notes
- in order to run with the webpage the gui needs image api uri,
- this should be the image api uri that is accessible for the web user.
 
- the reason it can't use the api is because the api usually
 will be on host.docker.internal, which is not accessiable from webpage

### Known issues

- the website has a problematic pagination which if stays on the snapshots of 
the users for too long can download all he's images unrequited.
- no way to auto create parser
- lack of tests, due to time limitations, and mostly complexity of 
testing components that require docker containers to be tested.
- bad web site/design, again time limitations.
- running on flask development server, for now.


# Enjoy :)