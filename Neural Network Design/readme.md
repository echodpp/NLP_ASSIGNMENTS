We want to design a neural network that segments an English word into prefixes, root, and suffixes using a BIO labelling scheme.
For example, the word “unprepossessing” has the labelling: (“u”, B-pre), (“n”, I-pre), (“p”, B-pre), (“r”, I-pre), (“e”, I-pre), (“p”, B-root), (“o”, I- root), (“s”, I-root), (“s”, I-root), (“e”, I-root), (“s”, I-root), (“s”, I-root), (“i”, B-suf), (“n”, I-suf), (“g”, I-suf). Note that due to the nature of the application, O will not be used.
Fully specify a neural network to solve this problem. Describe:
• how the inputs and outputs are encoded • the structure of the network
• the loss function used
Describe the network in enough detail that one could implement it using PyTorch. You may describe it in terms of common abstractions (e.g. “use a standard LSTM cell of such-and-such size”) if that’s useful.
You do not need to define batch sizes, learning rates, and other optimization parameters.
You may assume that the input contains only lowercase Latin letters.
We want to design a neural network that segments an English word into prefixes, root, and suffixes using a BIO labelling scheme.
For example, the word “unprepossessing” has the labelling: (“u”, B-pre), (“n”, I-pre), (“p”, B-pre), (“r”, I-pre), (“e”, I-pre), (“p”, B-root), (“o”, I- root), (“s”, I-root), (“s”, I-root), (“e”, I-root), (“s”, I-root), (“s”, I-root), (“i”, B-suf), (“n”, I-suf), (“g”, I-suf). Note that due to the nature of the application, O will not be used.
Fully specify a neural network to solve this problem. Describe:
• how the inputs and outputs are encoded • the structure of the network
• the loss function used
Describe the network in enough detail that one could implement it using PyTorch. You may describe it in terms of common abstractions (e.g. “use a standard LSTM cell of such-and-such size”) if that’s useful.
You do not need to define batch sizes, learning rates, and other optimization parameters.
You may assume that the input contains only lowercase Latin letters.
