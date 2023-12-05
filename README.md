# Game Theory Visualization

This repository contains scripts for visualizing interesting game theory concepts using Python and matplotlib. The implemented games include the Bertrand model, Cournot game, and Best Response Functions.

## Table of Contents

- [Introduction](#introduction)
- [Games](#games)
  - [Bertrand Model](#bertrand-model)
  - [Cournot Game](#cournot-game)
  - [Best Response Functions](#best-response-functions)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)

## Introduction

Game theory is a branch of mathematics and economics that studies strategic interactions among rational decision-makers. This repository provides visualizations for key game theory concepts to enhance understanding and insight.

## Games

### Bertrand Model

The Bertrand model is a game theory model of competition between firms that assumes firms set prices rather than quantities. It explores the pricing strategies and equilibrium in a competitive market.

### Cournot Game

The Cournot game models competition between firms that simultaneously choose quantities of a homogeneous product to produce. It investigates the Nash equilibrium in a duopoly setting.

### Best Response Functions

Best Response Functions (BRF) are employed in various game theory scenarios to find optimal strategies for players. The visualization here focuses on illustrating the best response surfaces for different player actions.

## Getting Started

To run the visualizations, you need Python and the matplotlib library installed. Clone this repository to your local machine:

```bash
git clone https://github.com/BenKurrek/game-theory-visualization.git
```

Navigate to the project directory:

```bash
cd game-theory-visualization
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

The primary entry point is the main.py file. You can specify the game type and additional parameters using command-line arguments.

```bash
python3 main.py <game> [--a <value>] [--c <value>]
```

Replace <game> with the desired game type (bertrand, cournot, brf). Optionally, you can set parameters a and c for the specific game.


## Examples

Here are some examples of how to use the visualization scripts:

```bash
# Bertrand model with a=5 and c=4
python3 main.py bertrand --a 5 --c 4

# Cournot game with a=50 and c=1
python3 main.py cournot --a 50 --c 1

# Best Response Functions with c=100
python3 main.py brf --c 100
```

## Contributing

Contributions are welcome! If you have ideas for improvements or find any issues, feel free to open an issue or submit a pull request.