# Course Blueprint

## ชื่อคอร์ส
Custom Computer Vision AI with Python on Raspberry Pi

## แนวคิดของคอร์ส
คอร์สนี้สอนผู้เรียนให้สร้างระบบ Computer Vision AI ตั้งแต่การอ่านภาพด้วย OpenCV, การเตรียมข้อมูล, การ train โมเดล YOLO แบบ custom, การวัดผลโมเดล, ไปจนถึงการ deploy บน Raspberry Pi เพื่อใช้งานจริงแบบ edge AI

จุดขายของคอร์ส:
- เขียนด้วย Python ทั้งสายงาน
- ใช้ dataset จริงและ train จริง
- สามารถ custom model ตามโจทย์ของผู้เรียนได้
- มีเส้นทางจาก PC/GPU ไปสู่ Raspberry Pi deployment ชัดเจน

## กลุ่มเป้าหมาย
- ผู้เริ่มต้นถึงระดับกลางที่เขียน Python ได้เบื้องต้น
- ผู้สนใจ AI, IoT, Robotics, Smart Factory
- ผู้ที่อยากทำ object detection บนอุปกรณ์ edge

## ผลลัพธ์ที่ผู้เรียนควรทำได้
- ใช้ OpenCV อ่านภาพ, วิดีโอ, และกล้องได้
- เข้าใจพื้นฐานของ object detection
- สร้าง dataset และ label ข้อมูลของตัวเองได้
- train YOLO model แบบ custom ได้
- เปรียบเทียบโมเดลหลายขนาดและเลือกโมเดลให้เหมาะกับงาน
- export model เพื่อนำไป deploy บน Raspberry Pi ได้
- เขียน inference pipeline สำหรับงานจริงได้

## โครงคอร์สแนะนำ

### Module 1: Python + OpenCV Fundamentals
หัวข้อ:
- ภาพคืออะไร, pixel, color space, resolution
- BGR vs RGB
- การอ่านภาพและวิดีโอด้วย OpenCV
- การ resize, crop, draw, threshold, edge detection
- การเปิดกล้องและอ่าน frame แบบ real time

Lab:
- อ่านภาพจากไฟล์
- เปิด webcam แล้ววาดกรอบ/ข้อความลงบนภาพ
- แปลงภาพเป็น grayscale และตรวจจับขอบ

ผลลัพธ์:
- ผู้เรียนใช้ OpenCV เป็นฐานก่อนเข้าสู่ AI model

### Module 2: Introduction to Computer Vision AI
หัวข้อ:
- ความต่างระหว่าง image processing กับ AI vision
- classification, detection, segmentation
- แนวคิดของ dataset, label, train, val, test
- precision, recall, mAP แบบเข้าใจง่าย

Lab:
- ทดลองใช้ pretrained model ตรวจจับวัตถุจากภาพหรือวิดีโอ

ผลลัพธ์:
- ผู้เรียนเข้าใจ pipeline ของงาน Computer Vision AI

### Module 3: Data Collection and Labeling
หัวข้อ:
- การกำหนดโจทย์ detection ให้ชัด
- การเก็บภาพให้ครอบคลุมสภาพจริง
- หลักการ label ที่ดี
- การใช้ Roboflow หรือเครื่องมือ labeling อื่น
- การ split train/valid/test

Lab:
- สร้าง dataset ของวัตถุจริง 1 งาน
- export dataset เป็นรูปแบบ YOLO

ผลลัพธ์:
- ผู้เรียนมี dataset พร้อม train

### Module 4: Custom YOLO Model Training
หัวข้อ:
- โครงสร้างการ train ของ YOLO
- ความต่างของ `yolo11n`, `yolo11s`, `yolo11m`, `yolo11x`
- batch size, epoch, image size
- pretrained model และ transfer learning
- การอ่านผล `results.csv`, loss, precision, recall, mAP

Lab:
- train 2 ขนาดโมเดลขึ้นไป
- เปรียบเทียบความแม่นยำกับเวลา train
- เลือก model ที่เหมาะกับการ deploy

ผลลัพธ์:
- ผู้เรียน train โมเดล custom และวิเคราะห์ผลได้

### Module 5: Model Optimization for Raspberry Pi
หัวข้อ:
- ข้อจำกัดของ Raspberry Pi: CPU, RAM, FPS, latency
- ทำไมต้องเลือกโมเดลให้เหมาะกับ edge device
- export model เป็น OpenVINO หรือ TorchScript
- half precision และแนวคิดเรื่อง optimization
- กรณีมี AI HAT / accelerator กับกรณีใช้ CPU ล้วน

Lab:
- export model จากผล train
- เปรียบเทียบ performance ระหว่าง model size ต่างกัน

ผลลัพธ์:
- ผู้เรียนรู้ว่าความแม่นยำอย่างเดียวไม่พอ ต้องดูความเร็วด้วย

