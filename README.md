🚀 Asteroid Splitter
Asteroid Splitter is a fast-paced 2D arcade game built with Python and Pygame where the player must manage a growing field of asteroids. Asteroids enter the screen from the edges and can be split into smaller ones upon impact. The objective is to keep the screen manageable while experiencing chaotic asteroid fragmentation!

🎮 Features
Dynamic asteroid spawning at random screen edges.

Realistic splitting behavior when asteroids are destroyed.

Object-oriented architecture for clean and reusable game entities.

Built using Pygame's sprite system for easy integration and collision management.


🧠 How It Works
The game uses a base class CircleShape to define all circular game entities with position, velocity, and radius.

Asteroid inherits from CircleShape and can split() into smaller pieces with randomized directions when destroyed.

AsteroidField manages spawning new asteroids from random edges with randomized movement vectors.

🛠️ Requirements
Python 3.x

Pygame (pip install pygame)

📦 File Structure
bash
Copy
Edit
.
├── asteroid.py         # Defines the Asteroid class and its split behavior
├── asteroidfield.py    # Handles the logic for spawning and updating asteroids
├── circleshape.py      # Base class for circular game objects
├── constants.py        # (You should define game constants here)
└── main.py             # (Your main game loop should go here)

🕹️ Controls
Player controls (WASD movement, SPACE for shooting)

Detect collisions to trigger split() on asteroids

🚧 To Do
 Add player spaceship and controls

 Implement shooting and asteroid destruction

 Add score tracking and game-over logic

 Add sound effects and polish visuals

 Optimize collision detection for performance

📃 License
MIT License (or your preferred open-source license)

🙌 Credits
Developed by [RoadtoFire]. Powered by Python and Pygame.
