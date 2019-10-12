import sys
import time

import tptp_parser

def main(argv):
    time_init = time.time_ns()

    ast = tptp_parser.parse(argv[1])
    time_afterparse = time.time_ns()
    
    # to string
    print('% to string:')
    print(ast.toString())

    print()
    print('% select specific child:')
    print(ast.child(0).toString())
    print(ast.child(0).ruleString())

    print()
    print('% iterate children:')
    for n in ast:
        print(n.toString())

    print()
    print('% dfs:')
    for n in tptp_parser.dfs(ast):
        print(n.toString(), n.ruleString())

    print()
    print('% dfs with filter:')
    for n in tptp_parser.filter(ast, tptp_parser.noderule_thf_binary_formula):
        print(n.toString(), n.ruleString())

    time_afterast = time.time_ns()

    print('{parse} parse[ms]'.format(
        parse=int((time_afterast-time_init)/1000000),
    ))

if __name__ == '__main__':
    main(sys.argv)
