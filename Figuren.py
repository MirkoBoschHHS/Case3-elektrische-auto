import plotly.figure_factory as ff


def histogram(laadpaal_data):
    fig = ff.create_distplot([laadpaal_data['ChargeTime']],
                             group_labels=['Laadtijd'],
                             bin_size=0.25,  # elke bin komt overeen met 15 minuten
                             show_rug=False,
                             curve_type='kde',
                             histnorm='probability density')

    annotation_mean = {'xref': 'paper',
                       'yref': 'paper',
                       'x': 0.8,
                       'y': 0.8,
                       'showarrow': False,
                       'text': '<b>Gemiddelde: ' + str(round(laadpaal_data.ChargeTime.mean(), 2)) + ' uur</b>',
                       'font': {'size': 15, 'color': 'black'}}

    annotation_median = {'xref': 'paper',
                         'yref': 'paper',
                         'x': 0.8,
                         'y': 0.7,
                         'showarrow': False,
                         'text': '<b>Mediaan: ' + str(round(laadpaal_data.ChargeTime.median(), 2)) + ' uur</b>',
                         'font': {'size': 15, 'color': 'black'}}

    fig.update_layout({'annotations': [annotation_mean, annotation_median],
                       'title': "Histogram laadtijd elektrische auto's met benadering kansdichtheidsfunctie",
                       'xaxis': {'range': [0, 8]}})

    fig.update_xaxes(title_text='Laadtijd in uren')
    fig.update_yaxes(title_text='Dichtheid')

    return fig