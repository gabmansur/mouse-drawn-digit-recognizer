# Recognizing mouse-drawn digits with 5-layer Sequential CNN for digits recognition trained on MNIST dataset

Draw a digit, let a neural net guess what you wrote!  
This project combines a browser-based drawing canvas with a trained CNN model (Keras/TensorFlow) to recognize digits you sketch, just like the MNIST challenge, but interactive and more fun.

## Features

- **Interactive Web App:** Draw any digit (0–9) with your mouse (or finger, touchscreen), hit "Predict" and get instant feedback.
- **Custom CNN Model:** Trained on the MNIST dataset for accurate digit recognition.
- **Live Preprocessing:** Your doodle is resized, grayscaled, and formatted in real time to feed the model.
- **Full Pipeline:** From data to deep learning to browser inference (Flask backend, JS/canvas frontend).
- **Portable & Open:** Easy to run locally, great for demos, workshops, or learning computer vision basics.

## How It Works

1. **You draw a digit** in the browser (canvas).
2. **Canvas snapshot** is sent to the backend Flask server.
3. **Preprocessing:** Image is resized and normalized to match MNIST specs.
4. **CNN predicts** the digit and shows the result live.

## Getting Started

1. **Clone the repo**:
    ```bash
    git clone https://github.com/gabmansur/mouse-drawn-digit-recognizer.git
    cd mouse-drawn-digit-recognizer
    ```
2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3. **Run the app**:
    ```bash
    python app.py
    ```
4. **Visit** [http://localhost:5000](http://localhost:5000) in your browser. Draw & play!

## Model Details

- **Architecture:** Small Convolutional Neural Network (CNN) built in Keras.
- **Training Data:** MNIST handwritten digits (60,000 samples).
- **Performance:** >98% accuracy on test set.


## Why This Project?

Sometimes it’s more fun to *draw* your own data!  
This project shows how to bridge deep learning, web dev, and a bit of UI—perfect for beginners, tinkerers, or anyone looking for a tangible AI demo.


Snapshots from app: 

![initial](assets/canvas.PNG)
![initial](assets/canvas_filled.PNG)
![initial](assets/prediction.PNG)
