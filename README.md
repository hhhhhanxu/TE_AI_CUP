# TE_AICUP
## This is the sensor parameter detection project of TE AI CUP
##### This project is to test the position, force, speed and other parameters of the crimping machine to determine whether the product is qualified for crimping.
## The project mainly consists of two parts, the GUI interface made by PyQT5 and the neural network model based on PyTorch.
##### The CORE code for inference is in the CORE folder, containing both preprocessing and inference files. Trained models are among them.
##### The rest of the code contains the QT interface, scripts for data retrieval, and main functions.
## Dependency libraries mainly contain：
##### \
python==3.8.0 \
pytorch==1.4.0 \
pyqt5==5.15.0 \
numpy==1.19.2 \
requests==2.23.0 \
BS4==4.9.0 \
matplotlib = 3.2.1 \
scipy = 1.4.1
