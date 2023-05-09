# towerOfHanoiChatGPT

def hanoi(n, src, dest, temp):
    if n > 0:
        hanoi(n - 1, src, temp, dest)
        print(f"Move disk {n} from {src} to {dest}")
        hanoi(n - 1, temp, dest, src)

hanoi(5, "A", "C", "B")
