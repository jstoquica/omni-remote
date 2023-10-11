from omniORB import CORBA
import RemoteMiddleware, RemoteMiddleware__POA

class RemoteCalculator_i(RemoteMiddleware__POA.RemoteCalculator):
    def add(self, x, y):
        print(f"Received request to add {x} and {y}")
        return x + y

orb = CORBA.ORB_init([], CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")
poaManager = poa._get_the_POAManager()
poaManager.activate()

calculator = RemoteCalculator_i()
obj = calculator._this()

print(orb.object_to_string(obj))
print("Remote Middleware Server ready...")

orb.run()

