# A Tool for Foreshore Vulnerability Assessment
This README provides an organized, high-level overview of the project, including file structure, instructions, and key features, which will make it easy for others to understand and navigate the project. 

### Authors
Christian Hart, Danika Van Proosdij, Chris Ross, Makadunyiswe Ngulube, Marijke de Vet

---

## Project Overview
This project introduces a **Foreshore Vulnerability Assessment Tool** designed to evaluate the protective capacity of foreshore marshes under varying future erosive conditions and water depth scenarios. The tool provides spatial predictions of marsh widths necessary for wave attenuation relative to current marsh and dike locations, assisting in identifying areas where dike realignment could mitigate wave impacts and reduce overtopping risk.

## Abstract
The tool integrates wave measurements, modeling, and multiple GIS datasets—including manual survey points, digital surface models (DSMs), and vegetation characteristics—to assess vulnerability in a section of the hypertidal Upper Bay of Fundy, Canada. Wave parameters were obtained from RBR pressure sensors deployed sequentially along two transect lines extending from mudflats to the salt marsh platform. This GIS-based analysis determines current marsh widths, calculates end-point erosion rates, and compiles marsh elevation statistics across the study area. The tool employs a hybrid model combining process-based modeling and machine learning, producing predictions that align well with existing literature. By comparing current marsh extents with predicted widths, the tool highlights the vulnerability of certain areas to wave action, particularly during extreme tides and storm events. The findings suggest that dike realignment could benefit several sections of the study area, providing a nature-based solution to reduce the impact of flooding.

## Key Features
- **Wave Attenuation Analysis**: Calculates marsh widths required to attenuate waves under future erosive and water depth scenarios.
- **Erosion Analysis**: Calculates end-point erosion rates through projected shoreline transects and their intersection with shoreline shapefiles.
- **GIS Integration**: Uses high-resolution GIS data from multiple sources, including manual surveys and DSMs.
- **Predictive Modeling**: Combines process-based and machine learning methods to predict marsh widths.

## Project Structure

1_data&prep
2_WaterLevelAnalysis
3_WaveAnalysis
4_GISAnalysis


## Getting Started
1. **Install Dependencies**: Ensure you have Python and required packages, as well as ArcPRO installed. :