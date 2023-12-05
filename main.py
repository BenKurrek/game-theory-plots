import argparse
from src.bertrand import bertrand_game
from src.cournot import cournot_game
from src.relationship_brf import brf_game

def main():
    parser = argparse.ArgumentParser(description='Game Theory Visualization')
    parser.add_argument('game', choices=['bertrand', 'cournot', 'brf'], help='Type of game to visualize')
    parser.add_argument('--a', type=float, help='Parameter a')
    parser.add_argument('--c', type=float, help='Parameter c')
    parser.add_argument('--animate', type=str, help='Parameter to animate the Cournot game')
    
    args = parser.parse_args()

    if args.game == 'bertrand':
        bertrand_game(args.a, args.c, args.animate)
    elif args.game == 'cournot':
        cournot_game(args.a, args.c, args.animate)
    elif args.game == 'brf':
        brf_game(args.c)

if __name__ == '__main__':
    main()
