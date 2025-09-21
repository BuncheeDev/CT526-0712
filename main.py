from mylib import myfunc


def main():
    """
    โปรแกรมสำหรับแสดงตัวอย่าง  myfunc
    """
    try:
        turns = input("ใส่เลขที่ต้องการ: ")
        if turns.strip() == "":
            turns = 4
        else:
            turns = int(turns)
        # แสดงผล input
        for i in range(1, turns + 1):
            result = myfunc(" (\_/)", i)
            result1 = myfunc("( •_•)", i)
            result2 = myfunc("/ > > ", i)

            print(result)
            print(result1)
            print(result2)

    except ValueError:
        print("กรุณาใส่ตัวเลขที่ถูกต้อง")
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")


if __name__ == "__main__":
    main()
