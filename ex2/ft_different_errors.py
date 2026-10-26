def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        42 / 0
    elif operation_number == 2:
        open("/non/existent/file", "r")
    elif operation_number == 3:
        "abc" + 1
    return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    operation_number = 0
    while operation_number <= 4:
        print(f"Testing operation {operation_number}...")
        try:
            garden_operations(operation_number)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        else:
            print("Operation completed successfully")
        operation_number += 1
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
