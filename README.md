# ชุดโค้ดตัวอย่างสำหรับคอร์ส

โฟลเดอร์นี้รวมโค้ดตัวอย่างตั้งแต่เริ่มต้นจนถึง deploy:
- ติดตั้ง environment
- ทดลอง OpenCV พื้นฐาน
- ดาวน์โหลด dataset จาก Roboflow
- train YOLO custom model
- predict จากภาพเดี่ยว
- compare ผล train
- export model
- รัน inference จากกล้องบน Raspberry Pi

## 1. เตรียมเครื่อง

เปิด PowerShell ที่โฟลเดอร์โปรเจกต์นี้:

```powershell
cd G:\intern-practice\Assign\reserchAI
```

สร้าง virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

อัปเกรด pip และติดตั้ง package:

```powershell
python -m pip install --upgrade pip
pip install -r .\course_examples\requirements.txt
```

ตรวจสภาพแวดล้อม:

```powershell
python .\course_examples\scripts\00_check_env.py
```

## 2. ตั้งค่า Roboflow API key

สร้างไฟล์ `.env`:

```powershell
Copy-Item .\course_examples\.env.example .\course_examples\.env
```

จากนั้นเปิด `course_examples\.env` แล้วใส่ค่า:

```text
ROBOFLOW_API_KEY=your_real_key
```

## 3. ใช้ dataset ที่มีอยู่แล้ว

โปรเจกต์นี้มี dataset อยู่แล้วที่:

```text
Model\Woodenbox-13\data.yaml
```

ดังนั้นถ้าจะสอนแบบเร็ว สามารถข้ามขั้น download แล้วไป train ต่อได้เลย

## 4. ดาวน์โหลด dataset ใหม่จาก Roboflow

```powershell
python .\course_examples\scripts\03_download_roboflow.py
```

ถ้าจะระบุ project เอง:

```powershell
python .\course_examples\scripts\03_download_roboflow.py --workspace myworkspace --project myproject --version 1
```

## 5. ตัวอย่าง OpenCV ง่ายๆ

ประมวลผลภาพพื้นฐาน:

```powershell
python .\course_examples\scripts\01_opencv_image_basic.py
```

ถ้าจะใช้รูปของตัวเอง:

```powershell
python .\course_examples\scripts\01_opencv_image_basic.py --input .\my_image.jpg
```

เปิด webcam:

```powershell
python .\course_examples\scripts\02_opencv_webcam.py
```

## 6. Train YOLO custom model

ใช้ dataset ในโปรเจกต์นี้:

```powershell
python .\course_examples\scripts\04_train_yolo.py
```

ตัวอย่างปรับค่าการ train:

```powershell
python .\course_examples\scripts\04_train_yolo.py --model yolo11n.pt --epochs 20 --batch 16 --imgsz 640 --name yolo11n_demo
```

ถ้าจะใช้ CPU:

```powershell
python .\course_examples\scripts\04_train_yolo.py --device cpu
```

## 7. Predict จากภาพเดี่ยว

สคริปต์นี้จะพยายามใช้ `train23/weights/best.pt` ก่อน:

```powershell
python .\course_examples\scripts\05_predict_image.py
```

หรือระบุ model และภาพเอง:

```powershell
python .\course_examples\scripts\05_predict_image.py --model .\Model\runs\detect\train23\weights\best.pt --source .\Model\Woodenbox-13\valid\images\1000049575_frame_003_jpg.rf.bb057e9949f7ed3eeecde88b6efa3e78.jpg
```

## 8. Compare ผลการ train

สรุปว่า run ไหนแม่นกว่า:

```powershell
python .\course_examples\scripts\06_compare_training_runs.py
```

## 9. Export model

Export เป็น OpenVINO:

```powershell
python .\course_examples\scripts\07_export_model.py --format openvino --half
```

Export เป็น TorchScript:

```powershell
python .\course_examples\scripts\07_export_model.py --format torchscript
```

## 10. Raspberry Pi real-time inference

หลังจากย้าย model ไปที่ Raspberry Pi แล้ว:

```powershell
python .\course_examples\scripts\08_rpi_webcam_inference.py --model .\best.pt
```

หรือถ้ามี model อยู่แล้วในโปรเจกต์:

```powershell
python .\course_examples\scripts\08_rpi_webcam_inference.py
```

## ลำดับแนะนำเวลาสอน

1. `00_check_env.py`
2. `01_opencv_image_basic.py`
3. `02_opencv_webcam.py`
4. `03_download_roboflow.py`
5. `04_train_yolo.py`
6. `05_predict_image.py`
7. `06_compare_training_runs.py`
8. `07_export_model.py`
9. `08_rpi_webcam_inference.py`

## หมายเหตุสำคัญ

- training ควรทำบนเครื่องที่มี GPU จะเร็วกว่า Raspberry Pi มาก
- Raspberry Pi เหมาะกับ inference มากกว่า training
- อย่าเก็บ API key ไว้ใน notebook หรือ commit ลง repo
- ถ้าจะใช้บน Raspberry Pi 5 แบบ CPU-only ให้เริ่มจากโมเดลเล็ก เช่น `yolo11n` หรือ `yolo11s`
