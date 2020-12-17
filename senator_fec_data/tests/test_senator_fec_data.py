from senator_fec_data import __version__
from senator_fec_data import senator_fec_data as sfd
from bs4 import BeautifulSoup
import os
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from xml.etree.ElementTree import parse

key = os.getenv("FEC_API_KEY")

def test_version():
    assert __version__ == '0.1.0'
    
def test_get_api_key():
    key1 = sfd.get_api_key("FEC_API_KEY")
    assert type(key) == str
    assert key == key1
    
def test_get_senator_list():
    senatorlist = sfd.get_senator_list()
    assert type(senatorlist).__name__ is 'DataFrame'
    
def test_get_senator(state):
    senators = sfd.get_senator("MA")
    assert type(senators) == obj
    
def test_get_senator_id(senator, key):
    id_ = sfd.get_senator_id("Elizabeth Warren", key)
    assert id_ == 'S2MA00170'
    assert type(id_) == str
    
def test_get_fec_totals_senator(senator, key):
    warren_total = sfd.get_fec_totals_senator("Elizabeth Warren", key)
    assert type(warren_total).__name__ is 'DataFrame' 
    
def test_get_fec_totals_state(state, key):
    MA_total = sfd.get_fec_totals_state("MA", key)
    assert type(warren_total).__name__ is 'NoneType' 
    
def test_lifetime_contributions_senator(senator, key):
    warren_life_c = sfd.lifetime_contributions_senator("Elizabeth Warren", key)
    assert type(warren_life_c) == str
    assert warren_c_life == "Elizabeth Warren has raised a total of $47963846.95 in unitemized contributions in his or her life."
    
def test_lifetime_contributions_state(state, key):
    ma_life_c = sfd.lifetime_contributions_state("MA", key)
    assert type(ma_life_c).__name__ is 'NoneType'
    
def test_lifetime_expenditures_senator(senator, key):
    warren_life_e = sfd.lifetime_expenditures_senator("Elizabeth Warren", key)
    assert type(warren_life_e) == str
    assert warren_c_life == "Elizabeth Warren has spent a total of $69572641.42999999 through his or her campaigns for the Senate."
    
def test_lifetime_expenditures_state(state, key):
    ma_life_e = sfd.lifetime_expenditures_state("MA", key)
    assert type(ma_life_e).__name__ is 'NoneType'
    
    
def test_get_fec_expenditures_senator(senator, key):
    warren_plot = sfd.get_fec_expenditures_senator("Elizabeth Warren", key)
    assert type(warren_plot) != str
    assert type(warren_plot) != int
    
def test_get_fec_expenditures_state(state, key):
    ma_plot = sfd.get_fec_expenditures_state("MA", key)
    assert type(ma_plot) != str 
    assert type(ma_plot) != int

def test_get_fec_contributions_senator(senator, key):
    warren_plot_c = sfd.get_fec_contributions_senator("Elizabeth Warren", key)
    assert type(warren_plot_c) != str
    assert type(warren_plot_c) != int
    
def test_get_fec_expenditures_state(state, key):
    ma_plot_c = sfd.get_fec_contributions_state("MA", key)
    assert type(ma_plot_c) != str 
    assert type(ma_plot_c) != int  
    
def test_full_report_senator(senator, key):
    full_report_warren= sfd.full_report_warren
    assert type(full_report_warren).__name__ is 'NoneType'
    
    
    
    

