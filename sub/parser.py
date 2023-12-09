import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--file', help="chose the video file you wish to sub")
    parser.add_argument(
        '-l', '--language', help="choose the language you wish to sub in")
    parser.add_argument(
        '-p', '--path', help="path where you want the subbed video to be saved")

    args = parser.parse_args()

    return args
