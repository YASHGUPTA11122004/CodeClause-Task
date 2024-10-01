import torch
import cv2
import streamlit as st

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def detect_objects(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = model(frame_rgb)

    results.render()

    result_image = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)

    return result_image

def video_feed():
    cap = cv2.VideoCapture(0)
    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            st.write("Failed to grab frame.")
            break

        frame = detect_objects(frame)

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        stframe.image(frame_rgb, channels="RGB")

        if st.session_state["stop_stream"]:
            break

    cap.release()


st.title("YOLOv5 Object Detection")
st.sidebar.title("Control Panel")


if "stop_stream" not in st.session_state:
    st.session_state["stop_stream"] = False


if st.sidebar.button("Start Stream"):
    st.session_state["stop_stream"] = False  # Reset stop state
    video_feed()


if st.sidebar.button("Stop Stream"):
    st.session_state["stop_stream"] = True
