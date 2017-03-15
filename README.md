# Lab Number 1

In this lab the point is to get you thinking with a test mindset. What we have here is a simplistic KNN Regression tool. What you will do is take a look at regression.py and complete the tasks labeled with TODO.

# Environment

To get your environment running you will need Python 3.5.x (I've tested both). You will also have to install some packages:

```
pip install ipython pandas numpy scipy sklearn matplotlib
```

# To run the experiment

I highly recommend using ipython to do you development with.

In a console you can run

```
import regression
```

which will load the Regression class

from there you can run the command

```
r = Regression()
r.plot_error_rates()
```

This won't work on first pass so feel free to also rely on importlib to reload the library

```
import importlib
importlib.reload(regression)
```

So you don't have to leave the console.

Good luck and please ask questions in Slack if you get stuck. This is your time to learn!



