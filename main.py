def read_log_file(filename):
    try:
        with open(filename, 'r', encoding ='utf-8') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {filename}")
    except Exception as e:
        print(f"알 수 없는 오류가 발생했습니다: {e}")

if __name__ == '__main__':
    read_log_file('mission_computer_main.log')
