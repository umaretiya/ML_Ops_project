from housing.entity.config_entity import DataIngestionConfig 
from housing.entity.artifact_entity import DataIngestionArtifact
from housing.exception import HousingException
from housing.logger import logging

import os,sys,tarfile
from six.moves import urllib

import pandas as pd 
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
