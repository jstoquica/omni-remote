from omniORB import CORBA
import RemoteMiddleware

orb = CORBA.ORB_init([], CORBA.ORB_ID)
ior = input("Enter IOR of RemoteCalculator object: ")

obj = orb.string_to_object(ior)
calculator = obj._narrow(RemoteMiddleware.RemoteCalculator)

if calculator is None:
    print("Object reference is not a RemoteCalculator")
else:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    result = calculator.add(x, y)
    print(f"Result received from Remote Middleware Server: {result}")

