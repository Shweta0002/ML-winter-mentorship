def print_formatted(number):
    # your code goes here
    w = len(str(bin(number)).replace('0b',''))

    for num in range(1, number+1):

        dec = str(num)
        oc_ = str(oct(num)).replace('0o','')
        he_ = str(hex(num)).replace('0x','').upper()
        bi_ = str(bin(num)).replace('0b','')
        print(dec.rjust(w), oc_.rjust(w), he_.rjust(w), bi_.rjust(w), sep=' ')
     
