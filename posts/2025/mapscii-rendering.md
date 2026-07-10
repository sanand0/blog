---
title: Mapscii Rendering
date: 2025-11-26T00:00:00+05:30
categories:
  - coding
description: I investigated MapSCII’s terminal rendering pipeline, which uses Braille characters to achieve 2x4 pixel density per cell. Key techniques include polygon triangulation with Earcut and filling horizontal spans between edge points using Bresenham’s algorithm.
---

I [asked Claude Sonnet 4.5 on GitHub Copilot](https://github.com/copilot/c/83dfdc9c-dbb5-4d8a-b16a-af25464bbec4):

> How does [mapscii](https://github.com/rastapasta/mapscii) render vector tiles as text blocks on the terminal? What are the libraries it uses and how does it use them? Explain as a detailed tutorial with examples so that I can learn how to rasterize vector shapes on the terminal.

Below's the explanation. What's noteworthy to me is:

- [How it uses Braille characters](#step-1-understanding-braille-characters-for-pixels) to get 8 pixels per character cell (2x4 grid).
- [How it fills polygons](#step-4-drawing-filled-polygons-with-earcut) using (a) triangulation and (b) getting all edge points using Bresenham's algorithm, then (c) filling horizontal spans between edge pairs.

---

I'll help you understand how mapscii renders vector tiles as text blocks on the terminal. Let me search through the repository to find the relevant code and understand the architecture. Now let me get more specific files to understand the rendering pipeline better:# How MapSCII Renders Vector Tiles as Text Blocks on the Terminal

MapSCII is a fascinating project that transforms geographic vector tiles into ASCII/Braille art on your terminal. Let me break down the complete rendering pipeline with detailed examples so you can learn how to rasterize vector shapes on the terminal.

## Architecture Overview

The rendering pipeline consists of several key components:

1. **TileSource** - Fetches and manages vector tiles
2. **Tile** - Parses vector tile data (Protobuf format)
3. **Renderer** - Orchestrates the rendering process
4. **Canvas** - Provides drawing primitives (lines, polygons)
5. **BrailleBuffer** - Converts pixels to Braille/ASCII characters

## Key Libraries Used

```json
{
  "@mapbox/vector-tile": "^1.3.1", // Parse vector tile format
  "pbf": "^3.2.1", // Protobuf decoding
  "earcut": "^2.2.2", // Polygon triangulation
  "rbush": "^3.0.1", // 2D spatial indexing
  "bresenham": "0.0.4", // Line rasterization
  "simplify-js": "^1.2.4", // Polyline simplification
  "x256": "0.0.2" // Color conversion to xterm-256
}
```

## Step-by-Step Tutorial

### Step 1: Understanding Braille Characters for Pixels

Braille characters are perfect for terminal graphics because each character represents a 2×4 pixel grid:

```javascript
// BrailleBuffer uses Unicode Braille patterns (U+2800 - U+28FF)
// Each Braille character has 8 dots in a 2×4 grid:
//
// ⠁ ⠂  (left column: 0x1, 0x2, 0x4, 0x40)
// ⠄ ⠈  (right column: 0x8, 0x10, 0x20, 0x80)
// ⠐ ⠠
// ⠈ ⡀

const brailleMap = [
  [0x1, 0x8],
  [0x2, 0x10],
  [0x4, 0x20],
  [0x40, 0x80],
];
```

Each Braille character gives you **8 pixels** in just one terminal cell, effectively quadrupling your resolution!

### Step 2: Creating a Braille Buffer

```javascript name=braille-buffer-example. js
class BrailleBuffer {
  constructor(width, height) {
    // Map of which bits correspond to which dot positions
    this.brailleMap = [
      [0x1, 0x8],
      [0x2, 0x10],
      [0x4, 0x20],
      [0x40, 0x80],
    ];

    // Store pixel state, colors
    const size = (width * height) / 8; // Each cell stores 8 pixels
    this.pixelBuffer = Buffer.alloc(size);
    this.foregroundBuffer = Buffer.alloc(size);
    this.backgroundBuffer = Buffer.alloc(size);
  }

  // Set a single pixel at (x, y)
  setPixel(x, y, color) {
    if (x >= 0 && x < this.width && y >= 0 && y < this.height) {
      // Project x,y to buffer index
      const idx = (x >> 1) + (this.width >> 1) * (y >> 2);

      // Get the specific dot mask for this pixel
      const mask = this.brailleMap[y & 3][x & 1];

      // Set the bit
      this.pixelBuffer[idx] |= mask;
      this.foregroundBuffer[idx] = color;
    }
  }

  // Generate terminal output
  frame() {
    const output = [];
    let currentColor = null;

    for (let y = 0; y < this.height / 4; y++) {
      for (let x = 0; x < this.width / 2; x++) {
        const idx = (y * this.width) / 2 + x;

        // Add ANSI color codes when color changes
        const colorCode = this._termColor(
          this.foregroundBuffer[idx],
          this.backgroundBuffer[idx],
        );
        if (currentColor !== colorCode) {
          output.push(currentColor = colorCode);
        }

        // Convert pixel bits to Braille character
        const brailleChar = String.fromCharCode(0x2800 + this.pixelBuffer[idx]);
        output.push(brailleChar);
      }
      output.push("\n");
    }

    return output.join("");
  }

  _termColor(foreground, background) {
    if (foreground && background) {
      return `\x1B[38;5;${foreground};48;5;${background}m`;
    } else if (foreground) {
      return `\x1B[49;38;5;${foreground}m`;
    }
    return "\x1B[39;49m"; // Reset
  }
}
```

### Step 3: Drawing Lines with Bresenham's Algorithm

```javascript name=line-drawing.js
const bresenham = require("bresenham");

class Canvas {
  constructor(width, height) {
    this.buffer = new BrailleBuffer(width, height);
  }

  // Draw a line from point A to point B
  line(from, to, color, width = 1) {
    if (width === 1) {
      // Simple bresenham for single-pixel width
      bresenham(from.x, from.y, to.x, to.y, (x, y) => {
        this.buffer.setPixel(x, y, color);
      });
    } else {
      // Thick line using Bresenham with width
      this._thickLine(from.x, from.y, to.x, to.y, width, color);
    }
  }

  // Draw a polyline (e.g., roads, rivers)
  polyline(points, color, width = 1) {
    for (let i = 1; i < points.length; i++) {
      this.line(points[i - 1], points[i], color, width);
    }
  }
}
```

### Step 4: Drawing Filled Polygons with Earcut

For filled areas (buildings, water bodies), MapSCII uses polygon triangulation:

```javascript name=polygon-drawing.js
const earcut = require("earcut");

class Canvas {
  polygon(rings, color) {
    // Convert rings to flat array of vertices
    const vertices = [];
    const holes = [];

    for (const ring of rings) {
      if (vertices.length) {
        holes.push(vertices.length / 2); // Mark hole start
      }
      for (const point of ring) {
        vertices.push(point.x);
        vertices.push(point.y);
      }
    }

    // Triangulate the polygon
    const triangles = earcut(vertices, holes);

    // Draw each triangle
    for (let i = 0; i < triangles.length; i += 3) {
      const pa = [vertices[triangles[i] * 2], vertices[triangles[i] * 2 + 1]];
      const pb = [
        vertices[triangles[i + 1] * 2],
        vertices[triangles[i + 1] * 2 + 1],
      ];
      const pc = [
        vertices[triangles[i + 2] * 2],
        vertices[triangles[i + 2] * 2 + 1],
      ];

      this._filledTriangle(pa, pb, pc, color);
    }
  }

  _filledTriangle(pointA, pointB, pointC, color) {
    // Get edges using Bresenham
    const a = bresenham(pointB[0], pointB[1], pointC[0], pointC[1]);
    const b = bresenham(pointA[0], pointA[1], pointC[0], pointC[1]);
    const c = bresenham(pointA[0], pointA[1], pointB[0], pointB[1]);

    // Combine and sort all edge points by Y, then X
    const points = a
      .concat(b)
      .concat(c)
      .filter((p) => p.y >= 0 && p.y < this.height)
      .sort((a, b) => (a.y === b.y ? a.x - b.x : a.y - b.y));

    // Fill horizontal spans between edge pairs
    for (let i = 0; i < points.length - 1; i++) {
      const point = points[i];
      const next = points[i + 1];

      if (point.y === next.y) {
        // Draw horizontal line
        for (let x = point.x; x <= next.x; x++) {
          this.buffer.setPixel(x, point.y, color);
        }
      } else {
        this.buffer.setPixel(point.x, point.y, color);
      }
    }
  }
}
```

### Step 5: Processing Vector Tiles

```javascript name=tile-processing.js
const VectorTile = require("@mapbox/vector-tile").VectorTile;
const Protobuf = require("pbf");
const RBush = require("rbush");
const zlib = require("zlib");

class Tile {
  async load(buffer) {
    // Decompress if gzipped
    if (this._isGzipped(buffer)) {
      buffer = await new Promise((resolve, reject) => {
        zlib.gunzip(buffer, (err, data) => {
          err ? reject(err) : resolve(data);
        });
      });
    }

    // Parse Protobuf
    this.tile = new VectorTile(new Protobuf(buffer));

    // Process each layer
    const layers = {};
    for (const name in this.tile.layers) {
      const layer = this.tile.layers[name];
      const nodes = [];

      for (let i = 0; i < layer.length; i++) {
        const feature = layer.feature(i);
        const geometries = feature.loadGeometry();

        // Get style for this feature
        const style = this.styler.getStyleFor(name, feature);
        if (!style) continue;

        // Convert geometries to nodes with boundaries
        for (const points of geometries) {
          nodes.push(
            this._addBoundaries({
              layer: name,
              style,
              points,
              color: this._getColor(style),
            }),
          );
        }
      }

      // Create spatial index for efficient querying
      const tree = new RBush(18);
      tree.load(nodes);

      layers[name] = {
        extent: layer.extent,
        tree,
      };
    }

    return layers;
  }
}
```

### Step 6: The Complete Rendering Pipeline

```javascript name=renderer.js
class Renderer {
  async draw(center, zoom) {
    this.canvas.clear();

    // 1. Calculate visible tiles
    const tiles = this._visibleTiles(center, zoom);

    // 2.  Fetch all tiles in parallel
    await Promise.all(
      tiles.map(async (tile) => {
        tile.data = await this.tileSource.getTile(
          tile.xyz.z,
          tile.xyz.x,
          tile.xyz.y,
        );

        // 3. Query spatial index for visible features
        const scale = tile.data.layers[layerId].extent / tileSize;
        tile.layers[layerId].features = tile.data.layers[layerId].tree.search({
          minX: -tile.position.x * scale,
          minY: -tile.position.y * scale,
          maxX: (this.width - tile.position.x) * scale,
          maxY: (this.height - tile.position.y) * scale,
        });
      }),
    );

    // 4. Draw features in correct order (background to foreground)
    const drawOrder = ["water", "landuse", "building", "road", "poi_label"];
    for (const layerId of drawOrder) {
      for (const tile of tiles) {
        for (const feature of tile.layers[layerId].features) {
          this._drawFeature(tile, feature, scale);
        }
      }
    }

    // 5. Generate terminal output
    return this.canvas.frame();
  }

  _drawFeature(tile, feature, scale) {
    // Transform coordinates from tile space to screen space
    const points = feature.points.map((p) => ({
      x: Math.floor(tile.position.x + p.x / scale),
      y: Math.floor(tile.position.y + p.y / scale),
    }));

    // Draw based on geometry type
    switch (feature.style.type) {
      case "line":
        this.canvas.polyline(
          points,
          feature.color,
          feature.style.paint["line-width"],
        );
        break;
      case "fill":
        this.canvas.polygon([points], feature.color);
        break;
      case "symbol":
        this.canvas.text(
          feature.label,
          points[0].x,
          points[0].y,
          feature.color,
        );
        break;
    }
  }
}
```

### Step 7: Coordinate Transformations

```javascript name=coordinate-utils.js
const utils = {
  // Convert lat/lon to tile coordinates at zoom level
  ll2tile(lon, lat, zoom) {
    const n = Math.pow(2, zoom);
    return {
      x: ((lon + 180) / 360) * n,
      y: ((1
        - Math.log(
            Math.tan((lat * Math.PI) / 180)
              + 1 / Math.cos((lat * Math.PI) / 180),
          ) / Math.PI) / 2) * n,
    };
  },

  // Convert tile coordinates back to lat/lon
  tile2ll(x, y, zoom) {
    const n = Math.pow(2, zoom);
    return {
      lon: (x / n) * 360 - 180,
      lat: (Math.atan(Math.sinh(Math.PI * (1 - (2 * y) / n))) * 180) / Math.PI,
    };
  },

  // Get tile size in pixels at fractional zoom
  tilesizeAtZoom(zoom) {
    return Math.pow(2, zoom - Math.floor(zoom)) * 256;
  },
};
```

## Complete Example: Drawing a Simple Map

```javascript name=simple-map-example.js
const Canvas = require("./Canvas");
const x256 = require("x256");

// Create a 160x64 pixel canvas (80x16 terminal cells in Braille mode)
const canvas = new Canvas(160, 64);

// Define some colors (xterm-256 color codes)
const BLUE = x256([0, 0, 255]);
const GREEN = x256([0, 200, 0]);
const GRAY = x256([128, 128, 128]);

// Draw a river (polyline)
const riverPoints = [
  { x: 20, y: 50 },
  { x: 40, y: 45 },
  { x: 60, y: 40 },
  { x: 80, y: 35 },
  { x: 100, y: 30 },
];
canvas.polyline(riverPoints, BLUE, 3);

// Draw a building (polygon)
const buildingRing = [
  { x: 70, y: 20 },
  { x: 90, y: 20 },
  { x: 90, y: 40 },
  { x: 70, y: 40 },
];
canvas.polygon([buildingRing], GRAY);

// Draw a road (polyline)
const roadPoints = [
  { x: 0, y: 25 },
  { x: 160, y: 25 },
];
canvas.polyline(roadPoints, GRAY, 2);

// Draw a label
canvas.text("Town Hall", 80, 30, GRAY);

// Output to terminal
process.stdout.write(canvas.frame());
```

## Performance Optimizations

MapSCII uses several clever optimizations:

1. **RBush Spatial Index**: Only processes features visible in the viewport
2. **Polyline Simplification**: Uses `simplify-js` to reduce point counts
3. **Tile Padding**: Renders slightly beyond viewport to avoid edge artifacts
4. **Draw Order Optimization**: Different layer orders for different zoom levels
5. **Color Caching**: Avoids repeated color conversions

## Key Takeaways

To rasterize vector shapes on the terminal:

1. **Use Braille characters** for 4x resolution boost (2×4 pixels per cell)
2. **Implement a pixel buffer** that maps coordinates to Braille dot positions
3. **Use Bresenham's algorithm** for line rasterization
4. **Use Earcut for polygon triangulation** and scanline filling
5. **Leverage xterm-256 colors** with ANSI escape codes
6. **Transform coordinates** from geographic space to screen space
7. **Use spatial indexing** (RBush) for efficient viewport queries

The complete rendering pipeline is: **Vector Tiles → Parse Protobuf → Query Spatial Index → Transform Coordinates → Rasterize to Pixels → Convert to Braille → Output ANSI Codes**

You can explore more implementation details in the [rastapasta/mapscii repository](https://github.com/rastapasta/mapscii).
