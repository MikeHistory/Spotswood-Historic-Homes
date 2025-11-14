# Spotswood Historic Homes - Python Map Generator

This Python script generates the interactive map for Spotswood Historic Homes.

## Setup (First Time Only)

1. **Install Python 3** (if not already installed)
   - Download from https://python.org
   - Or use your system's package manager

2. **Install Folium**
   ```bash
   pip install -r requirements.txt
   ```
   Or:
   ```bash
   pip install folium
   ```

## Usage

### Generate the Map

```bash
python3 generate_map.py
```

This will create/update `index.html` with all the historic properties.

### Add a New Property

See **[ADD_NEW_PROPERTY.md](ADD_NEW_PROPERTY.md)** for detailed instructions.

**Quick version:**
1. Edit `generate_map.py`
2. Add your new property to the `properties` list
3. Run `python3 generate_map.py`
4. Commit and push changes

## Files

- **`generate_map.py`** - Main Python script that generates the map
- **`ADD_NEW_PROPERTY.md`** - Step-by-step guide for adding properties
- **`requirements.txt`** - Python dependencies
- **`index.html`** - Generated map (created by the script)
- **`images/`** - Property photos

## Features

The generated map includes:
- ✓ Interactive Leaflet map with OpenStreetMap and Google Satellite layers
- ✓ Custom colored markers by era (1700s-1950s)
- ✓ Different icons for homes, churches, and industrial buildings
- ✓ Construction year tooltips above each pin
- ✓ Detailed popups with photos and descriptions
- ✓ Mobile-responsive design
- ✓ Marker clustering for better performance

## Property Data Structure

```python
[latitude, longitude, name, year, era, description, image_filename, icon_type, marker_color]
```

**Example:**
```python
[40.39157, -74.38792, "300 Manalapan Ave", "1905", "1900-1909",
 "Early 20th century home in the residential section of town.",
 "300manalapanave.jpeg", "home", "green"]
```

## Workflow for Adding Homes

When your mom sends you a new property:

1. Get the address and info
2. Look up coordinates on Google Maps (right-click → coordinates)
3. Save photo to `images/` folder
4. Edit `generate_map.py` and add the property
5. Run `python3 generate_map.py`
6. Preview `index.html` in your browser
7. Git commit and push

```bash
git add index.html images/
git commit -m "Add [property address]"
git push
```

## Need Help?

- Check `ADD_NEW_PROPERTY.md` for detailed instructions
- Look at existing entries in `generate_map.py` for examples
- Make sure Folium is installed: `pip install folium`

## GitHub Pages

The map is automatically published to:
https://donald-coyote.github.io/Spotswood-Historic-Homes/

Changes pushed to the `main` branch will appear live within a few minutes.
