The verify work on the original WBLPN, the basic source code is from https://github.com/cryptolu/whitebox-LPN.

The accurate rate compute code is shown in ``SuccessRateWBLPN.py``.

Three verify works are contained in this work, the rate test of the original WBLPN (contains the version with pool and without pool) and the operation time test.

You can use

```
Sage ...
```

and 

```
Sage ...
```
to run the rate test work.
Both of the two work operations on random choose trace expect the several nodes are the linear shares.

The command 
```
sage
```
is used to test the speedy of the original WBLPN, where it contains the time of running WBLPN against a simuation dummy shuffling as the parameters set in our paper.
An interesting thing is chosing random row in the pool for Ms in each loop is the mainly time complexity in the operation, which is about 10 times as other code.
For the purpose of fairness, the time test results in our paper ___do not___ contains this time, since we consider this can be optimized by the precompuations phase.
That is, this random chosen trace index can be chosen in the offline phase and directly used in the WBLPN operation.
