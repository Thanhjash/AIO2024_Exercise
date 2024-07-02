import cv2
import numpy as np
from PIL import Image
import streamlit as st

MODEL = "../M1_Week4_220624/model/MobileNetSSD_deploy.caffemodel"  # Update path to your model file
PROTOTXT = "../M1_Week4_220624/model/MobileNetSSD_deploy.prototxt.txt"  # Update path to your prototxt file

# List of labels for the objects that MobileNet SSD can detect
LABELS = ["background", "aeroplane", "bicycle", "bird", "boat", 
          "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", 
          "dog", "horse", "motorbike", "person", "pottedplant", "sheep", 
          "sofa", "train", "tvmonitor"]

def process_image(image):
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
    net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)
    net.setInput(blob)
    detections = net.forward()
    return detections

def annotate_image(image, detections, confidence_threshold=0.5):
    (h, w) = image.shape[:2]
    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > confidence_threshold:
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            label = f"{LABELS[idx]}: {confidence:.2f}"
            cv2.rectangle(image, (startX, startY), (endX, endY), (70, 2), 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(image, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    return image

def main():
    st.title('Object Detection for Images')
    file = st.file_uploader('Upload Image', type=['jpg', 'png', 'jpeg'])
    if file is not None:
        st.image(file, caption="Uploaded Image")
        image = Image.open(file)
        image = np.array(image)
        detections = process_image(image)
        processed_image = annotate_image(image, detections)
        st.image(processed_image, caption="Processed Image")

if __name__ == "__main__":
    main()
