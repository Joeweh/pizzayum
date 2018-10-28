from pizzapy.store import StoreLocator
from pizzapy.order import Order

import info
import sys

me = info.CUSTOMER
store = StoreLocator.find_closest_store_to_customer(me)
order = Order.begin_customer_order(me, store)
card = info.CARD

order.add_item('20BCOKE')

testing = str(input('Testing? ')).upper()
if testing == 'YES':
    order.pay_with(card)
elif testing == 'NO':
    order.place(card)
    store.place_order(order, card)
else:
    print('Must answer "YES" or "NO".')

sys.exit(0)
