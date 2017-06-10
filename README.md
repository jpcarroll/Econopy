# Econopy
_____________________________________________________________________________________
Economic Inequality Metrics in Python for My Thesis

  - Supports Python 2 and 3 
  - Requires Numpy and  Matplotlib 
_____________________________________________________________________________________
# Setup

  - Installation
  - Examples

### Installation


```sh
$ git clone https://github.com/jpcarroll/Econopy.git
$ cd Econopy
$ python setup.py install
```

### Examples:

```sh
import econopy as ep
import numpy as np

j = np.array([241,104,93,346,228,487,173,222,9,188])

k = np.array([299,427,317,311,269,263,22,342,382,159])

l = np.array([-330,0,322,273,156,25,52,186,308,315])
```

To calculate the Gini Coefficient:
```sh
print (ep.gini(j))
$  0.332711621234
```

To calculate the Hill's alpha parameter:
```sh
print (ep.hill(k))
$  1.42639302646
```

To graph a Cumulative distribution function (CDF) 
```sh
ep.cdf(j) 
```

![CDF](https://image.prntscr.com/image/tHM5UfOkTom4JA5KwP4GiA.png)

The Gini coefficient can also accept zeros and negative numbers:
```sh
print (ep.gini(l))
$  0.77895944912
```

