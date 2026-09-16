
import re                                      # 정규표현식(Regular Expression) 기능을 사용하기 위한 모듈
import shutil                                  # 파일 복사, 이동 등의 파일 시스템 작업을 위한 모듈
from pathlib import Path                       # 운영체제에 독립적인 경로 처리를 위한 Path 클래스
from urllib.parse import unquote, quote               # URL 인코딩된 문자열(%20 등)을 원래 문자로 변환하는 함수


# ============================================================
# 설정1 - 직접 입력
# ============================================================

# Notion Export 폴더 이름
NOTION_EXPORT_DIR_NAME = "2026-09-16-introduction-to-linearalgebra"

# 게시글 날짜
POST_DATE = "2026-09-16"

# 게시글 slug
POST_SLUG = "introduction-to-linearalgebra"

# ============================================================
# 설정2 - front matter 정보 입력
# ============================================================
POST_TITLE = "test post title"   
DESCRIPTION = "study note of linear algebra, textbook : Introduction to Linear Algebra, 5th edition, by Gilbert Strang"  # 게시글 설명
AUTHOR = "Sproutato"
# POST_DATE = "2026-09-05"
CATEGORIES = ["Linear Algebra"]
TAGS = []
PUBLISHED = True
PIN = False
MATH = True
MERMAID = True
                 # 게시글 제목을 원본 Markdown 파일명으로 설정
                               # 게시글 설명을 빈 문자열로 설정
                      # 게시글 작성자 ID를 cotes로 설정
                 # 게시글 날짜와 한국 시간대(+0900)를 설정
                            # 게시글 카테고리를 빈 목록으로 설정
                      # 게시글 태그를 빈 목록으로 설정
                         # 게시글을 실제 사이트에 게시하도록 설정
                  # 게시글을 상단 고정하지 않도록 설정
                    # 수학식 렌더링 기능을 활성화
                   # Mermaid 다이어그램 렌더링 기능을 활성화
IMAGE_PATH = ""  # 게시글 대표 이미지 경로
IMAGE_LQIP = ("data:image/webp;base64,"                                          # 게시글 대표 이미지 로딩 전 표시할 저화질 placeholder 경로
"UklGRpoAAABXRUJQVlA4WAoAAAAQAAAADwAABwAAQUxQSDIAAAARL0AmbZurmr57yyIiqE8oiG0bejIYEQTgqiDA9vqnsUSI6H+oAERp2HZ65qP/"
"VIAWAFZQOCBCAAAA8AEAnQEqEAAIAAVAfCWkAALp8sF8rgRgAP7o9FDvMCkMde9PK7euH5M1m6VWoDXf2FkP3BqV0ZYbO6NA/VFIAAAA")  
IMAGE_ALT = ""  # 게시글

# ============================================================
# 설정3 - 기본값들 + 자동 설정
# ============================================================

# Jekyll 프로젝트 루트
JEKYLL_ROOT = Path(                            # 문자열 경로를 Path 객체로 변환
    r"C:\Users\kkhs0\GitHub\sproutato.github.io"
)

# Notion Export 폴더
NOTION_EXPORT_DIR = Path(
    fr"{JEKYLL_ROOT}\assets\posts\{NOTION_EXPORT_DIR_NAME}"
)

# 폴더 안의 Markdown 파일 찾기
md_files = list(
    NOTION_EXPORT_DIR.glob("*.md")
)

# Markdown 파일이 하나도 없는 경우
if len(md_files) == 0:
    raise FileNotFoundError(
        f"Markdown 파일을 찾을 수 없습니다: {NOTION_EXPORT_DIR}"
    )

# Markdown 파일이 여러 개인 경우
if len(md_files) > 1:
    raise RuntimeError(
        f"Markdown 파일이 여러 개 있습니다: {md_files}"
    )

# 유일한 Markdown 파일 선택
NOTION_MD = md_files[0]


# ============================================================
# 경로 설정
# ============================================================

POST_NAME = f"{POST_DATE}-{POST_SLUG}"         # 날짜와 slug를 합쳐 최종 게시글 이름 생성

