# Instruction to run this repo
* clone the repository

```
python3 -m pip install --upgrade pip setuptools

pip install numpy cython

cd openpifpaf
python3 -m pip install --editable '.[train,test]'

time CUDA_VISIBLE_DEVICE=0,1 python3 -m openpifpaf.train --batch-size=8 \
--basenet=shufflenetv2x2 \
--head-quad=1 \
--epochs=1 \
--momentum=0.9 \
--headnets \
pif \
paf \
--lambdas \
30 \
2 \
2 \
50 \
3 \
3 \
--loader-workers=16 \
--lr=0.1 \
--lr-decay \
120 \
14 \
--no-pretrain \
--weight-decay=1e-5 \
--update-batchnorm-runningstatistics \
--ema=0.03 \
--no-augmentation \
```
python3 -m pip install --editable '.[train,test]'


# Related Projects

* [monoloco](https://github.com/vita-epfl/monoloco): "Monocular 3D Pedestrian Localization and Uncertainty Estimation" which uses OpenPifPaf for poses.
* [openpifpafwebdemo](https://github.com/vita-epfl/openpifpafwebdemo): web front-end.


# Citation

```
@InProceedings{kreiss2019pifpaf,
  author = {Kreiss, Sven and Bertoni, Lorenzo and Alahi, Alexandre},
  title = {PifPaf: Composite Fields for Human Pose Estimation},
  booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  month = {June},
  year = {2019}
}
```


[CC-BY-2.0]: https://creativecommons.org/licenses/by/2.0/
