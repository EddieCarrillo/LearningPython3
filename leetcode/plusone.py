class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1 # plus one
        sig_idx = len(digits) - 1
        #You only need to proceed if there is a carry
        while carry > 0 and sig_idx >= 0:
            remainder = (digits[sig_idx] + carry) % 10
            carry = (digits[sig_idx] + carry) // 10
            digits[sig_idx] = remainder
            sig_idx -= 1
        if carry > 0:
            digits.insert(0, 1)
        return digits
