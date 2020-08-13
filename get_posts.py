import requests, json
from argparse import ArgumentParser

def cmdline_args():
    parser = ArgumentParser(description="Retrieve posts from https://jsonplaceholder.typicode.com/posts")
    parser.add_argument(
        "--start",
        type=int,
        help="Specify the beginning of the posts range",
    )
    parser.add_argument(
        "--end",
        type=int,
        help="Specify the end of the posts range",
    )
    parser.add_argument(
        "--out",
        help="Name of file for output",
    )
    return(parser.parse_args())

def api_call(args):
    get_url = 'https://jsonplaceholder.typicode.com/posts'
    params = dict()
    if args.start:
        params["_start"] = args.start
    if args.end:
        params["_end"] = args.end
    response = requests.get(get_url, params=params)
    data = response.json()
    return data

def data_output(data, filename):
    if filename is None:
        print(data)
    else:
        with open(filename, 'w') as outfile:
            json.dump(data, outfile)

if __name__ == '__main__':
    args = cmdline_args()
    data = api_call(args)
    data_output(data, args.out)


    
        
        



