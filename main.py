from boyer_moore import BoyerMoore
import time

if __name__ == '__main__':

    txt3 = "hi"
    pat3 = "hi"
    test3 = BoyerMoore(pat3, txt3)
    start3 = time.perf_counter()
    search_result3 = test3.search()
    end3 = time.perf_counter()
    print(f"Time taken: {(end3 - start3) * 10 ** 3}ms - best case")
    print("")

    txt1 = "hello hello"
    pat1 = "hello"
    test1 = BoyerMoore(pat1, txt1)
    start1 = time.perf_counter()
    search_result1 = test1.search()
    end1 = time.perf_counter()
    print(f"Time taken: {(end1 - start1) * 10 ** 3:f}ms - average case")
    print("")

    txt2 = "SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS"
    pat2 = "SSSS"
    test2 = BoyerMoore(pat2, txt2)
    start2 = time.perf_counter()
    search_result2 = test2.search()
    end2 = time.perf_counter()
    print(f"Time taken: {(end2 - start2) * 10 ** 3}ms - worst case")
    print("")
