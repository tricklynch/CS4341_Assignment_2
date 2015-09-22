import argparse
import os
import random
import sys

def main():
    # Take in the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "puzzle", type=int, help="Which puzzle it is solving (1, 2, or 3)"
    )
    parser.add_argument(
        "file", help="The name of the file it should read in that contains the puzzle information."
    )
    parser.add_argument(
        "time", type=int, help="How many seconds it has to work on a solution"
    )
    parser.add_argument(
        "-p", "--population", type=int, help="The size of the population"
    )
    parser.add_argument(
        "-e", "--elitism", type=int, help="The number of elite clones between generations"
    )
    parser.add_argument(
        "-c", "--culling", type=int, help="The number of members to cull between generations"
    )
    parser.add_argument(
        "-t", "--trials", type=int, help="The number of trials/generations to run"
    )
    parser.add_argument(
        "-r", "--rate", type=float, help="The mutation rate/chance"
    )
    args = parser.parse_args()

    # Seed the rng
    seed = os.urandom(16)
    random.seed(seed)

    # Add the puzzles directory to the path
    sys.path.append("puzzles")
    # A string to represent the name of the file of the puzzle we are solving
    puzzle = "puzzle" + str(args.puzzle)
    try:
        # Import the puzzle to be solved
        puzzle_package = __import__(puzzle)
    except ImportError:
        print("That is not a valid puzzle number.")
        sys.exit(1)
    # Run the main function within the puzzle
    puzzle_package.main(
        puzzle=args.puzzle,
        file=args.file,
        time=args.time,
        population=args.population,
        elitism=args.elitism,
        culling=args.culling,
        trials=args.trials,
        rate=args.rate
    )

if __name__ == "__main__":
    main()
