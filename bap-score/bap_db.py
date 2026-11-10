# DB 모듈
# - SQLite 급식 테이블 생성/저장/조회 담당

import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BAP_DB_PATH = os.path.join(BASE_DIR, "bap.db")

# ===========================================================
#  1. init_bap_db() : 급식 테이블 생성
# ===========================================================

def init_bap_db():
    conn = None
    try:
        conn = sqlite3.connect(BAP_DB_PATH)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS meals (
                mlsv_ymd TEXT NOT NULL,
                meal_nm TEXT NOT NULL,
                dish_nm TEXT NOT NULL,
                cal_info TEXT,
                PRIMARY KEY (mlsv_ymd, meal_nm)
            )
        """)

    except sqlite3.Error as e:
        print("DB 오류:", e)
        raise
 
    finally:
        if conn is not None:
            conn.close()


# ===========================================================
#  2. load_baps(): 저장된 급식 정보 조회
# ===========================================================
def load_baps(mlsv_ymd):
    conn = None
    try:
        conn = sqlite3.connect(BAP_DB_PATH)
        cur = conn.cursor()
        cur.execute("SELECT * FROM meals WHERE mlsv_ymd = ?", (mlsv_ymd,))
        return cur.fetchall()

    except sqlite3.Error as e:
        print("DB 오류:", e)
        raise

    finally:
        if conn is not None:
            conn.close()


# ===========================================================
#  3. load_all_baps(): 저장된 급식 정보 조회
# ===========================================================
def load_all_baps():
    conn = None
    try:
        conn = sqlite3.connect(BAP_DB_PATH)
        cur = conn.cursor()
        cur.execute("SELECT * FROM meals")
        return cur.fetchall()

    except sqlite3.Error as e:
        print("DB 오류:", e)
        raise

    finally:
        if conn is not None:
            conn.close()


# ===========================================================
#  4. save_meal() : 급식 정보 저장 (같은 날짜는 덮어쓰기)
#  - 특정 일자에 조중석식 여러 건이 될 수도 있고, 구조상 1개월치 데이터 전부를 저장하므로 executemany()로 저장
# ===========================================================
def save_bap(rows):
    conn = None
    try:
        conn = sqlite3.connect(BAP_DB_PATH)
        cur = conn.cursor()
        cur.executemany("INSERT OR REPLACE INTO meals VALUES (?, ?, ?, ?)", rows)
        conn.commit()

    except sqlite3.Error as e:
        print("DB 오류:", e)
        if conn is not None:
            conn.rollback()
        raise

    finally:
        if conn is not None:
            conn.close()