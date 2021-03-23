import os
from unittest import TestCase
from DropletML import droplet
import torch


class TestDroplet(TestCase):

    def test_droplet(self):
        a = torch.tensor([1,2,3])