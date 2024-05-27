The verify work on the original WBLPN, the basic source code is from https://github.com/cryptolu/whitebox-LPN.

The accurate rate compute code is shown in ``SuccessRateWBLPN.py``.

Three verify works are contained in this work, the rate test of the original WBLPN (contains the version with pool and without pool) and the operation time test.

You can use

```
Sage VerRateWBLPN.sage m c
```

and 

```
Sage VerRateWBLPN_pool.sage m c Nt
```
to run the rate test work.
m is the size of verify matrix, c is the threshold value and Nt is the trace used in all the attack (Nt = m + Tp).
Both of the two work operations on random choose trace expect the several nodes are the linear shares.

The command 
```
sage RunTimeWBLPN.sage Ns Bytei w T
```
is used to test the speedy of the original WBLPN, where it contains the time of running WBLPN against a simuation dummy shuffling as the parameters set in our paper.
