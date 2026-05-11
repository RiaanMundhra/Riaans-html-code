class illegalbuilding:
    def __del__(self):
        print("BMC wants to create a road here... RIP class")

target = illegalbuilding()
del target