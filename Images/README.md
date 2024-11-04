# Foreshore Vulnerability Assessment Data Documentation

This document provides a summary of the datasets used in the Foreshore Vulnerability Assessment Tool, including details on data collection, processing, and any modifications made.

---

## 1. GNSS Data
- **Source**: Collected by In_Coast
- **Description**: The names of GNSS points were manually edited to facilitate ease of identification.

## 2. Water Level Data
- **Source**: Collected by In_Coast
- **Processing**: Data was downloaded using HOBOWARE software.

## 3. Wave Data
- **Source**: Collected by In_Coast from 2020-2022
- **Description**: File names were renamed for convenience.

## 4. Vegetation Data
- **Source**: Collected by In_Coast
- **Description**: No modifications were made to this dataset.

## 5. Digital Surface Model (DSM) Data
- **Source**: Provided by MP_Sparc and downloaded from GeoNB
- **Processing**:
  - The MP_Sparc data was used as-is with no modifications.
  - GeoNB data was converted from LAZ to LAS format using `arcpy.conversion.ConvertLas` in ArcPro.
  - The LAS files were organized into a LAS dataset using `arcpy.management.CreateLasDataset`.
  - Noise was classified and removed by adjusting the LAS dataset properties.

## 6. Dike Data
- **Description**: This dataset was created through manual interpolation using the Point-to-Line tool in ArcPro.

## 7. Transect Data
- **Source**: Created using the AMBUR package in R
- **Description**: Transects were generated based on the Dike Data.

## 8. Marsh Data
- **Source**: Derived from DSMs
- **Processing**:
  - The dataset was created using the Contour tool in ArcPro, with a contour elevation of 4.5 m.
  - The contour lines were manually cleaned after generation.

---

This documentation provides a quick reference for each dataset used, its sources, and any processing steps. For further details, refer to individual scripts and processing files.