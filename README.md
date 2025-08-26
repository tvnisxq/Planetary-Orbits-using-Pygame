# Planetary Orbits Using Pygame


A beautiful simulation of planetary orbital motion built with Python and Pygame. This project demonstrates gravitational interactions between celestial bodies using real physics principles.

## Features

- Realistic gravitational physics simulation
- Interactive celestial body creation
- Zoom functionality to observe orbital details
- Accurate position updates based on gravitational forces
- Customizable planetary properties (mass, radius, velocity, color)

## Requirements

- Python 3.10+
- Pygame 2.6.1
- Math module (built-in)

## Installation

1. Clone this repository
2. Set up a virtual environment (optional but recommended):
```sh
python -m venv planetary_pygame_venv
source planetary_pygame_venv/Scripts/activate  # On Windows use: planetary_pygame_venv\Scripts\activate
```
3. Install required packages:
```sh
pip install pygame
```

## Usage

Run the simulation using:
```sh
python src/main.py
```

### Controls

- **Left Mouse Click**: Create new celestial bodies
- **Zoom**: Toggle between normal and zoomed view

## How It Works

The simulation uses Newton's law of universal gravitation to calculate the forces between celestial bodies. Each body's position is updated based on:

- Gravitational constant (G = 6.67430e-11)
- Mass of interacting bodies
- Distance between bodies
- Current velocity vectors

The [`Body`](src/main.py) class handles all celestial body properties and physics calculations.

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is licensed under the included license file.

## Acknowledgments

- Pygame community for the excellent graphics library
- Physics equations based on Newton's laws of motion and gravitation
