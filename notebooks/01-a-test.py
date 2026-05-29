# %% [markdown]
# # Um teste simples!
#
# Quem sabe faz ao vivo.

# %%
import os
import pandas as pd
from pathlib import Path

project_root_env = os.getenv("PROJECT_ROOT")
if not project_root_env:
    raise RuntimeError(
        "PROJECT_ROOT environment variable must be set before running this notebook."
    )
project_root = Path(project_root_env)

# %% [markdown]
# Verificando se a variável de ambiente está correta:

# %%
print(f"Project root is set to: {project_root}")

# %% [markdown]
# Lendo os dados do problema que vai me dar uma medalha Fields:

# %%
data_path = project_root / "data" / "dataset.csv"

dataset_df = pd.read_csv(data_path, header=None, names=["x", "y"])

dataset_df

# %%
dataset_df.plot.scatter(x="x", y="y", title="Scatter plot of x vs y")
