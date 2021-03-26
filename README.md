# SecML Malware plugin

![PyPI](https://img.shields.io/pypi/v/secml_malware?style=flat-square)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/zangobot/secml_malware?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues/zangobot/secml_malware?style=flat-square)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/secml_malware?style=flat-square)
![PyPI - Downloads](https://img.shields.io/pypi/dm/secml_malware?style=flat-square)


This is a plugin for the [SecML](https://secml.gitlab.io) Python library.
There is a [pre-trained MalConv](https://github.com/endgameinc/ember) model trained by EndGame, included in this project for testing.

# Included Attacks

* **Partial DOS Header manipulation**, formulated by [Demetrio et al.](https://arxiv.org/abs/1901.03583)
* **Padding attack**, formulated by [Kolosnjaji et al.](http://pralab.diee.unica.it/sites/default/files/kolosnjaji18-eusipco.pdf)
* **GAMMA**, formulated by [Demetrio et al.](https://arxiv.org/abs/2003.13526)
* **FGSM padding + slack** formulated by [Kreuk et al.](https://arxiv.org/abs/1802.04528) and [Suciu et al.](https://arxiv.org/abs/1810.08280)
* **Content shifting and DOS header extension** formulated by [Demetrio et al.](https://arxiv.org/pdf/2008.07125.pdf)


# Installation

Navigate to the folder where you want to clone the project.
I recommend creating a new environment (I use `conda`):
```bash
conda create -n secml_malware_env python=3.7
conda activate secml_malware_env
pip install secml-malware
pip install git+https://github.com/endgameinc/ember.git
```
You also need to install `pytorch`, [find instructions here](https://pytorch.org/get-started/locally/). 


## Troubleshooting possible errors

If you encouter problem due to *libmagic*, [follow this instruction](https://github.com/ahupp/python-magic#installation).
If, for some reason, the installation through *pip* does not work, install `ember` and `pytorch` as described before, then:
```bash
git clone https://github.com/zangobot/secml_malware.git
cd secml_malware
pip install -r requirements.txt
```

# How to use
Activate your environment, and import the `secml_malware` package inside your script:
```python
import secml_malware
print(secml_malware.__version__)
```
The tests included in this project show how the library can be used for applying the manipulation to the input programs.
There is also an [example Jupyter notebook tutorial](https://github.com/zangobot/secml_malware/blob/master/attack_tutorial.ipynb) that shows how to build a apply a standard attack.

# Docker
There is also a `Dockerfile` that can be used to start a container and test the library without messing with virtual environments!
```bash
docker build --tag secml_malware:0.2 .
docker run --rm -it secml_malware:0.2 bash
```
The container is also shipped with `ipython`, for a more interactive experience with this library.

# Cite
Depending on the manipulations / formalization you are using, please cite our work:

**Content shifting and DOS header extension  manipulations** or **RAMEn formalization**
```bibtex
@article{demetrio2020adversarial,
    title={Adversarial EXEmples: A Survey and Experimental Evaluation of Practical Attacks on Machine Learning for Windows Malware Detection},
    author={Luca Demetrio and Scott E. Coull and Battista Biggio and Giovanni Lagorio and Alessandro Armando and Fabio Roli},
    year={2020},
    eprint={2008.07125},
    archivePrefix={arXiv},
    primaryClass={cs.CR}
}
``` 

**GAMMA**
```bibtex
@misc{demetrio2021functionalitypreserving,
      title={Functionality-preserving Black-box Optimization of Adversarial Windows Malware}, 
      author={Luca Demetrio and Battista Biggio and Giovanni Lagorio and Fabio Roli and Alessandro Armando},
      year={2021},
      eprint={2003.13526},
      archivePrefix={arXiv},
      primaryClass={cs.CR}
}

```

**Partial DOS manipulation**
```bibtex
@inproceedings{demetrio2019explaining,
  title={Explaining Vulnerabilities of Deep Learning to Adversarial Malware Binaries},
  author={Luca Demetrio and Battista Biggio and Giovanni Lagorio and Fabio Roli and Alessandro Alessandro},
  booktitle={ITASEC19},
  volume={2315},
  year={2019}
}

```

# Bug reports
If you encounter something strange, feel free to open an issue! I am working a lot, and bugs are present everywhere.
Let me know, and I'll try to fix them as soon as possible.

# Testing
I provide a small test suite for the attacks I have developed inside the plugin.
If you want to run them, **ADD GOODWARE/MALWARE samples!**
There are two distinct folders: 
```
secml_malware/data/goodware_samples
secml_malware/data/malware_samples/test_folder
```
Please, add samples to both folders (**if and only if** you want to run the internal tests).
