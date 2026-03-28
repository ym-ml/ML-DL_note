import torch
import torchvision
from torchvision import transforms

def load_data_fashion_mnist(batch_size, resize=None):
    """Download the Fashion-MNIST dataset and then load it into memory.

    Defined in :numref:`sec_utils`"""
    trans = [transforms.ToTensor()]
    if resize:
        trans.insert(0, transforms.Resize(resize))
    trans = transforms.Compose(trans)
    mnist_train = torchvision.datasets.FashionMNIST(
        root="../data", train=True, transform=trans, download=True)
    mnist_test = torchvision.datasets.FashionMNIST(
        root="../data", train=False, transform=trans, download=True)
    return (torch.utils.data.DataLoader(mnist_train, 
                                        batch_size, 
                                        shuffle=True, # DDP need to use DistributedSampler
                                        num_workers=get_dataloader_workers(),
                                        pin_memory=True, # pin_memory=True can speed up data transfer to GPU
                                        prefetch_factor=2, # 每个worker预取2个batch的数据 2~4
                                        persistent_workers=True, #保持worker进程存活,适用于epoch较多时
                                        ), 

            torch.utils.data.DataLoader(mnist_test, batch_size, shuffle=False,
                                        num_workers=get_dataloader_workers()))

def get_dataloader_workers():
    """Use 4 processes to read the data.

    Defined in :numref:`sec_utils`"""
    return 4