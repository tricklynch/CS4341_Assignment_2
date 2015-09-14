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
        "filename", help="The name of the file it should read in that contains the puzzle information."
    )
    parser.add_argument(
        "time", type=int, help="How many seconds it has to work on a solution"
    )
    parser.add_argument(
        "-p", "--population", type=int, help="The size of the population"
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
    puzzle_package.main()

if __name__ == "__main__":
    main()
