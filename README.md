# OmniORB - remote communitaction

## 1. Create and activate a CONDA env on both computers:

    $ conda create -n omni-env -c conda-forge python=3.10 omniorb omniorbpy

    $ conda activate omni-env

## 2. Generate Python Code from IDL on both computers:

    $ omniidl -bpython RemoteMiddleware.idl

## 3. Run the OmniORB Service on both computers:

    $ omniNames -start

## 4. Run the Server on computer A:

    $ python RemoteMiddlewareServer.py

## 5. Run the Client on computer B:

    $ python RemoteMiddlewareClient.py

## 6. Enter the IOR obtained from the server terminal on computer A (step 4):

    $ Enter IOR of Greetings object:

    IOR:010000001a...

## 7. It is possible to interact beetwen computers!
