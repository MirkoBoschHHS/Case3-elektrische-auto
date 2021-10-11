import plotly.figure_factory as ff
import folium
import streamlit as st


def histogram_laadtijd_elek_auto(laadpaal_data):
    fig = ff.create_distplot([laadpaal_data['ChargeTime']],
                             group_labels=['Laadtijd'],
                             bin_size=0.25,  # elke bin komt overeen met 15 minuten
                             show_rug=False,
                             curve_type='kde',
                             histnorm='probability density',)

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
    fig.update_layout(
        autosize=False,
        width=800,
        height=550, )

    return fig



#---------------------------------------------------


def color_producer(type):
    if type == 'Ecotap':
        return 'Black'
    if type == 'Allego BV':
        return 'dimgray'
    if type == '(Unknown Operator)':
        return 'silver'
    if type == 'Shell UK Oil Products Limited':
        return 'rosybrown'
    if type == 'Ionity':
        return 'brown'
    if type == 'EV-Box':
        return 'darkred'
    if type == 'Tesla Motors (Worldwide)':
        return 'salmon'
    if type == 'Alfen':
        return 'orangered'
    if type == 'nan':
        return 'sienna'
    if type == 'Vattenfall InCharge':
        return 'saddlebrown'
    if type == 'Greenflux':
        return 'peru'
    if type == 'Last Mile Solutions':
        return 'darkorange'
    if type == 'Eneco':
        return 'burlywood'
    if type == '(Private Residence/Individual)':
        return 'moccasin'
    if type == 'Nuon':
        return 'darkgoldenrod'
    if type == 'FastNed':
        return 'gold'
    if type == 'Blue Marble Charging':
        return 'khaki'
    if type == 'Park & Charge (D)':
        return 'olive'
    if type == 'Incharge':
        return 'yellow'
    if type == 'Park & Charge (CH)':
        return 'yellowgreen'
    if type == 'Lidl':
        return 'darkolivergreen'
    if type == 'The New Motion (NL)':
        return 'chartreuse'
    if type == '(Business Owner at Location)':
        return 'darkseagreen'
    if type == 'TOTAL Nl PlugToDrive':
        return 'lightgreen'
    if type == 'EV-Point':
        return 'lime'
    if type == 'EVnetNL':
        return 'springgreen'
    if type == 'e-Laad':
        return 'aquamarine'
    if type == 'Blue Corner (Belgium)':
        return 'turquoise'
    if type == 'The New Motion (BE)':
        return 'lightseagreen'
    if type == 'ThePluginCompany (Belgium)':
        return 'darkslategray'
    if type == 'MisterGreen, The Fast Charger Network':
        return 'aqua'
    if type == 'eNovates':
        return 'cadetblue'
    if type == 'POD Point (UK)':
        return 'deepskyblue'
    if type == 'Nomadpower':
        return 'dodgerblue'
    if type == 'ChargePoint (Coulomb Technologies)':
        return 'cornflowerblue'
    if type == 'Essent (NL)':
        return 'navy'
    if type == 'FLOW Charging':
        return 'slateblue'
    if type == 'Stadtwerke Clausthal-Zellerfeld':
        return 'indigo'
    if type == 'RWE Mobility/Essent':
        return 'darkviolet'

def add_categorical_legend(folium_map, title, colors, labels):
    if len(colors) != len(labels):
        raise ValueError("colors and labels must have the same length.")

    color_by_label = dict(zip(labels, colors))

    legend_categories = ""
    for label, color in color_by_label.items():
        legend_categories += f"<li><span style='background:{color}'></span>{label}</li>"

    legend_html = f"""
    <div id='maplegend' class='maplegend'>
      <div class='legend-title'>{title}</div>
      <div class='legend-scale'>
        <ul class='legend-labels'>
        {legend_categories}
        </ul>
      </div>
    </div>
    """
    script = f"""
        <script type="text/javascript">
        var oneTimeExecution = (function() {{
                    var executed = false;
                    return function() {{
                        if (!executed) {{
                             var checkExist = setInterval(function() {{
                                       if ((document.getElementsByClassName('leaflet-top leaflet-right').length) || (!executed)) {{
                                          document.getElementsByClassName('leaflet-top leaflet-right')[0].style.display = "flex"
                                          document.getElementsByClassName('leaflet-top leaflet-right')[0].style.flexDirection = "column"
                                          document.getElementsByClassName('leaflet-top leaflet-right')[0].innerHTML += `{legend_html}`;
                                          clearInterval(checkExist);
                                          executed = true;
                                       }}
                                    }}, 100);
                        }}
                    }};
                }})();
        oneTimeExecution()
        </script>
      """

    css = """

    <style type='text/css'>
      .maplegend {
        z-index:9999;
        float:right;
        background-color: rgba(255, 255, 255, 1);
        border-radius: 5px;
        border: 2px solid #bbb;
        padding: 10px;
        font-size:12px;
        positon: relative;
      }
      .maplegend .legend-title {
        text-align: left;
        margin-bottom: 5px;
        font-weight: bold;
        font-size: 90%;
        }
      .maplegend .legend-scale ul {
        margin: 0;
        margin-bottom: 5px;
        padding: 0;
        float: left;
        list-style: none;
        }
      .maplegend .legend-scale ul li {
        font-size: 80%;
        list-style: none;
        margin-left: 0;
        line-height: 18px;
        margin-bottom: 2px;
        }
      .maplegend ul.legend-labels li span {
        display: block;
        float: left;
        height: 16px;
        width: 30px;
        margin-right: 5px;
        margin-left: 0;
        border: 0px solid #ccc;
        }
      .maplegend .legend-source {
        font-size: 80%;
        color: #777;
        clear: both;
        }
      .maplegend a {
        color: #777;
        }
    </style>
    """

    folium_map.get_root().header.add_child(folium.Element(script + css))

    return folium_map

def map(response_dataframe, max_results):
    sw = response_dataframe[['AddressInfo.Latitude', 'AddressInfo.Longitude']].quantile(0.05).values.tolist()
    ne = response_dataframe[['AddressInfo.Latitude', 'AddressInfo.Longitude']].quantile(0.95).values.tolist()

    m = folium.Map()#location=[average_lat, average_lon], zoom_start=zoom)

    # Expres gebruik gemaakt van Circle
    # nu worden die circles niet enorm groot bij het uitzoemen
    # Als je inzoom zie ook dat ze verschillende radius hebben

    bar = st.progress(0)
    i = 0

    for row in response_dataframe.iterrows():
        row_values = row[1]
        location = [row_values['AddressInfo.Latitude'], row_values['AddressInfo.Longitude']]
        marker_location = row_values['AddressInfo.Town']
        marker = folium.Circle(location=location,
                               fill=True,
                               fill_color=color_producer(row_values['OperatorInfo.Title']),
                               color=color_producer(row_values['OperatorInfo.Title']),
                               popup='<strong>' + str(row_values['OperatorInfo.Title']) + '</strong>',
                               )
        marker.add_to(m)

        i += 1
        value = int(i / ((max_results / 100)))
        if(value > 98):
            value = 98
        bar.progress(value)

    import geocoder
    g = geocoder.ip('me').latlng
    # st.write(g.latlng)

    location = g
    marker_location = row_values['AddressInfo.Town']
    marker = folium.Marker(location=location,
                           popup='<strong>' + str("Your location based on IP") + '</strong>',
                           )
    marker.add_to(m)

    m.fit_bounds([sw, ne])
    return m ,bar





#---------------------------------------------------