POSTS_DIR = JEKYLL_ROOT / "_posts"             # Jekyll 게시글들이 저장되는 _posts 폴더 경로

ASSET_DIR = NOTION_EXPORT_DIR

OUTPUT_MD = POSTS_DIR / f"{POST_NAME}.md"      # 최종적으로 생성할 Jekyll Markdown 파일 경로


# ============================================================
# Front matter 설정
# ============================================================

# front_matter = (                                            # Chirpy/Jekyll 게시글 상단에 넣을 Front Matter 문자열 생성
#         "---\n"                                                 # YAML Front Matter 시작 구분자
#         f'title: "{POST_TITLE}"\n'                              # 게시글 제목을 원본 Markdown 파일명으로 설정
#         f'description: "{DESCRIPTION}"\n'                                     # 게시글 설명을 빈 문자열로 설정
#         f'author: {AUTHOR}\n'                                       # 게시글 작성자 ID를 cotes로 설정
#         f"date: {POST_DATE} 00:00:00 +0900\n"                   # 게시글 날짜와 한국 시간대(+0900)를 설정
#         f"categories: [{', '.join(CATEGORIES)}]\n"                                      # 게시글 카테고리를 빈 목록으로 설정
#         f"tags: [{', '.join(TAGS)}]\n"                                            # 게시글 태그를 빈 목록으로 설정
#         f"published: {PUBLISHED}\n"                                     # 게시글을 실제 사이트에 게시하도록 설정
#         f"pin: {PIN}\n"                                          # 게시글을 상단 고정하지 않도록 설정
#         f"math: {MATH}\n"                                          # 수학식 렌더링 기능을 활성화
#         f"mermaid: {MERMAID}\n"                                       # Mermaid 다이어그램 렌더링 기능을 활성화
#          "image:\n"                                               # 게시글 대표 이미지 설정 블록 시작
#     f"  path: {IMAGE_PATH}\n"                                # 대표 이미지의 웹 경로 설정
#     f"  lqip: {IMAGE_LQIP}\n"                                # 대표 이미지 로딩 전 표시할 저화질 placeholder 설정
#     f'  alt: "{IMAGE_ALT}"\n'                                # 대표 이미지의 대체 텍스트 설정
#     "---\n\n"                                                # Front Matter 종료 후 본문과 두 줄 분리
# )


# ============================================================
# 이미지 파일명 정리
# ============================================================

def sanitize_filename(filename: str) -> str:   # 이미지 파일명을 안전한 형식으로 바꾸는 함수 정의
    """                                         # 함수 설명을 위한 docstring 시작
    예:                                         # 사용 예시
        image%208.png                             # 원래 파일명
            ↓                                   # 변환
        image-8.png                             # 변환 후 파일명
    """                                         # docstring 종료

    path = Path(filename)                       # 전달받은 파일명을 Path 객체로 변환

    stem = path.stem                            # 확장자를 제외한 파일명 추출: "image 8"
    suffix = path.suffix.lower()                # 파일 확장자 추출 후 소문자로 변경: ".PNG" → ".png"

    # 공백 → -
    stem = re.sub(                              # 정규표현식으로 문자열을 치환
        r"\s+",                                 # 하나 이상의 공백 문자를 찾음
        "-",                                    # 찾은 공백을 하이픈(-)으로 변경
        stem                                    # 변환할 대상 문자열
    )

    # 안전한 문자만 남김
    stem = re.sub(                              # 다시 정규표현식 치환 수행
        r"[^a-zA-Z0-9_-]",                      # 영문자, 숫자, _, - 이외의 문자를 찾음
        "-",                                    # 해당 문자를 하이픈(-)으로 변경
        stem                                    # 변환할 파일명
    )

    # --- 같은 중복 하이픈 제거
    stem = re.sub(                              # 여러 개의 연속된 하이픈을 하나로 줄임
        r"-+",                                  # 하나 이상의 연속된 하이픈을 찾음
        "-",                                    # 하나의 하이픈으로 변경
        stem                                    # 변환할 파일명
    )

    stem = stem.strip("-")                      # 파일명 앞뒤에 붙은 하이픈 제거

    return stem + suffix                        # 정리된 파일명과 확장자를 합쳐 반환


