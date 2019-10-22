## pytorch_lmdb_imagenet

Convert ImageNet dataset to lmdb, adapted from [https://github.com/Lyken17/Efficient-PyTorch](https://github.com/Lyken17/Efficient-PyTorch)



1. Change Imagenet train set and val set to lmdb

```
python folder2lmdb.py
```

2. Test the dataset

```
python dataset_test.py
```

3. Train Imagenet

```
python train_imagenet.py /path/to/dataset/imagenet/  --lmdb
```