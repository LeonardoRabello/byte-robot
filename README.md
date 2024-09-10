# Byte - Robot Controlled by Raspberry Pi Zero 2W with Gemini Communication

**Byte** is a robot controlled by a Raspberry Pi Zero 2W, designed for capturing audio and video, processing data via the Gemini protocol, and providing real-time visual and audio feedback. It utilizes a 24x24 LED matrix for display and can convert speech to text, and vice versa.

## Features

- **Raspberry Pi Zero 2W** as the central processing unit.
- **Pi Camera Zero** for video capture.
- **9 MAX7219 LED matrices**, each with 8x8 LEDs, forming a 24x24 LED grid for visual feedback.
- **2 L298N H-bridge motor drivers** to control four DC motors.
- **4 DC motors** with the following specifications:
  - Metal shaft and 4 metal gears.
  - Reduction ratio: 1:90.
  - Voltage input: 3V-6V.
  - Output speed: 110 RPM.
- **Microphone** for audio input, and **speaker** for audio output.
- **Audio and Video Processing**:
  - Byte captures audio and video simultaneously.
  - The audio is converted to text and sent as input via the Gemini protocol.
  - Gemini processes the audio and video, returning a text output that Byte converts back to audio for playback through the speaker.
- **Gemini protocol** for communication and processing.

## Requirements

- Raspberry Pi Zero 2W
- Pi Camera Zero
- MAX7219 LED matrix drivers (9 units)
- L298N H-bridge motor drivers (2 units)
- 4 DC motors (3V-6V, 110 RPM)
- Microphone and speaker

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/LeonardoRabello/byte-robot.git