# ============================================================
# Markdown 이미지 경로 변환
# ============================================================

def replace_image_path(match):                  # 정규표현식으로 찾은 이미지 링크 하나를 처리하는 함수
    """                                         # 함수 설명 시작
    Markdown:                                   # 기존 Markdown 이미지 형식

    ![image.png](image%208.png)                 # Notion에서 Export된 이미지 링크

    ↓                                           # 아래와 같이 변환

    ![image.png](/assets/posts/.../image-8.png) # Jekyll에서 사용할 이미지 링크
    """                                         # 함수 설명 종료

    alt_text = match.group(1)                   # 첫 번째 그룹: [] 안의 이미지 설명 문자열 추출
    encoded_path = match.group(2)               # 두 번째 그룹: () 안의 이미지 경로 추출

    # http 이미지나 이미 변환된 절대 경로는 건드리지 않음
    if encoded_path.startswith(                 # 이미지 경로가 특정 문자열로 시작하는지 확인
        ("http://", "https://", "/")            # 외부 URL 또는 이미 절대 경로인 경우
    ):
        return match.group(0)                   # 원래 Markdown 이미지 문법을 그대로 반환

    # %20 → 공백
    decoded_path = unquote(encoded_path)        # URL 인코딩된 이미지 경로를 원래 문자열로 복원

    source_image = (                            # 실제 원본 이미지 파일의 위치 계산
        NOTION_MD.parent                        # Notion Markdown 파일이 있는 폴더
        / decoded_path                          # Markdown에 기록된 상대 이미지 경로 추가
    )

    if not source_image.exists():               # 해당 위치에 이미지 파일이 존재하지 않는 경우
        print(                                  # 경고 메시지를 콘솔에 출력
            f"[WARNING] 이미지 파일을 찾을 수 없음: {source_image}"
        )
        return match.group(0)                   # 이미지 링크를 수정하지 않고 원래 상태로 반환

    relative_path = source_image.relative_to(JEKYLL_ROOT)   # 전체 이미지 경로에서 Jekyll 루트 경로를 제거해 프로젝트 내부 상대경로만 추출

    relative_path = relative_path.as_posix()                 # Windows 경로 구분자 "\"를 웹 경로 구분자 "/"로 변환

    encoded_url = quote(relative_path)                       # 공백 같은 특수문자를 URL 인코딩 형식으로 변환

    new_url = f"/{encoded_url}"                              # 경로 앞에 "/"를 붙여 Jekyll 사이트 루트 기준 URL로 만듦

    return f"![{alt_text}]({new_url})"                       # 변환된 URL을 사용해 최종 Markdown 이미지 문법으로 반환


# ============================================================
# 실행
# ============================================================

