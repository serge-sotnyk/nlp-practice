# Another fast.ai Deep Learning Playground

## Why another repo?

Here are the main differences:
* Python:
    * Uses pyenv, a useful tool to manage multiple versions of python on one machine.
    * Uses pyenv-virtualenv
* Setup CLI:
    * Operations are idempotent (they do not recreate things if they already exist).
    * Setup everything using an AWS `--profile`
    * Create/restore volume snapshots, to save a bit of money
    * Use on demand or spot instances.
* Dogs vs Cats (Lesson 1, 2).
    * Added `download_data.sh` to download data from Kaggle.
    * Added `prepare_data_for_validation.sh` to create a random validation set.
    * Added `prepare_data_for_test.sh` to merge everything back again.
    * Refactored the python code from the notebooks into modules.
    * Added `submit_predictions.sh`

## Setup AWS

Refer to the [AWS install wiki page](http://wiki.fast.ai/index.php/AWS_install).

I have made step-by-step setup guide [here](setup/Readme.md). This setup has a number of differences:
* Setup instructions using the AWS console interface as of July 2017.
* Using an AWS `profile` argument instead of using the `default` profile.
* Commands to start/stop/reboot instances are split up into `.sh` files (instead of a single `commands.txt`).
* Does not open up instance ports (needed for Jupyter)


## Local project setup

First, install [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv).

Set up your environment using [install_local.sh](install_local.sh):

```
$ ./install_local.sh
```

This will:
* Install `anaconda2-4.4.0` (using `pyenv`) and use it for this project.
* Create a virtualenv called `(fast.ai)`
* Install all the dependencies listed in `requirements.txt` and `dev_requirements.txt`

You're ready! To activate this virtualenv:

```bash
$ source activate fast.ai
```

And do deactivate:

```bash
$ source deactivate
```

