import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['overweight'] = ((df['weight'] / (df['height'] / 100)**2) > 25).astype(int)

# 3
df['gluc'] = (df['gluc'] != 1).astype(int)
df['cholesterol'] = (df['cholesterol'] != 1).astype(int)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name="total")
    

    # 7
    facet_grid = sns.catplot(
        data=df_cat,
        x='variable',
        y='total',
        hue='value',
        col="cardio",
        kind="bar",
    )

    facet_grid.figure.subplots_adjust(top=0.85)
    facet_grid.figure.suptitle("Categorical Plot of Health Features", fontsize=14)

    # 8
    fig = facet_grid.figure


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    pressure_mask = df["ap_lo"] <= df["ap_hi"]
    
    short_mask = df["height"] >= df["height"].quantile(0.025) 
    
    tall_mask = df["height"] <= df["height"].quantile(0.975)
    
    low_weight_mask = df["weight"] >= df["weight"].quantile(0.025)
    
    high_weight_mask = df["weight"] <= df["weight"].quantile(0.975)

    df_heat = df[pressure_mask & short_mask & tall_mask & low_weight_mask & high_weight_mask]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(8, 6))

    # 15
    sns.heatmap(corr, annot=True, mask=mask, fmt=".1f", cmap="crest", ax=ax)
    ax.set_title("Correlation Matrix of Medical Data")


    # 16
    fig.savefig('heatmap.png')
    return fig
