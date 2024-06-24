import torch
import torch.nn as nn

class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        partition = x_exp.sum(0, keepdims=True)
        return x_exp / partition

data = torch.Tensor([1, 2, 3])
my_softmax = MySoftmax()
output = my_softmax(data)
print(output)