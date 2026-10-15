"""
final/ 의 PDF 6종을 portfolio-hub/assets/pdfs/ 로 동기화한다.

자소서·경력기술서·이력서·PPT가 신규 빌드되어 final/에 입주할 때 실행.
파일명은 portfolio-hub 사이트 카드와 매핑되도록 영문 슬러그로 변환한다.

실행: python outputs/portfolio-hub/_sync_pdfs.py
"""
from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FINAL = ROOT / "outputs" / "final"
DEST = Path(__file__).resolve().parent / "assets" / "pdfs"

# (파일 패턴, 결과 슬러그) — _final/은 "N. 한글_서민관.pdf" 형태
# 사이트에는 버전 미노출 정책 (2026-05-10 사용자 결정) — 슬러그도 버전 없이 고정
MAP = [
    (re.compile(r"^1\..*이력서.*\.pdf$"), "resume.pdf"),
    (re.compile(r"^2\..*자기소개서.*\.pdf$"), "cover_letter.pdf"),
    (re.compile(r"^3\..*경력기술서.*\.pdf$"), "career_history.pdf"),
    (re.compile(r"^4\..*보스몬스터.*\.pdf$"), "boss.pdf"),
    (re.compile(r"^5\..*디멘션.*\.pdf$"), "dimension.pdf"),
    (re.compile(r"^6\..*어비스.*\.pdf$"), "abyss.pdf"),
]


def main() -> int:
    if not FINAL.exists():
        print(f"[ERROR] final 폴더 없음: {FINAL}")
        return 1
    DEST.mkdir(parents=True, exist_ok=True)

    # 신규 파일명 매핑
    final_files = sorted(p.name for p in FINAL.iterdir() if p.suffix.lower() == ".pdf")
    new_names: dict[str, str] = {}
    for name in final_files:
        for pattern, slug in MAP:
            if pattern.match(name):
                new_names[name] = slug
                break

    if len(new_names) != 6:
        print(f"[WARN] _final/에서 6종 PDF를 찾지 못함 (발견: {len(new_names)})")
        for k, v in new_names.items():
            print(f"  - {k} → {v}")

    # 기존 portfolio-hub PDF 제거 (구버전 누적 방지)
    removed = 0
    for old in DEST.glob("*.pdf"):
        old.unlink()
        removed += 1
    print(f"[CLEAN] 기존 PDF {removed}개 제거")

    # 신규 복사
    for src_name, dst_name in new_names.items():
        src = FINAL / src_name
        dst = DEST / dst_name
        shutil.copy2(src, dst)
        size_kb = dst.stat().st_size // 1024
        print(f"[COPY] {src_name}\n     → {dst_name} ({size_kb} KB)")

    print(f"\n[DONE] {len(new_names)}개 PDF 동기화 완료")
    return 0


if __name__ == "__main__":
    sys.exit(main())