### Module 6: Real-Time Inference on Raspberry Pi
หัวข้อ:
- การติดตั้ง environment บน Raspberry Pi
- การอ่านภาพจากกล้อง
- inference loop
- การแสดงผล bounding box, class, confidence
- การออกแบบระบบให้เสถียรสำหรับงานจริง

Lab:
- รัน object detection แบบ real time บน Raspberry Pi
- บันทึกภาพหรือส่งผลลัพธ์ออก serial/network ได้

ผลลัพธ์:
- ผู้เรียน deploy ระบบ end-to-end ได้

### Module 7: Capstone Project
โจทย์แนะนำ:
- ตรวจจับกล่องไม้
- ตรวจจับชิ้นงานบนสายพาน
- ตรวจจับวัตถุเฉพาะทางในโรงงานหรือห้องทดลอง

ผลส่งมอบ:
- dataset
- trained model
- Raspberry Pi demo
- สรุปผล accuracy และ FPS

## โครงเวลาแนะนำ
- แบบเร่งรัด 1 วัน:
  - ช่วงเช้า: OpenCV + Vision AI + Dataset
  - ช่วงบ่าย: Training + Export + Deploy Demo
- แบบ 2 วัน:
  - Day 1: OpenCV, dataset, labeling, training
  - Day 2: evaluation, optimization, Raspberry Pi deployment, capstone
- แบบ 6-8 สัปดาห์:
  - สัปดาห์ละ 1 module พร้อมงานบ้าน

## โครงสร้างโปรเจกต์ปัจจุบันที่นำมาใช้สอนได้
- `AI course.docx` มี draft เนื้อหา OpenCV และ custom AI model training
- `Model/Woodenbox-13/` เป็น dataset YOLO พร้อม `data.yaml`
- `Model/Yolo (1).ipynb` เป็น notebook สำหรับดาวน์โหลด dataset และ train
- `Model/runs/detect/` มีผลการ train หลายรอบสำหรับเปรียบเทียบ

## Insight จากไฟล์ที่มีอยู่
- dataset ที่ใช้จริงอยู่ที่ `Model/Woodenbox-13/data.yaml`
- มีการ train หลายขนาดโมเดลและเก็บผลไว้แล้ว
- จากผลที่ตรวจดู:
  - `yolo11s` run `train23` ได้ `mAP50-95 ≈ 0.83023`
  - `yolo11m` run `train24` ได้ `mAP50-95 ≈ 0.81992`
- สำหรับการสอนบน Raspberry Pi ควรใช้ `yolo11s` เป็น baseline เพราะสมดุลกว่าเรื่องขนาดและความแม่นยำ

## ข้อแนะนำก่อนนำไปสอนจริง
- แยก workflow ให้ชัด:
  - train บนเครื่องที่มี GPU
  - deploy บน Raspberry Pi
- อย่า hardcode API key ใน notebook
- อย่า hardcode path ที่ผูกกับเครื่องเดียว
- เพิ่มไฟล์ตัวอย่างสำหรับ inference บน Raspberry Pi โดยเฉพาะ
- เตรียม slide ที่มีภาพ pipeline เดียวกันทั้งคอร์ส:
  - collect data
  - label
  - train
  - evaluate
  - export
  - deploy

## โครง Lab ที่ควรมีในคอร์ส
1. OpenCV image and video basics
2. Webcam real-time processing
3. Build custom dataset
4. Label and export YOLO dataset
5. Train YOLO custom model
6. Compare `n/s/m` model sizes
7. Export to edge format
8. Run inference on Raspberry Pi
9. Final custom project

## จุดที่ควรปรับจาก notebook ปัจจุบัน
- เปลี่ยนการใช้ API key เป็น environment variable
- แก้ path dataset ให้ตรงกับโฟลเดอร์ `Model/Woodenbox-13`
- แยก cell สำหรับ:
  - install
  - dataset download
  - train
  - evaluate
  - export
- เพิ่มส่วน inference test หลัง train เพื่อให้ผู้เรียนเห็นผลทันที

## รูปแบบการขายคอร์ส
ประโยคสั้นสำหรับใช้โปรโมต:

เรียนสร้างระบบ AI ตรวจจับวัตถุด้วย Python บน Raspberry Pi ตั้งแต่พื้นฐาน OpenCV ไปจนถึงการ train โมเดล custom ของตัวเองและ deploy ใช้งานจริงได้

## สิ่งที่ควรทำต่อ
1. แปลง `AI course.docx` เป็น slide outline แบบเป็นบทเรียน
2. สร้าง notebook เวอร์ชันสอนจริงที่ไม่มี secret key
3. สร้าง script inference สำหรับ Raspberry Pi
4. เตรียม benchmark accuracy/FPS ของแต่ละโมเดล
