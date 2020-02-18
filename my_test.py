import my_debugger

debugger = my_debugger.debugger()

#debugger.load("C:\\Windows\\System32\\calc.exe")
pid = input("Enter the PID of the process to attach to: ")
debugger.attach(int(pid))
debugger.detach()
