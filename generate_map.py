#!/usr/bin/env python3
"""
Spotswood Historic Homes Map Generator
Usage: python generate_map.py
Output: index.html
"""

import folium
from folium.plugins import MarkerCluster, Fullscreen

# Map configuration
MAP_CENTER = [40.391565230621474, -74.3903805208576]  # Spotswood, NJ
ZOOM_START = 15

# Property data structure
# Format: [latitude, longitude, name, year, era, description, image_filename, icon_type, marker_color]
properties = [
    # 1700s (Orange)
    [40.391119167853574, -74.38927290757084, "St. Peter's Church", "1899", "1700s",
     "Although there has been record of a chruch here since the 1740's, the current structure was rebuilt in the 1800's after a fire.",
     "stpeters.jpeg", "church", "orange"],

    [40.37404720357879, -74.41629291824485, "Ten Eyks Forge", "1700s", "1700s",
     "One of the earliest forges in the county, established before the Revolution. Some stonework is still visible",
     "oldforge.jpeg", "industry", "orange"],

    # 1800s (Red)
    [40.36855838554895, -74.39871061556082, "37 S. Shore Blvd", "1893", "1800s",
     "This historic home sits along the South River in Old Bridge Township, built in the late 1800s.",
     "37sshoreblvd.jpeg", "home", "red"],

    [40.38533844328248, -74.39040014355436, "26 Lakeview Dr", "1869", "1800s",
     "A well-preserved Victorian-era home located near the historic village center.",
     "26lakeviewdr.jpeg", "home", "red"],

    [40.35452738643187, -74.4418346184206, "15 Stockton Ave", "1835", "1800s",
     "One of the oldest homes in the area, featuring period architecture and original details.",
     "15stocktonave.jpeg", "home", "red"],

    [40.35820667651387, -74.43853956088016, "Helmetta Snuff Mill", "1880", "1800s",
     "Historic industrial site that produced snuff tobacco products in the late 1800s.",
     "helmettasnuffmill.jpeg", "industry", "red"],

    [40.388896968636886, -74.39068414004636, "Spotswood Reformed Church", "1821", "1800s",
     "Historic church building that has served the community for over 200 years.",
     "spotswoodreformedchurch.jpeg", "church", "red"],

    [40.38833992113134, -74.39151927267553, "Immaculate Convent", "Circa 1875", "1800s",
     "Historic convent building with Victorian-era architecture.",
     "immaculateconvent.jpeg", "church", "red"],

    [40.3894699695387, -74.39111314003768, "505 Main Street.", "1872", "1800s",
     "Historic commercial building in the heart of downtown Spotswood.",
     "505mainst.jpeg", "church", "red"],

    # 1900-1909 (Green)
    [40.39157370636695, -74.38792925268113, "300 Manalapan Ave", "1905", "1900-1909",
     "Early 20th century home in the residential section of town.",
     "300manalapanave.jpeg", "home", "green"],

    [40.39122326612788, -74.39006861818464, "222 Devoe Ave", "1900", "1900-1909",
     "Turn of the century home with classic architectural details.",
     "222devoeave.jpeg", "home", "green"],

    [40.39206844360736, -74.39129327711568, "92 Main St", "1907", "1900-1909",
     "Historic Main Street property from the early 1900s.",
     "92mainst.jpeg", "home", "green"],

    [40.39072382637394, -74.39020961003894, "421 Main St", "1905", "1900-1909",
     "Well-maintained early 20th century residence.",
     "421mainst.jpeg", "home", "green"],

    [40.39124791125989, -74.39238190941825, "22 Avenue C", "1906", "1900-1909",
     "Charming home from 1906 with period features.",
     "22avenuec.jpeg", "home", "green"],

    [40.390618564001936, -74.39228616271183, "33 Stockton Ave.", "1900", "1900-1909",
     "Historic turn-of-the-century residence.",
     "33stocktonave.jpeg", "home", "green"],

    [40.39222681887387, -74.38947457373988, "219 Manalapan Rd.", "1955", "1900-1909",
     "Mid-century home in established neighborhood.",
     "219manalapanrd.jpeg", "home", "green"],

    [40.39189913110842, -74.38905513817846, "191 Manalapan Rd.", "1905", "1900-1909",
     "Early 1900s residence with original character.",
     "191manalapanrd.jpeg", "home", "green"],

    [40.39299729885928, -74.39267009629838, "57 Lettau Drive", "1905", "1900-1909",
     "Historic home from the early 20th century.",
     "57lettaudrive.jpeg", "home", "green"],

    [40.39187447598622, -74.39152761554175, "24 Main Street.", "1905", "1900-1909",
     "Downtown historic residence from 1905.",
     "24mainst.jpeg", "home", "green"],

    [40.390088431242606, -74.38992659561226, "452 Main Street.", "1905", "1900-1909",
     "Historic Main Street property.",
     "452mainst.jpeg", "home", "green"],

    # 1910-1919 (Blue)
    [40.392527063739154, -74.39352582913688, "45 Lake Ave.", "1910", "1910-1919",
     "Early 1910s home near the lake.",
     "45lakeave.jpeg", "home", "blue"],

    [40.39283036128869, -74.39327835002088, "15 Mundy Ave.", "1910", "1910-1919",
     "Historic residence from 1910.",
     "15mundyave.jpeg", "home", "blue"],

    [40.39058747884896, -74.3904990851639, "321 Main St.", "1918", "1910-1919",
     "Late 1910s Main Street home.",
     "321mainst.jpeg", "home", "blue"],

    # 1920-1929 (Black)
    [40.39319200372395, -74.39384332641732, "116 Mundy Ave", "1926", "1920-1929",
     "1920s era residence.",
     "116mundyave.jpeg", "home", "black"],

    [40.39371229119035, -74.39397245897007, "114 Fernhead", "1926", "1920-1929",
     "Late 1920s home with period details.",
     "114fernhead.jpeg", "home", "black"],

    [40.391405714137255, -74.3898738827062, "79 Devoe Ave", "1929", "1920-1929",
     "Late 1920s residence.",
     "79devoeave.jpeg", "home", "black"],

    [40.38967838866699, -74.39008191003857, "490 Main Street", "1920", "1920-1929",
     "Early 1920s Main Street property.",
     "490mainst.jpeg", "home", "black"],

    [40.39197244134906, -74.39246582185026, "50 South Street.", "1928", "1920-1929",
     "Late 1920s home.",
     "50southst.jpeg", "home", "black"],

    [40.391892440098976, -74.39233669375854, "46 South Street.", "1928", "1920-1929",
     "1928 residence on South Street.",
     "46southst.jpeg", "home", "black"],

    [40.39181243884889, -74.39220756566682, "44 South Street.", "1928", "1920-1929",
     "Historic 1920s home.",
     "44southst.jpeg", "home", "black"],

    # 1930-1939 (Pink)
    [40.393086396390955, -74.3934629565627, "29 Mundy Ave.", "1938", "1930-1939",
     "Late 1930s residence.",
     "29mundyave.jpeg", "home", "pink"],

    [40.38995803615483, -74.39000559084225, "448 Main Street.", "1930", "1930-1939",
     "Early 1930s Main Street home.",
     "448mainst.jpeg", "home", "pink"],

    # 1940-1949 (Purple)
    [40.38981067861889, -74.38999559003859, "482 Main Street", "Circa 1945", "1940-1949",
     "Mid-1940s property.",
     "482mainst.jpeg", "home", "purple"],

    [40.39229147400177, -74.39134860281721, "186 Main Street.", "1945", "1940-1949",
     "Post-war 1940s home.",
     "186mainst.jpeg", "home", "purple"],

    # 1950-1959 (Darkred)
    [40.39296630385527, -74.39328500813735, "23 Mundy Ave.", "1955", "1950-1959",
     "Mid-1950s residence.",
     "23mundyave.jpeg", "home", "darkred"],

    [40.39144859878774, -74.3900403637838, "87 Devoe Ave.", "1954", "1950-1959",
     "1950s era home.",
     "87devoeave.jpeg", "home", "darkred"],

    [40.391578600138845, -74.39021616372537, "93 Devoe Ave.", "1953", "1950-1959",
     "Early 1950s residence.",
     "93devoeave.jpeg", "home", "darkred"],

    [40.39170860148995, -74.39039196366693, "97 Devoe Ave.", "1955", "1950-1959",
     "Mid-1950s home on Devoe Avenue.",
     "97devoeave.jpeg", "home", "darkred"],
]

