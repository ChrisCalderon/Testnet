import subprocess

class BaseNode:
    def __init__(self,
                 rpchost: str,
                 rpcport: int,
                 ):