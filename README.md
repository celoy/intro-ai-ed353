# Introduction to AI: Principles, Algorithms and Practice

Doctoral course for ED 353 (Marseille) · Christophe Eloy, Centrale Méditerranée & IRPHE

This course offers an introduction to the foundations of modern machine learning, from linear regression and gradient descent to neural networks and deep reinforcement learning. Each two-hour session combines a blackboard lecture deriving the key ideas with a short guided Jupyter notebook that participants can revisit and complete at their own pace. The emphasis is on understanding what these methods actually do, when they work, and why they fail. No prior experience with machine learning is required, though basic linear algebra and Python are assumed.

## Sessions

| # | Topic | Notebooks |
|---|-------|-----------|
| 0 | Python warm-up (self-study, not covered in class; solutions included) | [00a Python basics](notebooks/00a_python_basics.ipynb) [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/celoy/intro-ai-ed353/blob/main/notebooks/00a_python_basics.ipynb)<br>[00b NumPy and Matplotlib](notebooks/00b_numpy_matplotlib.ipynb) [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/celoy/intro-ai-ed353/blob/main/notebooks/00b_numpy_matplotlib.ipynb)<br>[00c Object-oriented programming](notebooks/00c_object_oriented_programming.ipynb) [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/celoy/intro-ai-ed353/blob/main/notebooks/00c_object_oriented_programming.ipynb) |
| 1 | Introduction, linear and multivariate regression | [01a Linear regression](notebooks/01a_linear_regression.ipynb) [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/celoy/intro-ai-ed353/blob/main/notebooks/01a_linear_regression.ipynb)<br>[01b Multivariate regression](notebooks/01b_multivariate_regression.ipynb) [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/celoy/intro-ai-ed353/blob/main/notebooks/01b_multivariate_regression.ipynb) |
| 2 | Bias–variance trade-off, regularization and gradient-descent variants | [02a Bias–variance and regularization](notebooks/02a_bias_variance_regularization.ipynb) [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/celoy/intro-ai-ed353/blob/main/notebooks/02a_bias_variance_regularization.ipynb)<br>[02b Optimizers](notebooks/02b_optimizers.ipynb) [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/celoy/intro-ai-ed353/blob/main/notebooks/02b_optimizers.ipynb) |
| 3 | Good practices: model selection, model reduction and feature extraction | *coming soon* |
| 4 | Introduction to classification, logistic regression, SVMs | *coming soon* |
| 5 | Other classifiers and clustering | *coming soon* |
| 6 | Neural networks and the backpropagation algorithm | *coming soon* |
| 7 | Deep supervised learning, convolutional networks | *coming soon* |
| 8 | Markov processes | *coming soon* |
| 9 | Reinforcement learning | *coming soon* |
| 10 | Deep reinforcement learning | *coming soon* |

Notebooks are added as the course progresses; run `git pull` before each session to get the new ones.

## Running the notebooks

There are three ways to run the notebooks. All of them install everything needed for the whole course at once.

### 1. Google Colab (nothing to install)

Click a Colab badge above, then run the first cell of the notebook: it downloads the data. You need a Google account. Use *File › Save a copy in Drive* to keep your work.

### 2. Python + venv

Requires Python 3.10 or newer.

```bash
git clone https://github.com/celoy/intro-ai-ed353.git
cd intro-ai-ed353
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

Next time, only `cd intro-ai-ed353`, `source .venv/bin/activate` and `jupyter lab` are needed.

### 3. conda

```bash
git clone https://github.com/celoy/intro-ai-ed353.git
cd intro-ai-ed353
conda env create -f environment.yml
conda activate intro-ai
jupyter lab
```

### Notes

- Tested on macOS with Python 3.14, NumPy 2.5, pandas 3.1, Matplotlib 3.11, scikit-learn 1.9 and PyTorch 2.15. Any Python from 3.10 on should work.
- PyTorch is the largest dependency. On Linux machines without an NVIDIA GPU, you can save several gigabytes by installing the CPU-only build first: `pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu`, then `pip install -r requirements.txt`.
- To avoid conflicts when you `git pull`, do your own work in a copy of each notebook placed in the `work/` folder (create it; git ignores it), or save the notebook under a new name.

## Data

- `notebooks/Data/*_temperature.dat`, `holland_seawater.dat`: monthly temperatures, from Mark Bakker's [Exploratory Computing with Python](http://mbakker7.github.io/exploratory_computing_with_python/).
- `notebooks/Data/movie_metadata.csv`: IMDb movie metadata, from [Kaggle](https://www.kaggle.com/karrrimba/movie-metadatacsv).
- `notebooks/Data/insurance.csv`: US medical insurance costs, from [Kaggle](https://www.kaggle.com/mirichoi0218/insurance).

## Further resources (free)

- [The Python Tutorial](https://docs.python.org/3/tutorial/), the official introduction to the language.
- [Scientific Python Lectures](https://lectures.scientific-python.org/): NumPy, Matplotlib, SciPy and more, for scientists and engineers.
- [NumPy: the absolute basics for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html) and the Matplotlib [quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html).
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) by Jake VanderPlas, including pandas and scikit-learn.

## Acknowledgements

Notebooks 00a and 00b are inspired by Mark Bakker's [Exploratory Computing with Python](http://mbakker7.github.io/exploratory_computing_with_python/) (TU Delft). Notebook 00c is adapted from an article by [Jeff Knupp](https://hackernoon.com/improve-your-python-python-classes-and-object-oriented-programming-d09ff461168d). In notebook 02b, the test function, the plotting code and the animation class are adapted from Louis Tiao's notebook [Visualizing and animating optimization algorithms with Matplotlib](https://github.com/ltiao/notebooks/blob/master/visualizing-and-animating-optimization-algorithms-with-matplotlib.ipynb) (MIT License, reproduced in the notebook).

## Licence

The code in this repository is released under the GNU General Public License v3.0 (see `LICENSE`). Datasets remain subject to the terms of their original sources.
