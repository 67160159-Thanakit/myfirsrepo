class BubbleSorter:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        n = len(self.arr)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if self.arr[j] > self.arr[j + 1]:
                    # สลับค่า
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
            # แสดงข้อมูลหลังแต่ละรอบ
            print(f"After round {i + 1}: {self.arr}")

    def display(self):
        print(f"Current data: {self.arr}")


if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]
    sorter = BubbleSorter(nums)

    print("Before sorting:")
    sorter.display()

    sorter.sort()

    print("\nAfter sorting:")
    sorter.display()