def create_marker_popup(name, year, era, description, image_filename):
    """Create HTML popup content for a marker"""
    popup_html = f"""
    <style>
        .popup-content {{
            font-family: Arial;
            font-size: 10px;
            line-height: 1.5;
            width: 250px; /* Default width for larger screens */
        }}
        .popup-content h4 {{
            margin: 8px 0;
        }}
        .popup-content p {{
            margin: 0 0 4px 0;
        }}
        @media (max-width: 600px) {{
            .popup-content {{
                width: 90vw; /* Make wider on small screens */
                font-size: 14px; /* Increase font size for mobile */
            }}
             .popup-content img {{
                width: 100%; /* Make image take full width on small screens */
                max-width: none;
             }}
        }}
    </style>
    <div class="popup-content">
        <h4>{name} ({year})</h4>
        <p><b>Era:</b> {era}</p>
        <p>{description}</p>
        <div style="text-align:center;margin:8px 0;"><img src="https://raw.githubusercontent.com/MikeHistory/Spotswood-Historic-Homes/refs/heads/main/images/{image_filename}" style="width: 100%; max-width: 200px; height: auto;"></div>
    </div>
    """
    return popup_html

def create_map():
    """Generate the complete map with all markers"""

    # Create base map
    m = folium.Map(
        location=MAP_CENTER,
        zoom_start=ZOOM_START,
        tiles='OpenStreetMap',
        prefer_canvas=False
    )

    # Add Google Satellite layer
    folium.TileLayer(
        tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
        attr='Google Satellite',
        name='Google Satellite',
        overlay=True,
        control=True,
        max_zoom=22
    ).add_to(m)

    # Add fullscreen button
    Fullscreen(position='topleft').add_to(m)

    # Organize markers by era for marker clustering
    era_clusters = {
        '1700s': {'color': 'orange', 'cluster': MarkerCluster(name='1700s', show=True,
                   options={'showCoverageOnHover': False, 'spiderfyOnMaxZoom': True, 'disableClusteringAtZoom': 16})},
        '1800s': {'color': 'red', 'cluster': MarkerCluster(name='1800s', show=True,
                   options={'showCoverageOnHover': False, 'spiderfyOnMaxZoom': True, 'disableClusteringAtZoom': 16})},
        '1900-1909': {'color': 'green', 'cluster': MarkerCluster(name='1900-1909', show=True,
                   options={'showCoverageOnHover': False, 'spiderfyOnMaxZoom': True, 'disableClusteringAtZoom': 16})},
        '1910-1919': {'color': 'blue', 'cluster': MarkerCluster(name='1910-1919', show=True,
                   options={'showCoverageOnHover': False, 'spiderfyOnMaxZoom': True, 'disableClusteringAtZoom': 16})},
        '1920-1929': {'color': 'black', 'cluster': MarkerCluster(name='1920-1929', show=True,
                   options={'showCoverageOnHover': False, 'spiderfyOnMaxZoom': True, 'disableClusteringAtZoom': 16})},
        '1930-1939': {'color': 'pink', 'cluster': MarkerCluster(name='1930-1939', show=True,
                   options={'showCoverageOnHover': False, 'spiderfyOnMaxZoom': True, 'disableClusteringAtZoom': 16})},
        '1940-1949': {'color': 'purple', 'cluster': MarkerCluster(name='1940-1949', show=True,
                   options={'showCoverageOnHover': False, 'spiderfyOnMaxZoom': True, 'disableClusteringAtZoom': 16})},
        '1950-1959': {'color': 'darkred', 'cluster': MarkerCluster(name='1950-1959', show=True,
                   options={'showCoverageOnHover': False, 'spiderfyOnMaxZoom': True, 'disableClusteringAtZoom': 16})},
    }

    # Add markers to their respective clusters
    for prop in properties:
        lat, lon, name, year, era, description, image, icon_type, marker_color = prop

        # Create popup
        popup_html = create_marker_popup(name, year, era, description, image)
        iframe = folium.IFrame(popup_html, width=350, height=250)
        popup = folium.Popup(iframe, max_width=500)

        # Create marker with custom icon
        marker = folium.Marker(
            location=[lat, lon],
            popup=popup,
            icon=folium.Icon(
                color=marker_color,
                icon_color='white',
                icon=icon_type,
                prefix='fa'
            ),
            tooltip=folium.Tooltip(
                year,
                permanent=True,
                direction='top',
                className='year-tooltip',
                offset=(0, -10)
            )
        )

        # Add marker to appropriate cluster
        marker.add_to(era_clusters[era]['cluster'])

    # Add all clusters to map
    for era_data in era_clusters.values():
        era_data['cluster'].add_to(m)

    # Add layer control
    folium.LayerControl(position='bottomright', collapsed=True).add_to(m)

    # Get the HTML and add custom CSS for tooltips and title
    html = m.get_root().render()

    # Add custom CSS for year tooltips and title banner
    custom_css = """
    <style>
        /* Year tooltip styling - discreet and mobile-friendly */
        .year-tooltip {
            background-color: rgba(0, 0, 0, 0.75) !important;
            color: white !important;
            border: none !important;
            border-radius: 4px !important;
            padding: 2px 6px !important;
            font-size: 11px !important;
            font-weight: bold !important;
            font-family: Arial, sans-serif !important;
            box-shadow: 0 1px 3px rgba(0,0,0,0.3) !important;
            white-space: nowrap !important;
        }

        .year-tooltip:before {
            border-top-color: rgba(0, 0, 0, 0.75) !important;
        }

        /* Mobile optimization */
        @media (max-width: 600px) {
            .year-tooltip {
                font-size: 10px !important;
                padding: 2px 5px !important;
            }
        }
    </style>
</head>"""

    title_banner = """
<style>
    .title-banner {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 9999;
        background: blue;
        color: yellow;
        padding: 16px;
        font-family: Arial, sans-serif;
        font-size: 20px;
        font-weight: bold;
        box-shadow: 0 2px 4px rgba(0,0,0,0.3);
        border-bottom: 3px solid #ddd;
        text-align: center; /* Center the text */
    }
    @media (max-width: 600px) {
        .title-banner {
            padding: 10px; /* Reduce padding on smaller screens */
            font-size: 16px; /* Reduce font size on smaller screens */
        }
    }
</style>
<div class="title-banner">
  Spotswood Historic Homes
</div>
</body>"""

    # Replace closing tags with custom elements
    html = html.replace('</head>', custom_css)
    html = html.replace('</body>', title_banner)

    # Fix FontAwesome version for compatibility with Leaflet Awesome Markers
    html = html.replace(
        'fontawesome-free@6.2.0',
        'fontawesome-free@5.15.4'
    )

    return html

if __name__ == '__main__':
    print("Generating Spotswood Historic Homes map...")

    # Generate the map
    map_html = create_map()

    # Save to index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(map_html)

    print(f"✓ Map generated successfully!")
    print(f"✓ Added {len(properties)} historic properties")
    print(f"✓ Output: index.html")
    print(f"\nTo add a new property:")
    print("  1. Add a new entry to the 'properties' list")
    print("  2. Format: [lat, lon, name, year, era, description, image_filename, icon_type, marker_color]")
    print("  3. Icon types: 'home', 'church', 'industry', 'store'")
    print("  4. Run: python generate_map.py")
