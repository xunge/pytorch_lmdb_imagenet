from folder2lmdb import ImageFolderLMDB
from torch.utils.data import DataLoader
from torchvision.transforms import Resize


if __name__ == "__main__":
    transform = Resize((224, 224))
    path = "/home/jiang/share/dataset/imagenet/train.lmdb"
    dataset = ImageFolderLMDB(path, transform)
    data_loader = DataLoader(dataset, batch_size=256, num_workers=10)
    for img, label in data_loader:
        # pass
        print(img.shape)
        print(label.shape)
