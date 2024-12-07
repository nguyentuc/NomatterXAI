# NoMatterXAI
This is the implementation of the paper [NoMatterXAI: Generating" No Matter What" Alterfactual Examples for Explaining Black-Box Text Classification Models](https://www.arxiv.org/pdf/2408.10528)

### Steps to reproduce our results
```bash
# Clone the repository
git clone https://github.com/nguyentuc/NomatterXAI.git

# Navigate into the directory
cd NomatterXAI/

# Setup python enironment and install dependencies
conda create --name NomatterXAI python==3.11
pip install -r requirements.txt
```

### Running sample scripts can be found in the NoMatterXAI/TextAttack/main/ folder

### Citation

If our work aids your research, please consider citing it as follows:

```bibtex
@article{nguyen2024nomatterxai,
  title={NoMatterXAI: Generating" No Matter What" Alterfactual Examples for Explaining Black-Box Text Classification Models},
  author={Nguyen, Tuc and Michels, James and Shen, Hua and Le, Thai},
  journal={arXiv preprint arXiv:2408.10528},
  year={2024}
}