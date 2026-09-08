import secrets,time
from bit import Key
from bit.format import bytes_to_wif

output_file = "found.txt"

def random_hex_between(start_hex: str, end_hex: str) -> str:
    start = int(start_hex, 16)
    end = int(end_hex, 16)

    diff = end - start + 1
    rand_int = secrets.randbelow(diff) + start
    return hex(rand_int)[2:].zfill(64)


def private_to_legacy_compressed(priv_hex: str) -> str:

    priv_bytes = bytes.fromhex(priv_hex)
    wif_compressed = bytes_to_wif(priv_bytes, compressed=True)
    key_compressed = Key(wif_compressed)
    address=key_compressed.address
    return address


# ---- MAIN ----
def checking(privateKey,targetaddress):
    addr = private_to_legacy_compressed(privateKey)
    if addr == targetaddress:
        print(f'\nPrivate Key: {privateKey}, Address: {addr}')
        result_string = f'Private Key: {privateKey}, Address: {addr}\n'
        with open(output_file, 'a') as f:
            f.write(result_string)

#-------------------------------------------------------------------------------


print(
      f"*******************************************************************************************************\n"
      f"Save to             : {output_file:<}")
print("BITCOIN PUZZLE SOLVER")
time.sleep(1)
print("DON'T WORRY, THIS CODE IS NOT USING YOUR COMPUTING POWER FOR ME.")
print("DONATION BTC = bc1qjqmgkuu4qefgwpdq24dvmz60pvjnn7egvc4zke   if you get lucky , give me a tip please ..")
time.sleep(1)
print("Scanning starts...")
st=int(time.time())
hex_count = 0

