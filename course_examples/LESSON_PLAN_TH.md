# Lesson Plan (Thai)

## Goal

เป้าหมายของชุดบทเรียนนี้คือ:
- ให้ผู้เรียนเข้าใจพื้นฐานของภาพและ webcam ด้วย OpenCV แบบคร่าว ๆ
- ใช้ custom model ที่มีอยู่แล้วให้เป็นก่อน
- เข้าใจ dataset และการ train custom model
- ต่อยอดไปสู่การทดลอง เปรียบเทียบผล และ export model

## Teaching Order

### Lesson 1: OpenCV overview
เป้าหมาย:
- รู้ว่า image คืออะไร
- รู้ว่า webcam ให้ frame ต่อเนื่องอย่างไร
- ใช้ OpenCV อ่านภาพและเปิดกล้องได้

สคริปต์:
- `00_check_env.py`
- `01_opencv_image_basic.py`
- `02_opencv_webcam.py`

กิจกรรมทดลอง:
- เปลี่ยนรูป input
- เปลี่ยนขนาดภาพ
- วาดข้อความหรือกรอบลงบนภาพ
- เปิด webcam แล้วสังเกต frame แบบ real-time

### Lesson 2: Predict with a trained model
เป้าหมาย:
- ใช้โมเดลที่เทรนแล้วกับภาพจริง
- เข้าใจ `SOURCE`, `CONFIDENCE`, `IMAGE_SIZE`

สคริปต์:
- `10_easy_predict.py`
- `easy_config.py`

กิจกรรมทดลอง:
- เปลี่ยน `SOURCE`
- เปลี่ยน `CONFIDENCE` เป็น `0.10`, `0.25`, `0.50`
- เปลี่ยน `IMAGE_SIZE` เป็น `320`, `640`, `960`
- สรุปว่าความเร็วและความแม่นเปลี่ยนอย่างไร

### Lesson 3: Train a custom model
เป้าหมาย:
- เข้าใจ dataset structure
- เข้าใจว่า custom model มาจาก data และ config
- train model ใหม่ได้

สคริปต์:
- `11_easy_train.py`
- `easy_config.py`
- `03_download_roboflow.py` ถ้าต้องการสอนโหลด dataset

กิจกรรมทดลอง:
- เปลี่ยน `BASE_MODEL`
- เปลี่ยน `EPOCHS`
- เปลี่ยน `BATCH`
- เปลี่ยน `TRAIN_RUN_NAME`

### Lesson 4: Evaluate and continue
เป้าหมาย:
- เปรียบเทียบ run ที่ train มา
- ทดลองกับ webcam หรือภาพจริงนอก dataset
- export model ไปใช้ต่อ

สคริปต์:
- `12_easy_webcam.py`
- `13_easy_compare.py`
- `14_easy_export.py`

กิจกรรมทดลอง:
- ใช้ webcam ทดสอบของจริง
- ดูว่า run ไหนดีที่สุด
- export model เป็น `openvino` หรือ `onnx`

## Suggested Format Per Lesson

แต่ละบทควรมี 3 ส่วน:
- อธิบายแนวคิดสั้น ๆ
- เดโมให้เห็นผลจริง
- ให้ผู้เรียนทดลองปรับ 1-3 ค่าแล้วสรุปสิ่งที่เปลี่ยนไป

ตัวอย่างเวลา:
- อธิบาย 10-15 นาที
- เดโม 10 นาที
- ทดลอง 15-20 นาที
- สรุป 5-10 นาที

## Why This Order

เหตุผลของลำดับนี้คือ:
- ไม่จมกับ OpenCV นานเกินไป
- ผู้เรียนได้เห็นงานจริงเร็ว
- ทุกบทมีจุดทดลองให้เข้าใจ ไม่ใช่แค่รันตาม
- เมื่อจบบท ผู้เรียนสามารถเอา flow นี้ไปทำโปรเจกต์ต่อได้
