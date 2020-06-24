# Import modules
import sys
import argparse
import license

if __name__ == '__main__':
    # Check license
    license.check_status()

    # Setup of argparse for script arguments
    class licenseAction(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            print("License status: %s" % license.message())
            sys.exit()


    parser = argparse.ArgumentParser(description="Converts bam into bigwig files. "
                                                 "Note: must have deeptools in path",
                                     prog="bamtobigwig.py")
    optional = parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    required.add_argument("-bam", type=str, default=None, metavar="BAM",
                          help="path to bam file for conversion", required=True)
    optional.add_argument("-str", action='store_true', help="for stranded bam, will give split bigwigs")
    optional.add_argument("-t", "--threads", nargs='?', const=1, type=int, default=1, metavar="",
                          help='number of threads to utilize (default = 1)')
    optional.add_argument("-l", "--license", action=licenseAction, metavar="", nargs=0,
                          help='show license status and exit')
    parser._action_groups.append(optional)
    args = parser.parse_args()

    if args.str:
        license.b2bw_strand(args.bam, args.threads)
    else:
        license.b2bw_unstrand(args.bam, args.threads)
