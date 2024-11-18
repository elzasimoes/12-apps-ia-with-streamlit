import numpy as np
from matplotlib import pyplot as plt

from application_pages.benchmarking_temporal_series import plot_forecasts


def test_plot_actual_and_forecasted_data():
    actual = np.array([1, 2, 3, 4, 5])
    forecasts = [np.array([5, 6, 7]), np.array([4, 5, 6])]
    titles = ['Forecast 1', 'Forecast 2']

    plot = plot_forecasts(actual, forecasts, titles)

    assert plot is not None
    assert isinstance(plot, plt.__class__)
    assert plt.gca().get_title() == 'Benchmark de Séries Temporais'
    legend_labels = [label.get_text() for label in plt.gca().get_legend().get_texts()]
    assert 'Dados Atuais' in legend_labels[0]
    assert 'Forecast 1' in legend_labels[1]
    assert 'Forecast 2' in legend_labels[2]
    assert plt.gca().get_xgridlines() != []
    assert plt.gca().get_ygridlines() != []


# Handling empty actual data without errors
def test_handle_empty_actual_data():
    actual = np.array([])
    forecasts = [np.array([5, 6, 7]), np.array([4, 5, 6])]
    titles = ['Forecast 1', 'Forecast 2']

    plot = plot_forecasts(actual, forecasts, titles)

    assert plot is not None
    assert isinstance(plot, plt.__class__)
