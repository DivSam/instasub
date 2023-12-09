import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-g', '--generate', help="Generate subtitles for a video file", action="store_true")
    args = parser.parse_args()

    return args
