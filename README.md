# PiHome

**A Smart Home System Miniature Model**

PiHome is a functional smart home prototype designed to simulate key automation features like door control and lighting
management. Built with a Raspberry Pi as the main controller, it integrates hardware components and a user-friendly GUI
developed using Python's Tkinter library.

This project demonstrates the seamless interaction between physical controls and digital interfaces, showcasing the
potential of smart home technologies in improving convenience, safety, and energy efficiency.

---

## Features

- **Door Automation**: Control doors using a servo motor via the GUI or physical buttons.
- **Smart Lighting**: Manage LED lights through on-screen controls or physical buttons.
- **Real-Time Synchronization**: Ensure smooth operation between GUI and physical components.
- **User-Friendly GUI**: Intuitive interface for controlling devices, designed with Tkinter.
- **Modular Design**: Easily expandable to include additional smart home features in the future.

---

## Project Components

### **Hardware**

- Raspberry Pi (Main controller)
- Servo Motor (Door control)
- LEDs and Resistors (Lighting management)
- Push Buttons (Physical controls)
- Breadboard and Jumper Wires (Connections)

### **Software**

- **Python**: Logic implementation and GPIO control.
- **Tkinter**: GUI development.
- **GPIO Library**: Interfacing with Raspberry Pi hardware.

---

## Getting Started

### **Prerequisites**

- Raspberry Pi set up with Raspbian OS.
- Python 3 installed on the Raspberry Pi.
- Necessary hardware components connected to the GPIO pins.

### **Setup Instructions**

1. Clone the repository:
   ```bash
   git clone https://github.com/ralphmarondev/pi-home.git
   cd pi-home
   ```
2. Install required Python libraries:
   ```bash
   pip install tkinter RPi.GPIO
   ```
3. Run the program:
   ```bash
   python3 main.py
   ```

---

## How It Works

- Use the **Tkinter GUI** to toggle door and lighting controls.
- Alternatively, press the physical buttons connected to the Raspberry Pi for manual control.
- All actions are synchronized, ensuring seamless operation between GUI and hardware.

---

## Future Enhancements

- Integration of sensors for enhanced automation (e.g., motion sensors, temperature sensors).
- Remote control functionality using a web or mobile app.
- Voice commands with speech recognition.
- Energy monitoring and efficiency tracking.

---

## About the Developer

Hi! I'm Ralph Maron A. Eda, a 4th-year computer engineering student with a passion for creating innovative systems that blend
hardware and software seamlessly. PiHome is part of my capstone project for Embedded Systems 2 and is a miniature
version of my thesis project.

I enjoy tackling challenges in automation and IoT, and PiHome reflects my commitment to designing practical and
efficient solutions for real-world needs. If you have any feedback or suggestions, feel free to reach out!

---

## License

This project is licensed under the [MIT License](LICENSE.txt).