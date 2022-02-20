from typing import Dict
import plotly.express as px
import pandas as pd


def read_results() -> Dict[int, pd.DataFrame]:
    return dict(tuple(pd.read_csv("results/results.csv").groupby('density')))


def main():
    for density, data in read_results().items():
        fig = px.line(data,
                      x="vertex_count",
                      y="time",
                      color="algorithm",
                      title=f"Density: {density}")
        fig.update_layout(xaxis_title="Vertex count",
                          yaxis_title="Execution time (seconds)",
                          font=dict(
                              family="Courier New, monospace",
                              size=16,
                              color="RebeccaPurple"
                          ))
        fig.write_image(f'results/images/density_{density}.png')


if __name__ == "__main__":
    main()
