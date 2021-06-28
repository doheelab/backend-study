
import torch
from torch.autograd import Variable

x = Variable(torch.ones(2, 2), requires_grad=True)
print(x)

y = x + 2
print(y)
print(y.grad_fn)

z = y * y * 3
out = z.mean()

print(z, out)

# 변화도(Gradient)
out.backward()
print(x.grad)



x = torch.randn(3)
x = Variable(x, requires_grad=True)

y = x * 2
while y.data.norm() < 1000:
    y = y * 2

gradients = torch.FloatTensor([0.1, 1.0, 0.0001])
y.backward(gradients)

print(x.grad)




import torch, torchvision
model = torchvision.models.resnet18(pretrained=True)
data = torch.rand(1, 3, 64, 64)
labels = torch.rand(1, 1000)

prediction = model(data) # 순전파 단계(forward pass)

loss = (prediction - labels).sum()
loss.backward() # 역전파 단계(backward pass)

optim = torch.optim.SGD(model.parameters(), lr=1e-2, momentum=0.9)
optim.step() # 경사하강법(gradient descent)


a = torch.tensor([2., 3.], requires_grad=True)
b = torch.tensor([6., 4.], requires_grad=True)
Q = 3*a**3 - b**2

# Q 에 대해서 .backward() 를 호출할 때, autograd는 이러한 변화도들을 계산하고 이를 각 텐서의 .grad 속성(attribute)에 저장합니다.
# Q.sum().backward() 와 같이 Q 를 스칼라(scalar) 값으로 집계(aggregate)한 뒤 암시적으로 .backward() 를 호출할 수도 있습니다.
external_grad = torch.tensor([1., 1.])

Q.backward(gradient=external_grad)

# 수집된 변화도가 올바른지 확인합니다.
print(9*a**2 == a.grad)
print(-2*b == b.grad)