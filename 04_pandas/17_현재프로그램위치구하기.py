"""
파일에서 실행하면 현재 파일 위치를 구하고
프로그램에서 실행하면 현재 프로그램 위치를 구하도록 처리
"""

from pathlib import Path

print(__file__)                         # 파이썬에 존재하는 현재 파일 위치를 가진 값
print(Path(__file__))                   # 파일을 Path로 만듦
print(Path(__file__).resolve())         # 절대경로로 반환
print(Path(__file__).resolve().parent)  # 현재 파일의 소속 폴더 경로를 반환
print(Path(__file__).resolve().parent.joinpath("data/inspection.csv"))
print(Path(__file__).resolve().parent / "data/inspection.csv")
                                        # 'joinpath' 또는 '/' 사용해서 경로 붙일 수 있다.


