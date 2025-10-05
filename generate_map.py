"""Generate the Spotswood Historic Homes map with a mobile-first Leaflet UI."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

OUTPUT_FILE = Path("index.html")

ERA_STYLES: Dict[str, Dict[str, str]] = {
    "1700s": {"color": "orange", "display": "1700s"},
    "1800s": {"color": "red", "display": "1800s"},
    "1900-1919": {"color": "green", "display": "1900-1919"},
    "1920-1939": {"color": "blue", "display": "1920-1939"},
}

MARKERS: List[Dict[str, str]] = [
    {
        "lat": 40.391298301514595,
        "lon": -74.3891452214229,
        "icon": "church",
        "marker_color": "orange",
        "title": "St. Peter's Church (1899)",
        "era": "1700s",
        "description": "Although there has been record of a chruch here since the 1740's, the current structure was rebuilt in the 1800's after a fire.",
        "image": "https://raw.githubusercontent.com/MikeHistory/Spotswood-Historic-Homes/refs/heads/main/images/stpeters.jpeg",
    },
    {
        "lat": 40.37404720357879,
        "lon": -74.41629291824485,
        "icon": "industry",
        "marker_color": "orange",
        "title": "Ten Eyks Forge (1700s)",
        "era": "1700s",
        "description": "One of the earliest forges in the county, established before the Revolution. Some stonework is still visible",
        "image": "https://raw.githubusercontent.com/MikeHistory/Spotswood-Historic-Homes/refs/heads/main/images/oldforge.jpeg",
    },
    {
        "lat": 40.37576344900822,
        "lon": -74.41134856125089,
        "icon": "home",
        "marker_color": "red",
        "title": "37 S. Shore Blvd (1893)",
        "era": "1800s",
        "description": "Predates Physical Culture City",
        "image": "https://raw.githubusercontent.com/MikeHistory/Spotswood-Historic-Homes/refs/heads/main/images/37Shore.jpeg",
    },
    {
        "lat": 40.38533844328248,
        "lon": -74.39040014355436,
        "icon": "home",
        "marker_color": "red",
        "title": "26 Lakeview Dr (1869)",
        "era": "1800s",
        "description": "Very old pine trees and water facing structures on property.",
        "image": "https://raw.githubusercontent.com/MikeHistory/Spotswood-Historic-Homes/refs/heads/main/images/26lakeview.jpeg",
    },
    {
        "lat": 40.35452738643187,
        "lon": -74.4418346184206,
        "icon": "home",
        "marker_color": "red",
        "title": "15 Stockton Ave (1835)",
        "era": "1800s",
        "description": "Marryott House",
        "image": "https://github.com/MikeHistory/Spotswood-Historic-Homes/blob/main/images/MarryottHouse.jpeg?raw=true",
    },
    {
        "lat": 40.37775887887239,
        "lon": -74.42493778094678,
        "icon": "industry",
        "marker_color": "red",
        "title": "Helmetta Snuff Mill (1880)",
        "era": "1800s",
        "description": "Now the 'Lofts at Helmetta' Condominiums",
        "image": "https://raw.githubusercontent.com/MikeHistory/Spotswood-Historic-Homes/refs/heads/main/images/Snuffmill.jpeg",
    },
    {
        "lat": 40.385888760121915,
        "lon": -74.40217742646804,
        "icon": "home",
        "marker_color": "green",
        "title": "300 Manalapan Ave (1905)",
        "era": "1900-1919",
        "description": "Constructed during Physical Culture era.",
        "image": "https://raw.githubusercontent.com/MikeHistory/Spotswood-Historic-Homes/refs/heads/main/images/300Manalapan.jpeg",
    },
    {
        "lat": 40.385249232439946,
        "lon": -74.38854921936806,
        "icon": "home",
        "marker_color": "green",
        "title": "222 Devoe Ave (1900)",
        "era": "1900-1919",
        "description": "Devoe Mansion?",
        "image": "https://raw.githubusercontent.com/MikeHistory/Spotswood-Historic-Homes/refs/heads/main/images/222devoe.jpeg",
    },
    {
        "lat": 40.3741229106213,
        "lon": -74.42815593006208,
        "icon": "home",
        "marker_color": "green",
        "title": "92 Main St (1907)",
        "era": "1900-1919",
        "description": "Main Street, Helmetta",
        "image": "https://raw.githubusercontent.com/MikeHistory/Spotswood-Historic-Homes/refs/heads/main/images/92mainstreet.jpeg",
    },
    {
        "lat": 40.39402914768797,
        "lon": -74.38645461845664,
        "icon": "home",
        "marker_color": "green",
        "title": "421 Main St (1905)",
        "era": "1900-1919",
        "description": "Three years before Spotswood became its own boro.",
        "image": "https://raw.githubusercontent.com/MikeHistory/Spotswood-Historic-Homes/refs/heads/main/images/421main.jpeg",
    },
    {
        "lat": 40.37959501397669,
        "lon": -74.40771826802995,
        "icon": "home",
        "marker_color": "green",
        "title": "22 Avenue C (1906)",
        "era": "1900-1919",
        "description": "Constructed during Physical Culture City era.",
        "image": "https://raw.githubusercontent.com/MikeHistory/Spotswood-Historic-Homes/refs/heads/main/images/22AveC.jpeg",
    },
    {
        "lat": 40.35616867884141,
        "lon": -74.44309178323445,
        "icon": "home",
        "marker_color": "green",
        "title": "33 Stockton Ave. (1900)",
        "era": "1900-1919",
        "description": "Jamesburg Turn of 20th Century.",
        "image": "https://raw.githubusercontent.com/MikeHistory/Spotswood-Historic-Homes/refs/heads/main/images/33stockton.jpeg",
    },
    {
        "lat": 40.38238830813217,
        "lon": -74.42103717710137,
        "icon": "home",
        "marker_color": "green",
        "title": "45 Lake Ave. (1910)",
        "era": "1900-1919",
        "description": "Tucked Away Behind Pines",
        "image": "https://raw.githubusercontent.com/MikeHistory/Spotswood-Historic-Homes/refs/heads/main/images/45lake.jpeg",
    },
    {
        "lat": 40.3891810684233,
        "lon": -74.38709707974064,
        "icon": "home",
        "marker_color": "green",
        "title": "15 Mundy Ave. (1910)",
        "era": "1900-1919",
        "description": "Across From Playground",
        "image": "https://raw.githubusercontent.com/MikeHistory/Spotswood-Historic-Homes/refs/heads/main/images/15mundy.jpeg",
    },
    {
        "lat": 40.38664472038314,
        "lon": -74.39896231749604,
        "icon": "home",
        "marker_color": "green",
        "title": "219 Manalapan Rd. (1905)",
        "era": "1900-1919",
        "description": "Blue House Old Timey Shutters",
        "image": "https://raw.githubusercontent.com/MikeHistory/Spotswood-Historic-Homes/refs/heads/main/images/219manalapan.jpeg",
    },
    {
        "lat": 40.39693198846547,
        "lon": -74.38427441933148,
        "icon": "home",
        "marker_color": "green",
        "title": "321 Main St. (1918)",
        "era": "1900-1919",
        "description": "Past Summerhill On Right",
        "image": "https://raw.githubusercontent.com/MikeHistory/Spotswood-Historic-Homes/refs/heads/main/images/321main.jpeg",
    },
    {
        "lat": 40.38718583361005,
        "lon": -74.39795347164319,
        "icon": "home",
        "marker_color": "green",
        "title": "191 Manalapan Rd. (1905)",
        "era": "1900-1919",
        "description": "At the intersection of River Street, itself a very old street.",
        "image": "https://raw.githubusercontent.com/MikeHistory/Spotswood-Historic-Homes/refs/heads/main/images/191manalapan.jpeg",
    },
    {
        "lat": 40.38408589764912,
        "lon": -74.39010246063746,
        "icon": "home",
        "marker_color": "green",
        "title": "57 Lettau Drive (1905)",
        "era": "1900-1919",
        "description": "Structure seems to hint at possible earlier origins.",
        "image": "https://raw.githubusercontent.com/MikeHistory/Spotswood-Historic-Homes/refs/heads/main/images/57lettau.jpeg",
    },
    {
        "lat": 40.38953733659066,
        "lon": -74.38243613495742,
        "icon": "home",
        "marker_color": "blue",
        "title": "116 Mundy Ave (1926)",
        "era": "1920-1939",
        "description": "Possible older mill structures on property.",
        "image": "https://raw.githubusercontent.com/MikeHistory/Spotswood-Historic-Homes/refs/heads/main/images/116mundy.jpeg",
    },
    {
        "lat": 40.38573789455148,
        "lon": -74.3834434656437,
        "icon": "home",
        "marker_color": "blue",
        "title": "114 Fernhead (1926)",
        "era": "1920-1939",
        "description": "Mary's House",
        "image": "https://raw.githubusercontent.com/MikeHistory/Spotswood-Historic-Homes/refs/heads/main/images/114fernhead.jpeg",
    },
    {
        "lat": 40.38973206524793,
        "lon": -74.38843207598228,
        "icon": "home",
        "marker_color": "blue",
        "title": "79 Devoe Ave (1929)",
        "era": "1920-1939",
        "description": "Long, old stone lined driveway in front.",
        "image": "https://raw.githubusercontent.com/MikeHistory/Spotswood-Historic-Homes/refs/heads/main/images/79devoe.jpeg",
    },
]


def build_html() -> str:
    markers_json = json.dumps(MARKERS, ensure_ascii=False, indent=2)
    era_styles_json = json.dumps(ERA_STYLES, ensure_ascii=False, indent=2)
    return f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"utf-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1, maximum-scale=1\">
    <title>Spotswood Historic Homes</title>
    <link rel=\"stylesheet\" href=\"https://cdn.jsdelivr.net/npm/leaflet@1.9.4/dist/leaflet.css\">\n    <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.4/leaflet.awesome-markers.css\">\n    <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.5.3/MarkerCluster.css\">\n    <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.5.3/MarkerCluster.Default.css\">\n    <link rel=\"stylesheet\" href=\"https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.5.2/css/all.min.css\">\n    <style>
        :root {{
            color-scheme: light;
        }}
        html, body {{
            height: 100%;
            margin: 0;
            font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif;
            background: #f4f6f8;
            color: #1f2933;
        }}
        #map {{
            position: absolute;
            inset: 0;
        }}
        .map-header {{
            position: fixed;
            top: 12px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 1100;
            background: rgba(255, 255, 255, 0.96);
            backdrop-filter: blur(6px);
            padding: 10px 18px;
            border-radius: 16px;
            box-shadow: 0 12px 32px rgba(15, 23, 42, 0.18);
            font-size: 1.05rem;
            font-weight: 600;
            letter-spacing: 0.02em;
            text-align: center;
        }}
        .leaflet-container {{
            font-size: 15px;
        }}
        .leaflet-control-attribution {{
            font-size: 11px;
            background: rgba(255, 255, 255, 0.85);
            border-radius: 10px 0 0 0;
            padding: 4px 8px;
        }}
        .leaflet-control-layers {{
            background: rgba(255, 255, 255, 0.95);
            border-radius: 14px;
            box-shadow: 0 14px 30px rgba(15, 23, 42, 0.2);
            border: 1px solid rgba(15, 23, 42, 0.1);
            padding: 6px 8px;
        }}
        .leaflet-control-layers-expanded label {{
            margin: 6px 0;
            display: flex;
            gap: 8px;
            align-items: center;
            font-weight: 500;
            color: #1f2933;
        }}
        .leaflet-popup-content-wrapper {{
            border-radius: 18px;
            box-shadow: 0 20px 40px rgba(15, 23, 42, 0.28);
            padding: 0;
            overflow: hidden;
        }}
        .leaflet-popup-content {{
            margin: 0;
            padding: 0;
            width: auto !important;
            overflow: hidden;
        }}
        .popup-card {{
            padding: 18px 20px 20px;
            max-width: 280px;
        }}
        .popup-header {{
            display: flex;
            flex-direction: column;
            gap: 4px;
        }}
        .popup-header h3 {{
            margin: 0;
            font-size: 1.1rem;
            line-height: 1.3;
        }}
        .popup-era {{
            margin: 0;
            font-size: 0.78rem;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: #64748b;
        }}
        .popup-description {{
            margin: 14px 0 16px;
            line-height: 1.55;
            color: #374151;
        }}
        .popup-image img {{
            width: 100%;
            height: auto;
            display: block;
            border-radius: 14px;
            box-shadow: 0 12px 24px rgba(15, 23, 42, 0.22);
        }}
        @media (max-width: 600px) {{
            .map-header {{
                width: calc(100vw - 32px);
                padding: 10px 16px;
                font-size: 1rem;
            }}
            .leaflet-container {{
                font-size: 14px;
            }}
            .leaflet-control-layers {{
                font-size: 0.88rem;
                max-width: 220px;
            }}
            .leaflet-popup-content-wrapper {{
                max-width: calc(100vw - 48px);
            }}
            .popup-card {{
                max-width: calc(100vw - 64px);
                padding: 16px 18px 18px;
            }}
        }}
    </style>
</head>
<body>
    <div id=\"map\" role=\"region\" aria-label=\"Spotswood historic homes map\"></div>
    <div class=\"map-header\">Spotswood Historic Homes</div>

    <script src=\"https://cdn.jsdelivr.net/npm/leaflet@1.9.4/dist/leaflet.js\"></script>\n    <script src=\"https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.4/leaflet.awesome-markers.js\"></script>\n    <script src=\"https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.5.3/leaflet.markercluster.js\"></script>\n    <script>
        const markers = {markers_json};
        const eraStyles = {era_styles_json};

        const map = L.map('map', {{ zoomControl: true, preferCanvas: false }});
        const baseLayer = L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
            maxZoom: 19,
            attribution: 'Data © <a href="https://openstreetmap.org">OpenStreetMap</a> contributors'
        }}).addTo(map);

        const clusters = {{}};
        const overlays = {{}};
        Object.entries(eraStyles).forEach(([era, style]) => {{
            const cluster = L.markerClusterGroup({{
                disableClusteringAtZoom: 19,
                spiderfyOnMaxZoom: true,
                showCoverageOnHover: false
            }});
            clusters[era] = cluster;
            overlays[`<span style="color:${{style.color}}; font-weight:600;">${{style.display}}</span>`] = cluster;
            cluster.addTo(map);
        }});

        const bounds = L.latLngBounds();
        const fallbackStyle = {{ color: 'cadetblue', display: 'Other' }};

        markers.forEach((marker) => {{
            const style = eraStyles[marker.era] || fallbackStyle;
            const icon = L.AwesomeMarkers.icon({{
                prefix: 'fa',
                icon: marker.icon || 'landmark',
                markerColor: style.color || fallbackStyle.color,
                iconColor: 'white',
                extraClasses: 'fa-rotate-0'
            }});

            const description = marker.description
                ? `<p class="popup-description">${{marker.description}}</p>`
                : '';
            const image = marker.image
                ? `<div class="popup-image"><img src="${{marker.image}}" alt="${{marker.title}}"></div>`
                : '';
            const popupHtml = `
                <div class="popup-card">
                    <div class="popup-header">
                        <h3>${{marker.title}}</h3>
                        <p class="popup-era">Era: ${{marker.era}}</p>
                    </div>
                    ${{description}}
                    ${{image}}
                </div>
            `;

            L.marker([marker.lat, marker.lon], {{ icon }})
                .bindPopup(popupHtml, {{ maxWidth: 320, autoPanPadding: [30, 30] }})
                .addTo(clusters[marker.era] || map);

            bounds.extend([marker.lat, marker.lon]);
        }});

        map.fitBounds(bounds, {{ padding: [30, 30] }});
        L.control.layers({{ 'OpenStreetMap': baseLayer }}, overlays, {{ collapsed: true, position: 'topright' }}).addTo(map);
    </script>
</body>
</html>
"""


def main() -> None:
    OUTPUT_FILE.write_text(build_html(), encoding="utf-8")
    print(f"Map saved to {OUTPUT_FILE.resolve()}")


if __name__ == "__main__":
    main()