while True:
    i=random_hex_between("0000000000000000000000000000000000000000000000400000000000000000","00000000000000000000000000000000000000000000007fffffffffffffffff")
    checking(i,"1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU")

    i=random_hex_between("0000000000000000000000000000000000000000000000800000000000000000","0000000000000000000000000000000000000000000000ffffffffffffffffff")
    checking(i,"1JTK7s9YVYywfm5XUH7RNhHJH1LshCaRFR")
        
    i=random_hex_between("0000000000000000000000000000000000000000000001000000000000000000","0000000000000000000000000000000000000000000001ffffffffffffffffff")
    checking(i,"12VVRNPi4SJqUTsp6FmqDqY5sGosDtysn4")
        
    i=random_hex_between("0000000000000000000000000000000000000000000002000000000000000000","0000000000000000000000000000000000000000000003ffffffffffffffffff")
    checking(i,"1FWGcVDK3JGzCC3WtkYetULPszMaK2Jksv")
        
    i=random_hex_between("0000000000000000000000000000000000000000000008000000000000000000","000000000000000000000000000000000000000000000fffffffffffffffffff")
    checking(i,"1DJh2eHFYQfACPmrvpyWc8MSTYKh7w9eRF")
        
    i=random_hex_between("0000000000000000000000000000000000000000000010000000000000000000","000000000000000000000000000000000000000000001fffffffffffffffffff")
    checking(i,"1Bxk4CQdqL9p22JEtDfdXMsng1XacifUtE")
        
    i=random_hex_between("0000000000000000000000000000000000000000000020000000000000000000","000000000000000000000000000000000000000000003fffffffffffffffffff")
    checking(i,"15qF6X51huDjqTmF9BJgxXdt1xcj46Jmhb")
        
    i=random_hex_between("0000000000000000000000000000000000000000000040000000000000000000","000000000000000000000000000000000000000000007fffffffffffffffffff")
    checking(i,"1ARk8HWJMn8js8tQmGUJeQHjSE7KRkn2t8")
        
    i=random_hex_between("0000000000000000000000000000000000000000000100000000000000000000","00000000000000000000000000000000000000000001ffffffffffffffffffff")
    checking(i,"15qsCm78whspNQFydGJQk5rexzxTQopnHZ")
        
    i=random_hex_between("0000000000000000000000000000000000000000000200000000000000000000","00000000000000000000000000000000000000000003ffffffffffffffffffff")
    checking(i,"13zYrYhhJxp6Ui1VV7pqa5WDhNWM45ARAC")
        
    i=random_hex_between("0000000000000000000000000000000000000000000400000000000000000000","00000000000000000000000000000000000000000007ffffffffffffffffffff")
    checking(i,"14MdEb4eFcT3MVG5sPFG4jGLuHJSnt1Dk2")
        
    i=random_hex_between("0000000000000000000000000000000000000000000800000000000000000000","0000000000000000000000000000000000000000000fffffffffffffffffffff")
    checking(i,"1CMq3SvFcVEcpLMuuH8PUcNiqsK1oicG2D")
        
    i=random_hex_between("0000000000000000000000000000000000000000002000000000000000000000","0000000000000000000000000000000000000000003fffffffffffffffffffff")
    checking(i,"1K3x5L6G57Y494fDqBfrojD28UJv4s5JcK")
        
    i=random_hex_between("0000000000000000000000000000000000000000004000000000000000000000","0000000000000000000000000000000000000000007fffffffffffffffffffff")
    checking(i,"1PxH3K1Shdjb7gSEoTX7UPDZ6SH4qGPrvq")
        
    i=random_hex_between("0000000000000000000000000000000000000000008000000000000000000000","000000000000000000000000000000000000000000ffffffffffffffffffffff")
    checking(i,"16AbnZjZZipwHMkYKBSfswGWKDmXHjEpSf")
        
    i=random_hex_between("0000000000000000000000000000000000000000010000000000000000000000","000000000000000000000000000000000000000001ffffffffffffffffffffff")
    checking(i,"19QciEHbGVNY4hrhfKXmcBBCrJSBZ6TaVt")
        
    i=random_hex_between("0000000000000000000000000000000000000000040000000000000000000000","000000000000000000000000000000000000000007ffffffffffffffffffffff")
    checking(i,"1EzVHtmbN4fs4MiNk3ppEnKKhsmXYJ4s74")
        
    i=random_hex_between("0000000000000000000000000000000000000000080000000000000000000000","00000000000000000000000000000000000000000fffffffffffffffffffffff")
    checking(i,"1AE8NzzgKE7Yhz7BWtAcAAxiFMbPo82NB5")
        
    i=random_hex_between("0000000000000000000000000000000000000000100000000000000000000000","00000000000000000000000000000000000000001fffffffffffffffffffffff")
    checking(i,"17Q7tuG2JwFFU9rXVj3uZqRtioH3mx2Jad")
        
    i=random_hex_between("0000000000000000000000000000000000000000200000000000000000000000","00000000000000000000000000000000000000003fffffffffffffffffffffff")
    checking(i,"1K6xGMUbs6ZTXBnhw1pippqwK6wjBWtNpL")
        
    i=random_hex_between("0000000000000000000000000000000000000000800000000000000000000000","0000000000000000000000000000000000000000ffffffffffffffffffffffff")
    checking(i,"15ANYzzCp5BFHcCnVFzXqyibpzgPLWaD8b")
        
    i=random_hex_between("0000000000000000000000000000000000000001000000000000000000000000","0000000000000000000000000000000000000001ffffffffffffffffffffffff")
    checking(i,"18ywPwj39nGjqBrQJSzZVq2izR12MDpDr8")
        
    i=random_hex_between("0000000000000000000000000000000000000002000000000000000000000000","0000000000000000000000000000000000000003ffffffffffffffffffffffff")
    checking(i,"1CaBVPrwUxbQYYswu32w7Mj4HR4maNoJSX")
        
    i=random_hex_between("0000000000000000000000000000000000000004000000000000000000000000","0000000000000000000000000000000000000007ffffffffffffffffffffffff")
    checking(i,"1JWnE6p6UN7ZJBN7TtcbNDoRcjFtuDWoNL")
        
    i=random_hex_between("0000000000000000000000000000000000000010000000000000000000000000","000000000000000000000000000000000000001fffffffffffffffffffffffff")
    checking(i,"1CKCVdbDJasYmhswB6HKZHEAnNaDpK7W4n")
        
    i=random_hex_between("0000000000000000000000000000000000000020000000000000000000000000","000000000000000000000000000000000000003fffffffffffffffffffffffff")
    checking(i,"1PXv28YxmYMaB8zxrKeZBW8dt2HK7RkRPX")
        
    i=random_hex_between("0000000000000000000000000000000000000040000000000000000000000000","000000000000000000000000000000000000007fffffffffffffffffffffffff")
    checking(i,"1AcAmB6jmtU6AiEcXkmiNE9TNVPsj9DULf")
        
    i=random_hex_between("0000000000000000000000000000000000000080000000000000000000000000","00000000000000000000000000000000000000ffffffffffffffffffffffffff")
    checking(i,"1EQJvpsmhazYCcKX5Au6AZmZKRnzarMVZu")
     
    i=random_hex_between("0000000000000000000000000000000000000200000000000000000000000000","00000000000000000000000000000000000003ffffffffffffffffffffffffff")
    checking(i,"18KsfuHuzQaBTNLASyj15hy4LuqPUo1FNB")
        
    i=random_hex_between("0000000000000000000000000000000000000400000000000000000000000000","00000000000000000000000000000000000007ffffffffffffffffffffffffff")
    checking(i,"15EJFC5ZTs9nhsdvSUeBXjLAuYq3SWaxTc")
        
    i=random_hex_between("0000000000000000000000000000000000000800000000000000000000000000","0000000000000000000000000000000000000fffffffffffffffffffffffffff")
    checking(i,"1HB1iKUqeffnVsvQsbpC6dNi1XKbyNuqao")
        
    i=random_hex_between("0000000000000000000000000000000000001000000000000000000000000000","0000000000000000000000000000000000001fffffffffffffffffffffffffff")
    checking(i,"1GvgAXVCbA8FBjXfWiAms4ytFeJcKsoyhL")
        
    i=random_hex_between("0000000000000000000000000000000000004000000000000000000000000000","0000000000000000000000000000000000007fffffffffffffffffffffffffff")
    checking(i,"1824ZJQ7nKJ9QFTRBqn7z7dHV5EGpzUpH3")
        
    i=random_hex_between("0000000000000000000000000000000000008000000000000000000000000000","000000000000000000000000000000000000ffffffffffffffffffffffffffff")
    checking(i,"18A7NA9FTsnJxWgkoFfPAFbQzuQxpRtCos")
        
    i=random_hex_between("0000000000000000000000000000000000010000000000000000000000000000","000000000000000000000000000000000001ffffffffffffffffffffffffffff")
    checking(i,"1NeGn21dUDDeqFQ63xb2SpgUuXuBLA4WT4")
        
    i=random_hex_between("0000000000000000000000000000000000020000000000000000000000000000","000000000000000000000000000000000003ffffffffffffffffffffffffffff")
    checking(i,"174SNxfqpdMGYy5YQcfLbSTK3MRNZEePoy")
        
    i=random_hex_between("0000000000000000000000000000000000080000000000000000000000000000","00000000000000000000000000000000000fffffffffffffffffffffffffffff")
    checking(i,"1MnJ6hdhvK37VLmqcdEwqC3iFxyWH2PHUV")
        
    i=random_hex_between("0000000000000000000000000000000000100000000000000000000000000000","00000000000000000000000000000000001fffffffffffffffffffffffffffff")
    checking(i,"1KNRfGWw7Q9Rmwsc6NT5zsdvEb9M2Wkj5Z")
        
    i=random_hex_between("0000000000000000000000000000000000200000000000000000000000000000","00000000000000000000000000000000003fffffffffffffffffffffffffffff")
    checking(i,"1PJZPzvGX19a7twf5HyD2VvNiPdHLzm9F6")
        
    i=random_hex_between("0000000000000000000000000000000000400000000000000000000000000000","00000000000000000000000000000000007fffffffffffffffffffffffffffff")
    checking(i,"1GuBBhf61rnvRe4K8zu8vdQB3kHzwFqSy7")
        
    i=random_hex_between("0000000000000000000000000000000001000000000000000000000000000000","0000000000000000000000000000000001ffffffffffffffffffffffffffffff")
    checking(i,"1GDSuiThEV64c166LUFC9uDcVdGjqkxKyh")
        
    i=random_hex_between("0000000000000000000000000000000002000000000000000000000000000000","0000000000000000000000000000000003ffffffffffffffffffffffffffffff")
    checking(i,"1Me3ASYt5JCTAK2XaC32RMeH34PdprrfDx")
        
    i=random_hex_between("0000000000000000000000000000000004000000000000000000000000000000","0000000000000000000000000000000007ffffffffffffffffffffffffffffff")
    checking(i,"1CdufMQL892A69KXgv6UNBD17ywWqYpKut")
        
    i=random_hex_between("0000000000000000000000000000000008000000000000000000000000000000","000000000000000000000000000000000fffffffffffffffffffffffffffffff")
    checking(i,"1BkkGsX9ZM6iwL3zbqs7HWBV7SvosR6m8N")
        
    i=random_hex_between("0000000000000000000000000000000020000000000000000000000000000000","000000000000000000000000000000003fffffffffffffffffffffffffffffff")
    checking(i,"1AWCLZAjKbV1P7AHvaPNCKiB7ZWVDMxFiz")
    
    i=random_hex_between("0000000000000000000000000000000040000000000000000000000000000000","000000000000000000000000000000007fffffffffffffffffffffffffffffff")
    checking(i,"1G6EFyBRU86sThN3SSt3GrHu1sA7w7nzi4")    

    i=random_hex_between("0000000000000000000000000000000080000000000000000000000000000000","00000000000000000000000000000000ffffffffffffffffffffffffffffffff")
    checking(i,"1MZ2L1gFrCtkkn6DnTT2e4PFUTHw9gNwaj")
        
    i=random_hex_between("0000000000000000000000000000000100000000000000000000000000000000","00000000000000000000000000000001ffffffffffffffffffffffffffffffff")
    checking(i,"1Hz3uv3nNZzBVMXLGadCucgjiCs5W9vaGz")
        
    i=random_hex_between("0000000000000000000000000000000400000000000000000000000000000000","00000000000000000000000000000007ffffffffffffffffffffffffffffffff")
    checking(i,"16zRPnT8znwq42q7XeMkZUhb1bKqgRogyy")
        
    i=random_hex_between("0000000000000000000000000000000800000000000000000000000000000000","0000000000000000000000000000000fffffffffffffffffffffffffffffffff")
    checking(i,"1KrU4dHE5WrW8rhWDsTRjR21r8t3dsrS3R")
        
    i=random_hex_between("0000000000000000000000000000001000000000000000000000000000000000","0000000000000000000000000000001fffffffffffffffffffffffffffffffff")
    checking(i,"17uDfp5r4n441xkgLFmhNoSW1KWp6xVLD")
            
    i=random_hex_between("0000000000000000000000000000002000000000000000000000000000000000","0000000000000000000000000000003fffffffffffffffffffffffffffffffff")
    checking(i,"13A3JrvXmvg5w9XGvyyR4JEJqiLz8ZySY3")
            
    i=random_hex_between("0000000000000000000000000000008000000000000000000000000000000000","000000000000000000000000000000ffffffffffffffffffffffffffffffffff")
    checking(i,"1UDHPdovvR985NrWSkdWQDEQ1xuRiTALq")
            
    i=random_hex_between("0000000000000000000000000000010000000000000000000000000000000000","000000000000000000000000000001ffffffffffffffffffffffffffffffffff")
    checking(i,"15nf31J46iLuK1ZkTnqHo7WgN5cARFK3RA")
            
    i=random_hex_between("0000000000000000000000000000020000000000000000000000000000000000","000000000000000000000000000003ffffffffffffffffffffffffffffffffff")
    checking(i,"1Ab4vzG6wEQBDNQM1B2bvUz4fqXXdFk2WT")
            
    i=random_hex_between("0000000000000000000000000000040000000000000000000000000000000000","000000000000000000000000000007ffffffffffffffffffffffffffffffffff")
    checking(i,"1Fz63c775VV9fNyj25d9Xfw3YHE6sKCxbt")
            
    i=random_hex_between("0000000000000000000000000000080000000000000000000000000000000000","00000000000000000000000000000fffffffffffffffffffffffffffffffffff")
    checking(i,"1QKBaU6WAeycb3DbKbLBkX7vJiaS8r42Xo")
            
    i=random_hex_between("0000000000000000000000000000100000000000000000000000000000000000","00000000000000000000000000001fffffffffffffffffffffffffffffffffff")
    checking(i,"1CD91Vm97mLQvXhrnoMChhJx4TP9MaQkJo")
            
    i=random_hex_between("0000000000000000000000000000200000000000000000000000000000000000","00000000000000000000000000003fffffffffffffffffffffffffffffffffff")
    checking(i,"15MnK2jXPqTMURX4xC3h4mAZxyCcaWWEDD")
            
    i=random_hex_between("0000000000000000000000000000400000000000000000000000000000000000","00000000000000000000000000007fffffffffffffffffffffffffffffffffff")
    checking(i,"13N66gCzWWHEZBxhVxG18P8wyjEWF9Yoi1")
            
    i=random_hex_between("0000000000000000000000000000800000000000000000000000000000000000","0000000000000000000000000000ffffffffffffffffffffffffffffffffffff")
    checking(i,"1NevxKDYuDcCh1ZMMi6ftmWwGrZKC6j7Ux")
            
    i=random_hex_between("0000000000000000000000000001000000000000000000000000000000000000","0000000000000000000000000001ffffffffffffffffffffffffffffffffffff")
    checking(i,"19GpszRNUej5yYqxXoLnbZWKew3KdVLkXg")
            
    i=random_hex_between("0000000000000000000000000002000000000000000000000000000000000000","0000000000000000000000000003ffffffffffffffffffffffffffffffffffff")
    checking(i,"1M7ipcdYHey2Y5RZM34MBbpugghmjaV89P")
            
    i=random_hex_between("0000000000000000000000000004000000000000000000000000000000000000","0000000000000000000000000007ffffffffffffffffffffffffffffffffffff")
    checking(i,"18aNhurEAJsw6BAgtANpexk5ob1aGTwSeL")
            
    i=random_hex_between("0000000000000000000000000008000000000000000000000000000000000000","000000000000000000000000000fffffffffffffffffffffffffffffffffffff")
    checking(i,"1FwZXt6EpRT7Fkndzv6K4b4DFoT4trbMrV")
            
    i=random_hex_between("0000000000000000000000000010000000000000000000000000000000000000","000000000000000000000000001fffffffffffffffffffffffffffffffffffff")
    checking(i,"1CXvTzR6qv8wJ7eprzUKeWxyGcHwDYP1i2")
            
    i=random_hex_between("0000000000000000000000000020000000000000000000000000000000000000","000000000000000000000000003fffffffffffffffffffffffffffffffffffff")
    checking(i,"1MUJSJYtGPVGkBCTqGspnxyHahpt5Te8jy")
            
    i=random_hex_between("0000000000000000000000000040000000000000000000000000000000000000","000000000000000000000000007fffffffffffffffffffffffffffffffffffff")
    checking(i,"13Q84TNNvgcL3HJiqQPvyBb9m4hxjS3jkV")
            
    i=random_hex_between("0000000000000000000000000080000000000000000000000000000000000000","00000000000000000000000000ffffffffffffffffffffffffffffffffffffff")
    checking(i,"1LuUHyrQr8PKSvbcY1v1PiuGuqFjWpDumN")
            
    i=random_hex_between("0000000000000000000000000100000000000000000000000000000000000000","00000000000000000000000001ffffffffffffffffffffffffffffffffffffff")
    checking(i,"18192XpzzdDi2K11QVHR7td2HcPS6Qs5vg")
            
    i=random_hex_between("0000000000000000000000000200000000000000000000000000000000000000","00000000000000000000000003ffffffffffffffffffffffffffffffffffffff")
    checking(i,"1NgVmsCCJaKLzGyKLFJfVequnFW9ZvnMLN")
            
    i=random_hex_between("0000000000000000000000000400000000000000000000000000000000000000","00000000000000000000000007ffffffffffffffffffffffffffffffffffffff")
    checking(i,"1AoeP37TmHdFh8uN72fu9AqgtLrUwcv2wJ")
            
    i=random_hex_between("0000000000000000000000000800000000000000000000000000000000000000","0000000000000000000000000fffffffffffffffffffffffffffffffffffffff")
    checking(i,"1FTpAbQa4h8trvhQXjXnmNhqdiGBd1oraE")
            
    i=random_hex_between("0000000000000000000000001000000000000000000000000000000000000000","0000000000000000000000001fffffffffffffffffffffffffffffffffffffff")
    checking(i,"14JHoRAdmJg3XR4RjMDh6Wed6ft6hzbQe9")
                
    i=random_hex_between("0000000000000000000000002000000000000000000000000000000000000000","0000000000000000000000003fffffffffffffffffffffffffffffffffffffff")
    checking(i,"19z6waranEf8CcP8FqNgdwUe1QRxvUNKBG")
                
    i=random_hex_between("0000000000000000000000004000000000000000000000000000000000000000","0000000000000000000000007fffffffffffffffffffffffffffffffffffffff")
    checking(i,"14u4nA5sugaswb6SZgn5av2vuChdMnD9E5")
                
    i=random_hex_between("0000000000000000000000008000000000000000000000000000000000000000","000000000000000000000000ffffffffffffffffffffffffffffffffffffffff")
    checking(i,"1NBC8uXJy1GiJ6drkiZa1WuKn51ps7EPTv")
    

    hex_count += 77
    if hex_count%77000==0:
        en=int(time.time())
        print("Total scanned = ",hex_count,f" || speed = {int(hex_count/(en-st))} keys per sec")