# def main():                                                     # 프로그램의 전체 변환 과정을 실행하는 메인 함수 정의

    # POSTS_DIR.mkdir(                                            # Jekyll의 _posts 폴더가 없으면 생성
    #     parents=True,                                           # 상위 폴더도 없으면 함께 생성
    #     exist_ok=True                                           # 이미 폴더가 존재해도 오류를 발생시키지 않음
    # )                                                           # mkdir 설정 종료

    markdown = NOTION_MD.read_text(                             # 원본 Notion Markdown 파일의 내용을 문자열로 읽음
        encoding="utf-8"                                        # UTF-8 인코딩으로 파일을 읽음
    )                                                           # read_text 설정 종료

    title_match = re.match(r"^#\s+(.+?)\r?\n+", markdown)            # Markdown 맨 처음의 H1 제목을 찾아 제목 부분을 그룹 1로 캡처

    if title_match:                                                  # 문서 맨 처음에서 H1 제목을 찾은 경우
        POST_TITLE = title_match.group(1).strip()                    # "# " 뒤의 실제 제목 문자열을 POST_TITLE에 저장
        markdown = markdown[title_match.end():]                      # 찾은 H1 제목 부분까지 제거하고 그 이후 본문만 남김
    else:                                                            # 문서 맨 처음에 H1 제목이 없는 경우
        POST_TITLE = NOTION_MD.stem                                  # Markdown 파일명을 대신 게시글 제목으로 사용

    pattern = r"!\[([^\]]*)\]\(([^)]+)\)"                       # Markdown 이미지 문법 ![alt](path)을 찾기 위한 정규표현식

    converted_markdown = re.sub(                                # Markdown 전체에서 이미지 문법을 찾아 새로운 경로로 치환
        pattern,                                                # 찾을 Markdown 이미지 정규표현식 패턴
        replace_image_path,                                     # 이미지가 발견될 때마다 호출할 경로 변환 함수
        markdown                                                # 이미지 경로를 변환할 Markdown 문자열
    )                                                           # re.sub 실행 종료

    # POST_TITLE = NOTION_MD.stem                                 # 원본 Markdown 파일명에서 확장자 .md를 제외한 제목만 추출

    front_matter = (                                            # Chirpy/Jekyll 게시글 상단에 넣을 Front Matter 문자열 생성
        "---\n"                                                 # YAML Front Matter 시작 구분자
        f'title: "{POST_TITLE}"\n'                              # 게시글 제목을 원본 Markdown 파일명으로 설정
        f'description: "{DESCRIPTION}"\n'                                     # 게시글 설명을 빈 문자열로 설정
        f'author: {AUTHOR}\n'                                       # 게시글 작성자 ID를 cotes로 설정
        f"date: {POST_DATE} 00:00:00 +0900\n"                   # 게시글 날짜와 한국 시간대(+0900)를 설정
        f"categories: [{', '.join(CATEGORIES)}]\n"                                      # 게시글 카테고리를 빈 목록으로 설정
        f"tags: [{', '.join(TAGS)}]\n"                                            # 게시글 태그를 빈 목록으로 설정
        f"published: {PUBLISHED}\n"                                     # 게시글을 실제 사이트에 게시하도록 설정
        f"pin: {PIN}\n"                                          # 게시글을 상단 고정하지 않도록 설정
        f"math: {MATH}\n"                                          # 수학식 렌더링 기능을 활성화
        f"mermaid: {MERMAID}\n"                                       # Mermaid 다이어그램 렌더링 기능을 활성화
         "image:\n"                                               # 게시글 대표 이미지 설정 블록 시작
    f"  path: {IMAGE_PATH}\n"                                # 대표 이미지의 웹 경로 설정
    f"  lqip: {IMAGE_LQIP}\n"                                # 대표 이미지 로딩 전 표시할 저화질 placeholder 설정
    f'  alt: "{IMAGE_ALT}"\n'                                # 대표 이미지의 대체 텍스트 설정
    "---\n\n"                                                # Front Matter 종료 후 본문과 두 줄 분리
)

                                                    # front_matter 문자열 생성 종료

    OUTPUT_MD.write_text(                                       # _posts 폴더에 최종 Jekyll Markdown 파일을 생성하거나 덮어씀
        front_matter + converted_markdown,                       # Front Matter와 변환된 Markdown 본문을 이어 붙여 저장
        encoding="utf-8"                                        # UTF-8 인코딩으로 파일 저장
    )                                                           # write_text 실행 종료

    print(f"[완료] {OUTPUT_MD}")                                # 생성된 최종 Markdown 파일 경로를 콘솔에 출력
