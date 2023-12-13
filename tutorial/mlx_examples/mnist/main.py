import argparse
import time

import numpy as np

import mlx.core as mx
import mlx.nn as nn
import mlx.optimizers as optim

import mnist


class MLP(nn.Module):
    """
    A simple MLP - Multi Layer Perceptron example for implementing MNIST
    """

    def __init__(self, num_layers: int, input_dim: int, hidden_dim: int, output_dim: int):

        super().__init__()
        
        # this will have all the size informaton across layers
        layer_sizes = [input_dim] + [hidden_dim] * num_layers + [output_dim]

        # Note: this is a simple trick to use the matrix chain multiplication
        self.layers = [
            nn.Linear(idim,odim)
            for idim, odim in zip(layer_sizes[:-1], layer_sizes[1:])
        ]

    def __call__(self, x):
        """
        Comment here what does the call special function in nn.Module does
        """
        for l in self.layers[:-1]:
            x = mx.maximum(l(x), 0.0)
        return self.layers[-1](x)  # for now this seems like a max polling
    

def loss_fn(model, X, y):
    return mx.mean(nn.losses.cross_entropy(model(X), y))

def eval_fn(model, X, y):
    return mx.mean(mx.argmax(model(X), axis=1) == y) # this returns the accuracy

def batch_iterate(batch_size, X, y):
    perm = mx.array(np.random.permutation(y.size)) # this gives a randomized indices to take in batch.
    for s in range(0, y.size, batch_size):
        ids = perm[s: s + batch_size]
        yield X[ids], y[ids] # this will prevent not having to return everything at once

def main():
    seed = 0
    num_layers = 2
    hidden_dim = 32
    num_classes = 10
    batch_size = 256
    num_epochs = 10
    learning_rate = 1e-1

    np.random.seed(seed)

    # Loading the data
    train_images, train_labels, test_images, test_labels = map(mx.array, mnist.mnist())

    # Loading the model
    model = MLP(num_layers, train_images.shape[-1], hidden_dim, num_classes)
    mx.eval(model.parameters())


    loss_and_grad_fn  = nn.value_and_grad(model, loss_fn)
    optimizer = optim.SGD(learning_rate=learning_rate)

    for e in range(num_epochs):
        tic = time.perf_counter()
        for X, y in batch_iterate(batch_size, train_images, train_labels):
            loss, grads = loss_and_grad_fn(model, X, y)
            optimizer.update(model, grads)
            mx.eval(model.parameters(), optimizer.state)

        accuracy = eval_fn(model, test_images, test_labels)
        toc = time.perf_counter()

        print(
            f"Epoch {e}: Test accuracy {accuracy.item():3f},"
            f"Time {toc - tic:.3f} (s)"
        )


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Train a simple MLP on MNIST using MLX")
    parser.add_argument("--gpu", action="store_true", help="Use the metal-backend")
    args = parser.parse_args()

    if not args.gpu:
        mx.set_default_device(mx.cpu)
    
    main()