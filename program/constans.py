from dydx3.constants import API_HOST_GOERLI, API_HOST_MAINNET
from decouple import from django.conf import settings

# !!!! SELECET MODE !!!!
MODE = "DEVELOPMENT"


# CLose all open positions and orders

ABORT_ALL_POSITIONS = False


# Find cointegrated pairs

FIND_COINTEGRATED = True

#Place Trades
PLACE_TRADES = True

# RESOLUTION


RESOLUTION = "1HOUR"


# sTATS WIndow
WINDOW = 21


# THresholds - Opneing

MAX_HALF_LIFE = 24 
ZSCORE_THRESH = 1.5
USD_PER_TRADE = 50
USD_MIN_COLLATERAL = 1880

# THRESHOLDS - CLosing
CLOSE_AT_ZSCORE_CROSS = True

# Ethereum Address
ETHEREUM_ADDRESS = ""