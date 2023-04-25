

# Place market order

def place_market_order(client, market, side, size, price, reduce_only):
    # Get Position Id
account_response = client.private.get_account()
position_id = account_response.data["account"]["positionId"]

# Get expiration time
server_time = client.public.get_time()
expiration = datetime.fromisoformat(server_time.data["iso"].replace("Z", "")) + timedelta(seconds=70)

# Place an order
placed_order = client.private.create_order(
  position_id=position_id, # required for creating the order signature
  market="BTC-USD",
  side="SELL",
  order_type="MARKET",
  post_only=True,
  size='0.005',
  price='45000',
  limit_fee='0.015',
  expiration_epoch_seconds=expiration.timestamp(),
  time_in_force="FOK", 
  reduce_only=False
)

# aBort all open positions
def abort_all_positions(client):
    pass