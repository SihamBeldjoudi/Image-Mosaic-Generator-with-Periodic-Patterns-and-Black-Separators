# **Image Mosaic Generator with Periodic Patterns and Black Separators**  

This Python script generates a mosaic image by combining sections of multiple input images. The composite image is structured into repeated patterns (periods) with black separator lines for clarity. The script is highly customizable and can be adapted for various image datasets and output formats.  

## **Features**  

- **Dynamic Image Selection**: Automatically selects a subset of images from a larger dataset, based on user-defined parameters.  
- **Periodic Mosaic Patterns**: Arranges image sections in structured rows and blocks, repeated over a defined number of periods.  
- **Black Separator Lines**: Adds visual separation between blocks and periods for enhanced readability.  
- **Customizable Dimensions**: Configurable input parameters for the number of images, periods, and output matrix size.  
- **Visualization and Saving**: Displays the generated mosaic and saves it as a PNG file.  


## **Example Output**  

The resulting mosaic combines sections of the selected images into a structured composite with black separators:  

| **Image Structure** | **Black Lines** |  
|----------------------|-----------------|  
| Repeated Patterns    | Between Blocks  |  
| Dynamic Sizing       | Between Periods |  


## **Installation**  

### Prerequisites  
Ensure you have Python 3.x installed and the following libraries:  
- `numpy`  
- `matplotlib`  
- `Pillow`  

Install the dependencies using `pip`:  
```bash  
pip install numpy matplotlib pillow  
```  

## **Usage**  

### 1. Prepare Input Images  
- Store your image files in the script's directory.  
- Name them using the format `Cam_X.png` (where `X` is an index, e.g., `Cam_0.png`, `Cam_6.png`).  

### 2. Run the Script  
Execute the script in your Python environment:  
```bash  
python _code_.py  
```  

### 3. Output  
- The generated mosaic image will be displayed using `matplotlib`.  
- It will also be saved in the script’s directory as `output_image.png`.  


## **Parameters**  

You can modify the following parameters in the script to adjust its behavior:  

| **Parameter**            | **Default Value** | **Description**                              |  
|---------------------------|-------------------|----------------------------------------------|  
| `total_images`           | `24`             | Total number of images available.            |  
| `images_to_use`          | `4`              | Number of images to include in the mosaic.   |  
| `matrix_height` / `matrix_width` | `512`     | Dimensions of the output mosaic image.       |  
| `periods`                | `5`              | Number of repeated patterns in the mosaic.   |  


## **How It Works**  

1. **Load Images**:  
   The script loads a subset of images based on the `images_to_use` parameter. It selects evenly spaced images from the total available files (`total_images`).  

2. **Matrix Initialization**:  
   Creates a zero-filled matrix of size `(matrix_height, matrix_width, 3)` to hold the mosaic image.  

3. **Image Placement**:  
   - Divides the matrix into sections (`blocks`) based on the number of periods and images.  
   - Fills each block with rows from the corresponding image.  

4. **Black Separator Lines**:  
   - Inserts black lines (RGB `[0, 0, 0]`) between blocks and periods to visually separate them.  

5. **Display and Save**:  
   - Displays the final image using `matplotlib`.  
   - Saves the output to a file (`output_image.png`).  


## **Example Output Visualization**  

Below is an example of how the generated mosaic might look:  

| **Pattern Example**         |  
|-----------------------------|  
| Block 1 (Image 1 rows)      |  
| Black Separator Line        |  
| Block 2 (Image 2 rows)      |  
| Black Separator Line        |  
| (Repeat for each period)    |  



## **Customization and Enhancements**  

### Customize the Output  
- Adjust the `images_to_use` and `periods` parameters for different patterns.  
- Change the `matrix_height` and `matrix_width` values to match your dataset.  

### Possible Enhancements  
- Add support for varying image resolutions.  
- Handle missing or mismatched files gracefully.  
- Introduce a graphical interface for parameter configuration.  
- Output additional metrics or logs for debugging purposes.  


