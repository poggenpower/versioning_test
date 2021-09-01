from copy import copy, deepcopy
import json
from collections import defaultdict
import logging
import argparse
import os
import re
import operator
import time
import signal
import sys
import paho.mqtt.client as mqtt
import yaml
import prometheus_client as prometheus
from yamlreader import yaml_load
import utils.prometheus_additions

__version__ = '1.3.1'
SUFFIXES_PER_TYPE = {
    "gauge": [], 
    "counter": ['total'],
    "counter_absolute": ['total'],
    "summary": ['sum', 'count'],
    "histogram": ['sum', 'count', 'bucket'],
    "enum": [],
}
