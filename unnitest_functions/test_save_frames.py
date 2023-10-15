"""
Esse módulo tem como objetivo verificar o funcionamento da função 'save_frames', que pertence 
ao módulo 'matheus_vis.py'. Para resumir, a função recebe o objeto plot (visualização), o ano analizado, 
mes analizado e o caminho para a pasta onde a imagem deverá ser salva.
"""

import sys, os

esse_caminho = os.path.dirname(os.path.abspath(__file__))
caminho_functions = os.path.join(esse_caminho, "..", "functions")
sys.path.append(caminho_functions)

import matplotlib.pyplot as plt
import unittest
import pandas as pd  
from utils import set_anabolizantes
from matheus_vis import save_frames

class TestSaveFrames(unittest.TestCase):
    """
    a classe vai conter os diferentes testes feitos para a função
    """

    