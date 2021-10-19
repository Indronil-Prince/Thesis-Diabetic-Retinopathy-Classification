import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import cm
import plotly.express as px


def plot_using_plt(x, y, z, colors): 
    fig, ax = plt.subplots(figsize=(16,16))
    ax = plt.axes(projection="3d")

    ax.scatter3D(x, y, z, zdir=x, c=colors, cmap=cm.Set1);
    plt.show()


def plot_using_plotly(x, y, z, colors):
    fig = px.scatter_3d(x, y, z, color=colors)
    fig.update_traces(marker=dict(size=2,
                                  line=dict(width=2,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))
    fig.show()


