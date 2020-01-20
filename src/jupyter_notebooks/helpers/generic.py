# -*- coding: utf-8 -*-

import sys

def sort_python_path():
    """
    Priority package:
      1. /usr/local packages (i.e. spark)
      2. /opt/conda
      3. All the rest
    """
    def _key_path(p):
        if p.startswith('/usr/local'):
            return 0
        if p.startswith('/opt/conda'):
            return 1
        return 2

    sys.path = sorted(sys.path, key=_key_path)

sort_python_path()

from IPython.display import display as dis
from collections import defaultdict, namedtuple, Counter
from contextlib import contextmanager
from datetime import datetime, timedelta
from decimal import Decimal
from functools import partial as part
from gzip import GzipFile
from io import BytesIO
from ipywidgets import interact, fixed
from math import sqrt
from pdb import set_trace as st
from statsmodels.formula.api import ols
from time import time

import boto3
import botocore
import csv
import hashlib
import json
import logging
import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
import pickle
import os
import random
import scipy as sp
# This conflicts for some reason with joblib Parallel.
# Disabling the import for seaborn
# import seaborn as sns
import sklearn
import statsmodels.api as sm
import sys
import traceback

pd.set_option('display.max_colwidth', -1)
pd.set_option("display.max_rows", 120)
pd.set_option("display.max_columns", 120)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

# sns.set_context("poster")
# sns.set(rc={'figure.figsize': (16, 9.)})
# sns.set_style("whitegrid")

_logger = logging.getLogger(__name__)


def pickle_it(obj, file_path):
    """
    Parameters
    ----------
    obj : object
        Any python obj
    file_path: str
        The file path name
    """
    pickle.dump(obj, open(file_path, 'wb'))


def unpickle_it(file_path):
    """
    Parameters
    ----------
    file_path: str
        The file path name
    """
    return pickle.load(open(file_path, 'rb'))


def setup_logging(loglevel=logging.INFO):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(
        level=loglevel, stream=sys.stdout,
        format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
    )


def open_expand(file_path, *args, **kwargs):
    """
    Allows to use '~' in file_path.
    """
    return open(os.path.expanduser(file_path), *args, **kwargs)


def _exception_handler(error_type, error_value, error_traceback):
    """Log all uncaught exceptions at runtime with sys.excepthook"""
    logging.exception("Uncaught exception {} {}".format(
        str(error_type), str(error_value)))
    tb = traceback.format_exception(
        error_type, error_value, error_traceback)
    traceback_string = ''
    for ln in tb:
        traceback_string += ln
    logging.exception(traceback_string)

    
def setup_logging(format=None, level=logging.INFO, handlers=None):
    """
    To log to a file instead of stdout:
    
    >>> setup_logging(handlers=[logging.FileHandler("myfile.log")])
    """
    if format is None:
        format="%(asctime)s %(levelname)s %(message)s"
        
    if handlers is None:
        handlers=[logging.StreamHandler()]
        
    # Use sys.excepthook to handle any uncaught exceptions
    sys.excepthook = _exception_handler
    
    logging.basicConfig(
        format=format,
        level=level,
        handlers=handlers,
    )