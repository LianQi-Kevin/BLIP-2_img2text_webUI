# BLIP-2 img2text webUI

This repository is an img2text frontend page for teaching purposes.

Based on [CLIP](https://github.com/pharmapsychotic/clip-interrogator) / [gradio](https://github.com/gradio-app/gradio)

---

### Build environment

#### 1. Server basic configuration

* RTX 3090
* CUDA 11.3
* Miniconda

#### 2. Create conda env

```shell
apt update && apt install net-tools lsof
conda create -n clip python==3.8
conda activate clip
```

#### 3. Install packages

```shell
pip install torch==1.12.0+cu113 torchvision==0.13.0+cu113 torchaudio==0.12.0 --extra-index-url https://download.pytorch.org/whl/cu113
pip install clip-interrogator==0.4.3 gradio==3.17.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
```


----

### version to be used

Use [BLIP-2](https://github.com/salesforce/LAVIS/tree/main/projects/blip2).

##### Install BLIP-2
```shell
conda create -n blip-2 python==3.8
conda activate blip-2
pip install salesforce-lavis==1.0.0 transformers==4.26.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
```

##### References

* https://github.com/salesforce/LAVIS/blob/main/examples/blip2_instructed_generation.ipynb
* https://github.com/salesforce/LAVIS/tree/main/projects/blip2
* https://mp.weixin.qq.com/s/OyLnRKgsklzQ09y9irtdQg