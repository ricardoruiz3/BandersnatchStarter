import altair as alt
from altair import Chart
from pandas import DataFrame


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    ''' Generates a scatter plot from the DataFrame
    Using x and y columns for axes and colors points by target column.
    Raises ValueError if columns are missing or DataFrame is empty.'''

    # Basic validation
    for col in [x, y, target]:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' not found in DataFrame")

    if df.empty:
        raise ValueError("DataFrame is empty")

    # Body of the function
    chart = alt.Chart(df).mark_circle().encode(
        x=x,
        y=y,
        color=alt.Color(target, type='nominal'),
        tooltip=[x, y, target]
    ).properties(
        width=600,
        height=400,
        background='white',
        padding=5,
        title=f"{y} vs {x} colored by {target}"
    )

    return chart
