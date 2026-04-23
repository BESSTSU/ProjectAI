# Learning Guide (Thai)

แนวที่อ่านง่ายสำหรับคนเรียนคือ:
- `.env` ใช้เก็บ secret เท่านั้น เช่น API key
- `easy_config.py` ใช้เก็บค่าที่ผู้เรียนควรลองแก้
- แยก script ตามงาน และแต่ละไฟล์มีโค้ดของตัวเอง

## 1. ไฟล์ที่ผู้เรียนควรแก้

แก้ไฟล์:
- `course_examples/scripts/easy_config.py`

ไฟล์นี้รวมค่าที่ควรลองปรับ เช่น:
- model path
- source ของรูปหรือวิดีโอ
- confidence
- image size
- epochs
- batch

## 2. `.env` ใช้เก็บอะไร

เหมาะกับข้อมูลที่ไม่ควร hardcode เช่น:
- `ROBOFLOW_API_KEY`

ไม่ควรใช้ `.env` เป็นที่เก็บ config หลักของบทเรียน เพราะ:
- คนเรียนมองไม่เห็นภาพรวมง่าย
- ค่าหลายตัวเป็น string หมด อ่านยาก
- เวลาสอนเรื่อง parameter ของ model จะอธิบายยากขึ้น

## 3. คำสั่งที่อ่านง่ายกว่าเดิม

### Predict
```powershell
python .\course_examples\scripts\10_easy_predict.py
```

### Train
```powershell
python .\course_examples\scripts\11_easy_train.py
```

### Webcam
```powershell
python .\course_examples\scripts\12_easy_webcam.py
```

### Compare
```powershell
python .\course_examples\scripts\13_easy_compare.py
```

### Export
```powershell
python .\course_examples\scripts\14_easy_export.py
```

## 4. สิ่งที่ผู้เรียนควรลองทำ

### Predict
- เปลี่ยน `SOURCE` เป็นรูปอื่น
- เปลี่ยน `CONFIDENCE` แล้วดูผล
- เปลี่ยน `IMAGE_SIZE` แล้วเทียบความเร็วกับความแม่น

### Train
- เปลี่ยน `BASE_MODEL` ระหว่าง `yolo11n.pt`, `yolo11s.pt`, `yolo11m.pt`
- เปลี่ยน `EPOCHS`
- เปลี่ยน `BATCH`
- เปลี่ยน `TRAIN_RUN_NAME`

### Compare
- ดูว่า run ไหนดีที่สุด
- ให้ผู้เรียนสรุปว่าค่าไหนทำให้ผลดีขึ้น

### Webcam
- ทดลองกับวัตถุจริงหน้ากล้อง
- สังเกตผลของแสง มุมกล้อง และระยะ

### Export
- แปลง model ไปเป็น format ที่ใช้ deploy
- เปรียบเทียบว่า format ไหนเหมาะกับงานจริง
