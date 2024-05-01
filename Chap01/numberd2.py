     1	from crossLine import main
     2	import sys
     3	
     4	# 引数にint型の回数が指定されていることを確認
     5	if len(sys.argv) <= 1:
     6	    count = int(input("count - >"))
     7	elif sys.argv[2].isdigit():
     8	    count = int(sys.argv[2])
     9	else:
    10	    count = int(input("count - >"))
    11	
    12	
    13	if __name__ == '__main__':
    14	    for i in range(count):
    15	        main()
    16	        print("Done!")
