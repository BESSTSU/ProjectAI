# Main learning config
# Edit only this file during the lessons.
# Paths can be relative to the project root, for example: Model/... or course_examples/...

# Shared settings used by multiple scripts
MODEL_PATH = ""  # Leave blank to auto-pick the best trained weights.
IMAGE_SIZE = 640
CONFIDENCE = 0.25
DEVICE = None  # None, "cpu", or GPU index such as 0

# Lesson 2: predict from an image or folder
SOURCE = "Model/Woodenbox-13/valid/images/1000049575_frame_003_jpg.rf.bb057e9949f7ed3eeecde88b6efa3e78.jpg"
SHOW_WINDOW = False
SAVE_OUTPUT = True
PREDICT_OUTPUT_DIR = "course_examples/outputs/easy_runner"
PREDICT_OUTPUT_NAME = "predict_run"

# Lesson 3: train a custom model
DATA_YAML = "Model/Woodenbox-13/data.yaml"
BASE_MODEL = "yolo11s.pt"
EPOCHS = 10
BATCH = 8
TRAIN_RUN_NAME = "easy_demo"
TRAIN_PROJECT_DIR = "Model/runs/course"

# Lesson 4: webcam test
CAMERA_INDEX = 0
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480

# Lesson 4: export model
EXPORT_FORMAT = "openvino"  # openvino, torchscript, onnx
EXPORT_HALF = False
