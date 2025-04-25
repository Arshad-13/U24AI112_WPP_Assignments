# Decode the message:
# A message containing the letters from A-Z can be encoded into the numbers using the mapping
# A-> 1, B-> 2, C-> 3, ..., Z-> 26. To decode an encoded message, you need to group the digits
# and do the reverse mapping. You are required to display all the possible decoded messages.
# For example: "11106" can be decoded into:
# a. "AAJF" with the grouping (1 1 10 6)
# b. "KJF" with the grouping (11 10 6)

def decode(s):
    def helper(s, memo):
        if s in memo:
            return memo[s]
        if not s:
            return [""]
        res = []
        if s[0] != "0":
            res += [chr(64 + int(s[:1])) + item for item in helper(s[1:], memo)]
        if len(s) >= 2 and "10" <= s[:2] <= "26":
            res += [chr(64 + int(s[:2])) + item for item in helper(s[2:], memo)]
        memo[s] = res
        return res
    
    return helper(s, {})

decoded_messages = decode("11106")
print(decoded_messages)