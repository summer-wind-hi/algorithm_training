# set_a = set((1, 2, 3))
# set_a.add(4)
# print(set_a)
#
# set_b = set([5, 6, 7])
# set_b.add(2)
# print(set_b)
#
# set_c = set_a.union(set_b)
# print(set_c)
#
# set_d = set_a.intersection(set_b)
# print(set_d)

class Parent(object):
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def speak(self):
        print("my name is {0}, and I'm {1} years old".format(self.name, self.age))


class Son(Parent):
    def __init__(self, n, a, g):
        super(Son, self).__init__(n, a)
        self.grade = g

    def speak(self):
        print("my name is {0}, and I'm {1} years old, I'm in grade {2:3d}".format(self.name, self.age, self.grade))


# son = Son("helen", 19, 9)
# son.speak()


#class property + class method
class Person(object):
    count = 0

    @classmethod
    def how_many(cls):
        print(cls.count)

    @staticmethod
    def how_many_static():
        print(Person.count)

    def __init__(self, name):
        self.name = name
        Person.count += 1

    def get_name(self):
        print("my name is  {}".format(self.name))

# xiaoming = Person("xiaoming")
# Person.how_many()
#
# xiaomei = Person("xiaomei")
# xiaomei.how_many()
# xiaomei.how_many_static()


# operator override
class MyVector(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "MyVector({}, {})".format(self.a, self.b)

    def __add__(self, other):
        return MyVector(self.a + other.a, self.b + other.b)

# v1 = MyVector(1, 2)
# v2 = MyVector(3, 4)
# print(v1 + v2)
# print(MyVector)


def my_test(func):
    print("a")
    # func()

    return func()

@my_test
def my_print():
    print("my print")


# error and except
def my_test_except(a):

    assert a > 5, "a should be > 5"

    if a > 10:
        raise Exception("a should be < 10")

# try:
#     my_test_except(11)
#
# except AssertionError as err:
#     print(err)
#
# except:
#     print("other error")
#
# else:
#     print(" 5 < a < 10")
#
# finally:
#     print("done")
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

# download datasets, and generate dataloader
train_set = datasets.MNIST(root="data",
                              train=True,
                              download=True,
                              transform=ToTensor)
train_dataloader = DataLoader(datasets=train_set,
                              batchsize=64,
                              shuffle=True)

device = "cuda" if torch.cuda.is_available() else "cpu"
# create model and instance
class Mnist(nn.Module):
    def __init__(self):
        super(Mnist, self).__init__()
        self.flatten = nn.Flatten()
        self.fc = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10)
        )

    def forward(self, x):
        out = self.flatten(x)
        out = self.fc(out)

        return out

model = Mnist().to(device)

# define loss and optimizer
loss_fn = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=1e-3)

# start to train
def train(dataloader, model, loss_fn, optimizer):
    model.train()
    for batch, (x, y) in enumerate(dataloader):
        x, y = x.to(device), y.to(device)

        # forward + loss + clear grad  + backward + update
        pred = model(x)
        loss = loss_fn(pred, y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()


def test(dataloader, model, loss_fn):
    model.eval()
    for batch, (x, y) in enumerate(dataloader):
        x, y = x.to(device), y.to(device)
        with torch.no_grad():
            pred = model(x)

            loss = loss_fn(pred, y)

