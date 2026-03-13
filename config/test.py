from Pyro5.api import Proxy

opx = Proxy("PYRO:opx1000@localhost:9090")

# Force the connection and binding immediately
opx._pyroBind() 

# Now check the representation
print(f"INSTRUMENTS: { {'opx1000': opx} }")