def main():                                                          # Notion Markdown을 Jekyll 게시글로 변환하는 전체 실행 함수 정의

    print("======================================================")   # 프로그램 시작 구분선 출력
    print("[START] Notion → Jekyll 변환 시작")                       # 프로그램 시작 메시지 출력
    print("======================================================")   # 프로그램 시작 구분선 출력
    print()                                                          # 출력 가독성을 위한 빈 줄 출력

    print(f"[설정] Jekyll Root       : {JEKYLL_ROOT}")                # 현재 설정된 Jekyll 프로젝트 루트 경로 출력
    print(f"[설정] Notion Export Dir : {NOTION_EXPORT_DIR}")          # 현재 설정된 Notion Export 폴더 경로 출력
    print(f"[설정] Notion MD         : {NOTION_MD}")                  # 자동으로 선택된 Notion Markdown 파일 경로 출력
    print(f"[설정] Output MD         : {OUTPUT_MD}")                  # 최종 생성될 Jekyll Markdown 파일 경로 출력
    print()                                                          # 설정 정보와 실제 처리 로그를 구분하기 위한 빈 줄 출력

    print("[1/6] _posts 폴더 확인 중...")                            # Jekyll _posts 폴더 확인 단계 시작 메시지 출력

    POSTS_DIR.mkdir(parents=True, exist_ok=True)                      # _posts 폴더가 없으면 생성하고 이미 존재하면 그대로 사용

    print(f"[1/6] _posts 폴더 준비 완료 : {POSTS_DIR}")              # _posts 폴더가 정상적으로 준비되었음을 출력
    print()                                                          # 다음 단계와 구분하기 위한 빈 줄 출력

    print("[2/6] Notion Markdown 읽는 중...")                        # 원본 Markdown 읽기 단계 시작 메시지 출력

    markdown = NOTION_MD.read_text(encoding="utf-8")                  # Notion에서 export한 Markdown 파일 전체 내용을 UTF-8로 읽음

    print(f"[2/6] Markdown 읽기 완료")                               # Markdown 읽기 성공 메시지 출력
    print(f"      문자 수 : {len(markdown):,}")                      # 읽은 Markdown 전체 문자 수 출력
    print()                                                          # 다음 단계와 구분하기 위한 빈 줄 출력

    print("[3/6] 게시글 제목 추출 중...")                            # 첫 번째 H1에서 게시글 제목을 추출하는 단계 시작 메시지 출력

    title_match = re.match(r"^#\s+(.+?)\r?\n+", markdown)             # Markdown 맨 처음에 있는 "# 제목" 형식의 H1을 탐색

    if title_match:                                                  # 맨 처음에 H1 제목이 정상적으로 존재하는 경우
        POST_TITLE = title_match.group(1).strip()                    # "# "를 제외한 실제 제목 문자열만 POST_TITLE에 저장
        markdown = markdown[title_match.end():]                      # 추출한 첫 번째 H1 부분을 본문에서 제거
        print(f"[3/6] H1 제목 추출 완료 : {POST_TITLE}")             # 추출한 게시글 제목 출력
    else:                                                            # Markdown 맨 처음에 H1 제목이 존재하지 않는 경우
        POST_TITLE = NOTION_MD.stem                                  # 원본 Markdown 파일명을 게시글 제목으로 대신 사용
        print(f"[3/6] H1 제목 없음 → 파일명 사용 : {POST_TITLE}")    # H1 대신 파일명을 사용했음을 출력

    print()                                                          # 다음 단계와 구분하기 위한 빈 줄 출력

    print("[4/6] 이미지 경로 검사 및 변환 중...")                   # Markdown 이미지 링크 변환 단계 시작 메시지 출력

    pattern = r"!\[([^\]]*)\]\(([^)]+)\)"                            # Markdown의 ![alt](path) 형식 이미지 문법을 찾는 정규표현식 정의

    image_matches = re.findall(pattern, markdown)                    # 실제 변환 전에 Markdown 안의 모든 이미지 문법을 찾아 목록으로 저장

    print(f"[4/6] 발견된 이미지 수 : {len(image_matches)}개")        # Markdown에서 발견한 전체 이미지 개수 출력

    converted_markdown = re.sub(pattern, replace_image_path, markdown)  # 발견된 모든 이미지에 replace_image_path 함수를 적용하여 경로 변환

    print(f"[4/6] 이미지 경로 변환 완료")                            # 모든 이미지 경로 변환이 끝났음을 출력
    print()                                                          # 다음 단계와 구분하기 위한 빈 줄 출력

    print("[5/6] Front Matter 생성 중...")                           # Chirpy용 Front Matter 생성 단계 시작 메시지 출력

    front_matter = (                                                 # 최종 Markdown 맨 위에 들어갈 YAML Front Matter 문자열 생성
        "---\n"                                                      # YAML Front Matter 시작 구분자 추가
        f'title: "{POST_TITLE}"\n'                                   # 추출한 H1 제목을 게시글 제목으로 설정
        f'description: "{DESCRIPTION}"\n'                             # 설정한 게시글 설명을 description에 입력
        f"author: {AUTHOR}\n"                                        # 설정한 작성자 ID를 author에 입력
        f"date: {POST_DATE} 00:00:00 +0900\n"                        # 게시글 날짜와 한국 표준시 시간대를 설정
        f"categories: [{', '.join(CATEGORIES)}]\n"                   # Python 카테고리 리스트를 YAML 배열 형태 문자열로 변환
        f"tags: [{', '.join(TAGS)}]\n"                               # Python 태그 리스트를 YAML 배열 형태 문자열로 변환
        f"published: {str(PUBLISHED).lower()}\n"                      # Python bool 값을 YAML 형식의 true 또는 false로 변환
        f"pin: {str(PIN).lower()}\n"                                 # 게시글 상단 고정 여부를 YAML bool 형식으로 변환
        f"math: {str(MATH).lower()}\n"                               # 수학식 렌더링 사용 여부를 YAML bool 형식으로 변환
        f"mermaid: {str(MERMAID).lower()}\n"                         # Mermaid 렌더링 사용 여부를 YAML bool 형식으로 변환
        "image:\n"                                                   # 대표 이미지 관련 YAML 블록 시작
        f"  path: {IMAGE_PATH}\n"                                    # 대표 이미지의 웹 경로 입력
        f"  lqip: {IMAGE_LQIP}\n"                                    # 대표 이미지 로딩 전에 보여줄 LQIP 데이터 입력
        f'  alt: "{POST_TITLE}"\n'                                    # 대표 이미지의 대체 텍스트 입력
        "---\n\n"                                                    # Front Matter를 종료하고 본문과 두 줄 간격 생성
    )                                                               # Front Matter 문자열 생성 종료

    print("[5/6] Front Matter 생성 완료")                            # Front Matter 생성 성공 메시지 출력
    print("------------------------------------------------------")   # Front Matter 확인용 구분선 출력
    print(front_matter)                                              # 실제로 생성된 Front Matter 전체 내용을 콘솔에 출력
    print("------------------------------------------------------")   # Front Matter 확인용 구분선 출력
    print()                                                          # 다음 단계와 구분하기 위한 빈 줄 출력

    print("[6/6] Jekyll Markdown 파일 저장 중...")                   # 최종 Markdown 파일 생성 단계 시작 메시지 출력

    OUTPUT_MD.write_text(front_matter + converted_markdown, encoding="utf-8")  # Front Matter와 변환된 본문을 합쳐 _posts에 저장

    print("[6/6] Jekyll Markdown 파일 저장 완료")                    # 파일 저장 성공 메시지 출력
    print(f"      출력 경로 : {OUTPUT_MD}")                          # 최종 생성된 파일의 전체 경로 출력
    print(f"      파일 존재 : {OUTPUT_MD.exists()}")                 # 파일이 실제 파일 시스템에 생성됐는지 True 또는 False로 출력
    print(f"      파일 크기 : {OUTPUT_MD.stat().st_size:,} bytes")   # 최종 Markdown 파일의 실제 파일 크기를 byte 단위로 출력
    print()                                                          # 최종 결과와 구분하기 위한 빈 줄 출력

    print("======================================================")   # 프로그램 종료 구분선 출력
    print("[완료] Notion → Jekyll 변환 완료")                        # 전체 작업 완료 메시지 출력
    print(f"[완료] 제목   : {POST_TITLE}")                           # 최종 게시글 제목 출력
    print(f"[완료] 원본   : {NOTION_MD}")                            # 사용한 원본 Notion Markdown 경로 출력
    print(f"[완료] 결과   : {OUTPUT_MD}")                            # 생성된 Jekyll Markdown 파일 경로 출력
    print("======================================================")   # 프로그램 종료 구분선 출력

if __name__ == "__main__":                      # 이 파일을 직접 실행한 경우에만 아래 코드 실행
    main()                                      # main 함수 호출