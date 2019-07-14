# -*- coding: utf-8 -*-
import logging
import sys

_logger = logging.getLogger(__name__)


def import_all():
    from IPython.display import display as dis
    from collections import defaultdict, namedtuple, Counter
    from contextlib import contextmanager
    from datetime import datetime, timedelta
    from decimal import Decimal
    from functools import partial as part
    from math import sqrt
    from pdb import set_trace as st
    from statsmodels.formula.api import ols
    from time import time

    import csv
    import logging
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import networkx as nx
    import numpy as np
    import pandas as pd
    import pickle
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

    setup_logging()


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
