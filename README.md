# Cross-modal Deep Face Normals with Deactivable Skip Connections
Victoria Fernández Abrevaya*, Adnane Boukhayma*, Philip H. S. Torr, Edmond Boyer (*Equal contrib.).</br> 
[CVPR 2020 (Oral)](https://arxiv.org/abs/2003.09691)</br> 
<img src="teaser.jpg"/>

## Requirements
+ Python 2.7
+ PyTorch 0.3

## Data preprocessing
download the [`dlib` trained facial shape predictor](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2). Put file `shape_predictor_68_face_landmarks.dat` in directory `data`.

Input images are assumed to be crops of fixed size around the face. Using `dlib`, this command finds the tightest rectangular box of edge size
 `l ` containing the face. Images are then cropped with a square patch of size `1.2xl`. Input images are located in `data/original` and cropped images are saved in `data/cropped`.
```
python crop.py
```

## Testing
Comming soon..

## Acknowledgement
This work was supported by the ERC grant ERC-2012-AdG 321162-HELIOS, the EPSRC grant Seebibyte EP/M013774/1 and the EPSRC/MURI grant EP/N019474/1.

## License
<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.
