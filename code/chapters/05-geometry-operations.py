# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Geometry operations {#geometric-operations}
#
# ## Prerequisites

import pandas as pd
pd.set_option("display.max_rows", 4)
pd.set_option("display.max_columns", 6)

# Packages...

import matplotlib.pyplot as plt
import geopandas as gpd

# Sample data...

seine = gpd.read_file("data/seine.gpkg")
us_states = gpd.read_file("data/us_states.gpkg")
nz = gpd.read_file("data/nz.gpkg")

# ## Introduction
#
# ## Geometric operations on vector data {#geo-vec}
#
# ### Simplification
#
# Simplify...

seine_simp = seine.simplify(2000)  # 2000 m

# Plot:

fig, axes = plt.subplots(ncols=2)
seine.plot(ax=axes[0])
seine_simp.plot(ax=axes[1])
axes[0].set_title("Original")
axes[1].set_title("Simplified (d=2000 m)")

# Compare number of nodes:

import sys
sys.getsizeof(seine)       ## Original (bytes)

sys.getsizeof(seine_simp)  ## Simplified (bytes)

# US states example.... Transform...

us_states2163 = us_states.to_crs(2163)

# Simplify...

us_states_simp1 = us_states2163.simplify(100000)

# Plot...

us_states_simp1.plot()

import topojson as tp
topo = tp.Topology(us_states2163, prequantize=False)
us_states_simp2 = topo.toposimplify(100000).to_gdf()

fig, axes = plt.subplots(ncols=3)
us_states2163.plot(ax=axes[0])
us_states_simp1.plot(ax=axes[1])
us_states_simp2.plot(ax=axes[2])
axes[0].set_title("Original")
axes[1].set_title("Simplified (w/ geopandas)")
axes[2].set_title("Simplified (w/ topojson)")

# ### Centroids
#
# Centroids...

nz_centroid = nz.centroid
seine_centroid = seine.centroid

# Point on surface...

nz_pos = nz.representative_point()
seine_pos = seine.representative_point()

base = nz.plot(color="white", edgecolor="lightgrey")
nz_centroid.plot(ax=base, color="None", edgecolor="black");
nz_pos.plot(ax=base, color="None", edgecolor="red");

base = seine.plot(color="grey")
seine_centroid.plot(ax=base, color="None", edgecolor="black");
seine_pos.plot(ax=base, color="None", edgecolor="red");

# ### Buffers
#
# ...

# ### Affine transformations
#
# ...

# ### Clipping
#
# ...

# ### Subsetting and clipping
#
# ...

# ### Geometry unions
#
# ...

# ### Type transformations
#
# ...

# ## Geometric operations on raster data {#geo-ras}
#
# ### Geometric intersections
#
# ...

# ### Extent and origin
#
# ...

# ### Aggregation and disaggregation
#
# ...

# ### Resampling
#
# ...

# ## Exercises
#