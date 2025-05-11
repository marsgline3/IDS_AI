from scapy.all import sniff, IP, TCP, UDP
import time
import threading
from collections import defaultdict, deque
import numpy as np
import pandas as pd
import joblib as jb


# Load model 
model = jb.load('rf_model.joblib')

#flow cache
flows = {}

#lock for thread safety
lock = threading.Lock()

#Sniffing funtion (to be run in a background thread)
def packet_handler(packet):
    pass
def flow_timeout_checker():
    pass

#Sniffing
sniff(prn=packet_handler, store=False)