import argparse
import logging
#import os
#import pathlib
import sys
import uvicorn

logger = logging.getLogger(__file__)

def parse_args():
    """Parses command line args.

    """
    parser = argparse.ArgumentParser(
        description="Run the Tower of Hanoi FastAPI web-service",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-d', '--dev', action='store_true',
                        help='Run FastAPI webservice in developer mode')
    parser.add_argument('-n', '--network', action='store_true',
                        help='Enable network access (default: local computer access only')
    parser.add_argument('-p', '--port', type=int,
                        help='Enable network access (default: local computer access only')
    args = parser.parse_args()
    return args, parser


def main():
    args, _ = parse_args()
    uvicorn_args={}
    if args.network: uvicorn_args['host']='0.0.0.0'
    if args.dev:
        uvicorn_args['reload']=True
        uvicorn_args['log_level']='debug'
    if args.port: uvicorn_args['port']=args.port

    logger.info(f"Running web service with options: {uvicorn_args}")
    return uvicorn.run("toh.main:app",**uvicorn_args)

if __name__ == "__main__":
    sys.exit(main())
