Facial Recognition Application with DeepFace

This project is a Python-based facial recognition application utilizing the DeepFace library for facial analysis and recognition. The application provides a simple graphical user interface (GUI) built with Tkinter, allowing users to capture facial images and perform real-time facial recognition.
Features

    Graphical User Interface (GUI):
        A Tkinter-based interface for an intuitive user experience.
        Buttons to start image capture and initiate facial recognition.

    Image Capture:
        Uses OpenCV to capture frames from a webcam.
        Displays frames in real-time with FPS (Frames Per Second) overlay.
        Allows users to save facial images by pressing the spacebar, prompting for the user’s name for organized storage.

    Facial Recognition:
        Employs DeepFace to perform real-time facial recognition.
        Compares live video frames against stored facial images in a local database.
        Supports the VGG-Face model for facial recognition.

    Multithreading Support:
        Ensures a smooth user experience by running the GUI, image capture, and recognition processes on separate threads.

    Database Management:
        Automatically creates a local db directory to store user images.
        Images are saved with user-provided names for easy identification.
