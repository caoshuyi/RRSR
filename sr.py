import torch
import torch.nn as nn
from math import sqrt


class Net(nn.Module):
	def __init__(self):
		super(Net, self).__init__()
		self.input = nn.Conv2d(in_channels=1, out_channels=64, kernel_size=3, stride=1, padding=1, bias=False)
		self.conv1 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1, padding=1, bias=False)
		self.conv2 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1, padding=1, bias=False)
		self.conv3 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1, padding=1, bias=False)
		self.output = nn.Conv2d(in_channels=64, out_channels=1, kernel_size=3, stride=1, padding=1, bias=False)
		self.relu = nn.ReLU(inplace=True)

		for m in self.modules():
			if isinstance(m, nn.Conv2d):
					n = m.kernel_size[0] * m.kernel_size[1] * m.out_channels
					m.weight.data.normal_(0, sqrt(2. / n))

	def forward(self, x):
		residual = x
		inputs = self.input(self.relu(x))
		out = inputs

		for _ in range(6):
			out = self.conv3(self.relu(self.conv2(self.relu(self.conv1(self.relu(out))))))
			out = torch.add(out, inputs)

		out = self.output(self.relu(out))
		out = torch.add(out, residual)

		return out
