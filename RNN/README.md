Consider the following regression problem. There is a sequence of words representing positive integers, e.g.
["three", "one", "four", "one", "five", "two", "five", "three", "five"]
and we want to know the product of the associated numbers. The result for the above example should be 9000.
Construct, manually, a RNN structure and associated weights that will solve this problem. This should be in the form of a flowchart identi- fying inputs and outputs, weights, sums, and activation functions, along with any necessary auxiliary text. Assume that the numbers are in [1, 5] (but as their string names). Note that your activation functions can be any scalar function.
HINT: log(xy) = log(x) + log(y)
