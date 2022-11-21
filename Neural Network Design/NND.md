# Neural Network Design
- Input : [ u, n, p, r, e, p, o, s, s, e, s ,s, i, n, g ] 
- Output: [(“u”, B-pre), (“n”, I-pre), (“p”, B-pre), (“r”, I-pre), (“e”, I-pre), (“p”, B-root), (“o”, I- root), (“s”, I-root), (“s”, I-root), (“e”, I-root), (“s”, I-root), (“s”, I-root), (“i”, B-suf), (“n”, I-suf), (“g”, I-suf)]
<img width="968" alt="Screen Shot 2022-11-21 at 12 37 27 PM" src="https://user-images.githubusercontent.com/90811429/203124898-cecf68c1-bdef-463d-80c4-ca7d789400c3.png">
  
  
## Overview
This is a many to many model with different length of input and output. we can simply the output to 6 different lables in this particular example. Them we split the model into two parts, we have a 
 encoder that inputs the letter and produces a hidden vector. The encoder is built with an Embedding layer that converts the words into a vector and a recurrent neural network (RNN) that calculates the hidden state, here we will be using Long Short-Term Memory (LSTM) layer.

Then the output of the encoder will be used as input for the decoder. For the decoder, we will be using LSTM layer again, as well as a dense layer that predicts the lables.


## Encoder
There are several ways of embedding
- one hot encoding: Each word encoded by one hot representation is a dimension, independent of each other. Which will produce a large number of redundant sparse matrix and ,The relationship between dimensions (words) is not reflected
- transformers:Transformer is a pure use of attention force encoder-decoder.Both the encoder and decoder have n transformer blocks
in each block using multi-headed (self-)attention forces, location-based feedforward networks, and layer normalization
- Wav2vec:It is a method of converting words into vectors, which contains two algorithms, skip-gram and CBOW. The major difference between them is that skip-gram is to predict the words around the central word by the central word, while CBOW is to predict the central word by the surrounding words.
- Distributed representation: word will be label in two groups (B/I) and (pre/root/suf) so we can encode the input u :[1,1,0,1,0,0] n:[2,0,1,1,0,0] r:[3,0,1,1,0,0]....
 we sometimes also add linear layer to multiply encoder and decoder.
```
embedding = Embedding(input_dim=6 , output_dim=6,)(input_sequence)
encoder = LSTM(64, return_sequences=False)(embedding)
```

## Decoder
The output of the encoder layer will be the hidden state of the last time step. We will then need to feed this vector into the decoder.
```
r_vec = RepeatVector(input)(encoder)
decoder = LSTM(64, return_sequences=True, dropout=0.2)(r_vec)
``` 
## Model
Here we are using LSTM model because we need take previous and later input letter intp consideration with the classification.LSTM networks are well-suited to classifying, processing and making predictions based on time series data, since there can be lags of unknown duration between important events in a time series.

## loss fuction
Lastly, we stack the layers to create the model and add a function loss.
we also need Softmax and Cross-entropy loss function.The objective is to calculate for cross-entropy loss given these information. Softmax is continuously differentiable function. This makes it possible to calculate the derivative of the loss function with respect to every weight in the neural network.

```
enc_dec_model = Model(input_sequence, Activation('softmax')(logits))
enc_dec_model.compile(loss=sparse_categorical_crossentropy,
              optimizer=Adam(1e-3),
              metrics=['accuracy'])
enc_dec_model.summary()
```

## using pytorch
```
import torch
from torch.autograd import Variable
import torch.nn as nn

torch.manual_seed(1)
input_size =  1
hidden_size = 32
batch_size = 5
sequence_length = 6
num_layers = 1

class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, sequence_length):
        super(LSTM, self).__init__()

        self.num_layers = num_layers
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.sequence_length = sequence_length

        self.lstm = nn.LSTM(input_size=input_size, hidden_size=hidden_size, batch_first=True)

    def forward(self, x):
        # (num_layers * num_directions, batch, hidden_size)
        h_0 = (Variable(torch.zeros(self.num_layers, x.size(0), self.hidden_size)) for _ in range(self.hidden_size))
        # Reshape input
        x.view(x.size(0), self.sequence_length, self.input_size)

        out, _ = self.lstm(x, h_0)

        return out

lstm = LSTM(input_size, hidden_size, num_layers, sequence_length)
print (lstm)

criterion = torch.nn.MSELoss()
optimizer = torch.optim.Adam(lstm.parameters(), lr=0.1)
```
