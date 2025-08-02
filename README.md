# Turtle Crossing Game

A fun arcade-style game where a turtle tries to cross a busy road while avoiding moving cars. Built with Python's Turtle graphics library.

## Features

- **Progressive Difficulty**: Cars move faster as you advance through levels
- **Collision Detection**: Game ends when turtle hits a car
- **Level System**: Each successful crossing increases the level
- **Continuous Gameplay**: Cars spawn continuously from the right side
- **Score Tracking**: Real-time level display
- **Simple Controls**: One-key control for easy gameplay

## Game Rules

- Use the **Up Arrow** key to move the turtle forward
- Avoid all moving cars coming from the right
- Reach the top of the screen (finish line) to advance to the next level
- Each level increases car speed, making the game more challenging
- Game ends if the turtle collides with any car

## Requirements

- Python 3.x
- turtle (built-in Python module)

## Project Structure

```
turtle-crossing/
│
├── main.py          # Main game loop and collision detection
├── player.py        # Player (turtle) class with movement logic
├── car_manager.py   # Car generation and movement system
└── scoreboard.py    # Level tracking and game over display
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/turtle-crossing-game.git
```

2. Navigate to the project directory:
```bash
cd turtle-crossing-game
```

3. Make sure you have all required files:
   - `main.py` (main game file)
   - `player.py` (turtle player logic)
   - `car_manager.py` (car spawning and movement)
   - `scoreboard.py` (level management)

## Usage

Run the main game file:
```bash
python main.py
```

### Controls
- **↑ Arrow Key**: Move turtle up/forward
- **Click anywhere**: Exit game after game over

## Game Specifications

- **Screen Size**: 600x600 pixels
- **Finish Line**: Y-coordinate 280
- **Collision Distance**: 20 pixels
- **Game Speed**: Updates every 0.1 seconds
- **Car Generation**: Random car spawning from right side
- **Level Progression**: Automatic level increase upon reaching finish line

## Gameplay Mechanics

1. **Player Movement**: Turtle moves vertically up the screen
2. **Car Traffic**: Cars move horizontally from right to left
3. **Level System**: Each level increases car speed
4. **Reset Mechanism**: Player returns to start position after each level
5. **Game Over**: Collision with any car ends the game


## Future Enhancements

- [ ] Add sound effects for collisions and level completion
- [ ] Implement high score system
- [ ] Add different car colors and sizes
- [ ] Create power-ups (slow motion, invincibility)
- [ ] Add background graphics and animations
- [ ] Implement pause functionality
- [ ] Add multiple lanes with different speeds

## Contributing

Feel free to fork this project and submit pull requests for improvements or new features.


## Acknowledgments

Inspired by the classic Frogger arcade game. Built as part of learning Python game development with Turtle graphics.
