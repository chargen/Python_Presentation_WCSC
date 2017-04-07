#!/usr/bin/env python2

from pwn import *


context.log_level = "INFO"
log.debug("You don't see me")
context.log_level = "DEBUG"
log.debug("Started")
context.log_level = "INFO"


"""
Find me a string that when appended to "wcsclol"
hashes to an md5 hex sum that starts with 5 zeros
"""
def hashes_properly(s):
    return md5sumhex("wcsclol" + s).startswith("00000")

solution = iters.mbruteforce(hashes_properly, string.letters + string.digits, 7)
log.success("Found solution " + solution)


"""
Assemble "xor eax, eax"
"""
log.success("xor eax, eax: " + repr(asm("xor eax, eax")))