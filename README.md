# KCNI Sumer School 2022 - Whole-Brain + Cognitive Network Modelling Project Week


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



