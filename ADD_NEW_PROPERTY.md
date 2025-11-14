# How to Add a New Historic Property

## Quick Steps

1. **Get the property information from your mom:**
   - Address
   - Construction year (or "Circa XXXX")
   - Brief description/history
   - Photo of the property

2. **Get the coordinates:**
   - Go to [Google Maps](https://www.google.com/maps)
   - Search for the address
   - Right-click on the location and select the coordinates at the top
   - Copy the latitude and longitude (e.g., `40.39157, -74.38792`)

3. **Add the photo:**
   - Save the photo in the `images/` folder
   - Use a descriptive filename like `123mainst.jpeg`

4. **Edit `generate_map.py`:**
   - Find the `properties = [` section
   - Add your new property following the format below

5. **Generate the map:**
   ```bash
   python3 generate_map.py
   ```

6. **Commit and push:**
   ```bash
   git add index.html images/
   git commit -m "Add [Property Name]"
   git push
   ```

---

## Property Format

```python
[latitude, longitude, "Name", "Year", "Era", "Description", "image.jpeg", "icon_type", "color"],
```

### Example - Adding a new home from 1915:

```python
properties = [
    # ... existing properties ...

    # 1910-1919 (Blue) - Add your new property here
    [40.39252, -74.39352, "123 Main Street", "1915", "1910-1919",
     "Beautiful colonial home built in 1915 with original woodwork.",
     "123mainst.jpeg", "home", "blue"],
]
```

---

## Field Reference

| Field | Description | Examples |
|-------|-------------|----------|
| **latitude** | Latitude coordinate | `40.39157` |
| **longitude** | Longitude coordinate | `-74.38792` |
| **name** | Property name/address | `"123 Main Street"` |
| **year** | Construction year | `"1915"`, `"Circa 1920"`, `"1800s"` |
| **era** | Era category (determines color/cluster) | See Era Guide below |
| **description** | Brief history/description | `"Victorian home..."` |
| **image_filename** | Photo filename in images/ folder | `"123mainst.jpeg"` |
| **icon_type** | Marker icon | `"home"`, `"church"`, `"industry"`, `"store"` |
| **color** | Marker color (must match era) | See Era Guide below |

---

## Era Guide (Color Coding)

Choose the era based on construction year:

| Era | Year Range | Color | Example |
|-----|------------|-------|---------|
| `"1700s"` | Before 1800 | `"orange"` | `"1700s"`, `"1785"` |
| `"1800s"` | 1800-1899 | `"red"` | `"1850"`, `"1893"` |
| `"1900-1909"` | 1900-1909 | `"green"` | `"1905"`, `"1909"` |
| `"1910-1919"` | 1910-1919 | `"blue"` | `"1915"`, `"1918"` |
| `"1920-1929"` | 1920-1929 | `"black"` | `"1926"`, `"1929"` |
| `"1930-1939"` | 1930-1939 | `"pink"` | `"1935"`, `"1938"` |
| `"1940-1949"` | 1940-1949 | `"purple"` | `"1945"`, `"1949"` |
| `"1950-1959"` | 1950-1959 | `"darkred"` | `"1953"`, `"1955"` |

---

## Icon Types

- **`"home"`** - Residential properties (most common)
- **`"church"`** - Churches and religious buildings
- **`"industry"`** - Mills, forges, industrial buildings
- **`"store"`** - Commercial/retail buildings

---

## Complete Example

Your mom sends you: **"78 Oak Street, built around 1922, it was the old Johnson family home with a beautiful wraparound porch"**

**Step 1:** Get coordinates from Google Maps
- Result: `40.39100, -74.39200`

**Step 2:** Save photo as `images/78oakst.jpeg`

**Step 3:** Add to `generate_map.py`:

```python
# 1920-1929 (Black)
[40.39100, -74.39200, "78 Oak Street", "Circa 1922", "1920-1929",
 "The old Johnson family home with a beautiful wraparound porch built in the early 1920s.",
 "78oakst.jpeg", "home", "black"],
```

**Step 4:** Generate map:
```bash
python3 generate_map.py
```

**Step 5:** View `index.html` in your browser to preview, then push to GitHub!

---

## Tips

- Always add a comma at the end of your property entry (except the very last one)
- Keep descriptions concise (1-2 sentences)
- Image filenames should be lowercase with no spaces
- Double-check the era and color match
- Test locally before pushing to GitHub

## Need Help?

- Check existing entries in `generate_map.py` for examples
- Make sure Python 3 and Folium are installed: `pip install folium`
