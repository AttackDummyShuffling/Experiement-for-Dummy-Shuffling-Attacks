The verify work on the Verify-Matrix-Changed (VMC) WBLPN, the source code is based on the works https://github.com/cryptolu/whitebox-LPN.

The accurate rate compute code is shown in ``SuccessRateVMC.py``.

Two verify works are contained in this work, the rate test of the VMC-WBLPN (contains the version with pool and without pool) and the operation time test.

You can use

```
Sage VerRateVMC.sage m c
```

and 

```
Sage VerRateVMC_pool.sage m c Nt
```
to run the rate test work.
m is the size of verify matrix, c is the threshold value and Nt is the trace used in all the attack (Nt = m + Tp).
Both of the two work operations on random choose trace expect the several nodes are the linear shares.
