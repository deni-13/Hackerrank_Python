def maxmin(arr):
    enk=min(arr)
    enb=max(arr)
    toplam=sum(arr)

    print(toplam-enb,toplam-enk)

maxmin([1,2,3,4,5])