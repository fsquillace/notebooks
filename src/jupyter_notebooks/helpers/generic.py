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
import seaborn as sns
import sklearn
import statsmodels.api as sm
import sys

pd.set_option('display.max_colwidth', -1)
pd.set_option("display.max_rows", 120)
pd.set_option("display.max_columns", 120)

sns.set_context("poster")
sns.set(rc={'figure.figsize': (16, 9.)})
sns.set_style("whitegrid")

_logger = logging.getLogger(__name__)


def pickle_it(obj, file_path):
    """
    Parameters
    ----------
    obj : object
        Any python obj
    filename: str
        The file path name
    """
    pickle.dump(obj, open(file_path, 'w'))


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
