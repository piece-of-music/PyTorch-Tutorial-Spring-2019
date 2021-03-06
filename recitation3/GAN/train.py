# PyTorch tutorial codes for course EL-7143 Advanced Machine Learning, NYU, Spring 2018
# train.py: trainig convolutional or linear neural networks for MNIST classification
import time, datetime

from Pipeline.option import args
from Pipeline.run import train

start_time = datetime.datetime.now().replace(microsecond=0)
print('\n---Started training at---', (start_time))

for epoch in range(1, args.epochs + 1):
    train(epoch)
    current_time = datetime.datetime.now().replace(microsecond=0)
    print('Time Interval:', current_time - start_time, '\n')