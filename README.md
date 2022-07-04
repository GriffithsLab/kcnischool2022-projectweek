# KCNI Sumer School 2022 - Whole-Brain + Cognitive Network Modelling Project Week

## About the project



## Setup Intructions


### 1. Clone repo

(Better: fork first, then clone your fork and add this repo as upstream)

```bash
git clone git@github.com:mygithubusername/kcnischool2022-projectweek
cd kcnischool2022-projectweek
git remote add upstream https://github.com/griffithslab/kcnischool2022-projectweek
git fetch upstream
git merge upstream/main
```

### 2. Setup Python env

```bash
conda activate myenv
```

### 3. Download data

```bash
cd data
python download_ds000201_data.py
cd ..
```

### 4. Look at the example notebooks

( in the `notebooks`  folder )

### 5. Get cracking!

When you're ready, pull request (PRs) back to main:

First add your new stuff on a feature branch in your fork:
```bash
git checkout -b "mynewfeature"
git add mynewfile.ipynb
git commit mynewfile.ipynb -m"comment on mynewfile"
git push -u origin mynewfeature
```

...then submit a PR from your github fork, where this push will appear!



### 5. Further reading:

https://www.biorxiv.org/content/10.1101/2022.05.19.492664v1

https://www.biorxiv.org/content/10.1101/2022.06.09.494069v1

https://www.jneurosci.org/content/33/27/11239 [PDF](https://drive.google.com/file/d/1ImucIqk5Cl-8fXVKzal8jY5IaiP5pLgw/view?usp=sharing)

https://openneuro.org/datasets/ds000201/versions/1.0.3


