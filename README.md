# License Plate Recognition (YOLOv8)

This repository contains a YOLOv8 license plate detection project built from a Roboflow dataset. The goal is to train a YOLOv8 object detection model to detect license plates in images.

## Objective

- Train a license plate detector using the YOLOv8 model architecture.
- Use the provided dataset in YOLO format for training, validation, and testing.
- Save trained weights and evaluation outputs in the `runs/` folder.

## Project Structure

- `main.py`
  - Main training script for the project.
  - Instantiates a new YOLOv8 model from `yolov8n.yaml` and trains it using `data.yaml`.
  - Sets training options like `epochs`, `imgsz`, `project`, `name`, and `patience`.
  - Saves the final trained model to `license_plate_detector.pt`.

- `data.yaml`
  - YOLOv8 dataset configuration file.
  - Defines absolute paths for `train`, `val`, and `test` datasets.
  - Sets `nc: 1` because there is only one class.
  - Defines class names under `names:`.

- `train/`, `valid/`, `test/`
  - Standard YOLO dataset folders.
  - Each contains `images/` and `labels/` subfolders.
  - Labels are in YOLO text format (`class x_center y_center width height`).

- `runs/`
  - Contains model training output directories such as `license_plate_model`, `license_plate_model2`, `license_plate_model3`, and `license_plate_model4`.
  - Each directory stores training logs, plots, final weights, and metadata such as `args.yaml`.

- `README.roboflow.txt`
  - Metadata and export details from the original Roboflow dataset.
  - Describes dataset size, preprocessing, and augmentation.

- `README.dataset.txt`
  - Source and license information for the dataset.
  - Lists original dataset projects used in the export.

## Workflow

1. Dataset preparation
   - The dataset is already organized in the YOLOv8 expected structure with train/valid/test splits.
   - Each image has a corresponding `.txt` label file in the annotations folder.
   - `data.yaml` points to the dataset directories and specifies the class names.

2. Training
   - Run `main.py` to launch training.
   - The script builds a new YOLO model from `yolov8n.yaml` and trains with the settings provided.
   - Training output is saved under `runs/license_plate_model` or a similar named run directory.

3. Model saving
   - After training, the model is saved as `license_plate_detector.pt`.
   - Additional run directories may also contain intermediate weights, validation results, and plots.

4. Evaluation and inference
   - Use the saved model weights for inference on new images.
   - Evaluate detection quality using YOLOv8 built-in metrics or inspect outputs in the `runs/` directory.

## Usage

1. Install requirements (YOLOv8 / ultralytics):
   ```bash
   pip install ultralytics
   ```

2. Run training:
   ```bash
   python main.py
   ```

3. Use the trained model for inference with the Ultralytics API or YOLOv8 CLI.

## Notes

- The dataset is designed for a single class: `license_plate`.
- Training settings in `main.py` are a starting point and can be tuned further.
- `args.yaml` files in `runs/` store the exact command-line options used for each training run.

## Recommended Improvements

- Convert `data.yaml` paths to relative paths for portability.
- Add a dedicated inference script for testing the trained model on new images.
- Add environment and dependency management files like `requirements.txt`.
