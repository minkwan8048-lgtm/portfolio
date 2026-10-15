# GitHub Pages 배포 가이드

`outputs/portfolio-hub/` 사이트를 `https://minkwan8048-lgtm.github.io/portfolio/`로 호스팅하는 방법.

---

## 사전 확인

- GitHub 계정: **minkwan8048-lgtm** (game-records와 동일 계정)
- Git 설치 완료
- `_sync_pdfs.py` 한 번 실행하여 `assets/pdfs/`에 PDF 6종 들어있음

---

## 1단계 — GitHub 저장소 생성

1. https://github.com/new 접속
2. Repository name: **`portfolio`**
3. Visibility: **Public** (Pages는 무료 플랜에서 Public만 호스팅 가능)
4. README·gitignore 등은 추가하지 않음 (이미 로컬에 있음)
5. **Create repository**

생성 후 저장소 URL: `https://github.com/minkwan8048-lgtm/portfolio`

---

## 2단계 — 로컬 → GitHub 푸시

PowerShell에서:

```powershell
cd C:\Users\zoowi\Documents\job-prep\outputs\portfolio-hub
git init
git add .
git commit -m "Initial: portfolio package hub site"
git branch -M main
git remote add origin https://github.com/minkwan8048-lgtm/portfolio.git
git push -u origin main
```

푸시 시 GitHub 인증창이 뜨면 사용자 이름·토큰 입력.

---

## 3단계 — GitHub Pages 활성화

1. 저장소 → **Settings** 탭
2. 좌측 메뉴 → **Pages**
3. Source 섹션:
   - Source: **Deploy from a branch**
   - Branch: **main** / **/ (root)**
4. **Save**

1~2분 후 페이지 상단에 다음과 같이 표시됨:

```
Your site is live at https://minkwan8048-lgtm.github.io/portfolio/
```

---

## 4단계 — 접속 확인

1. `https://minkwan8048-lgtm.github.io/portfolio/`로 접속
2. Hero 영역의 슬로건과 5장 카드 표시 확인
3. 각 카드 클릭 → 새 탭에서 PDF 열림 확인
4. 모바일에서도 한 번 확인 (반응형 동작)

---

## 5단계 — 이력서·이메일에 URL 첨부

면접관에게 보내는 이메일 본문에 URL 한 줄 첨부:

```
포트폴리오 패키지: https://minkwan8048-lgtm.github.io/portfolio/
```

또는 이력서 v2부터는 사이트 URL을 인적사항·하단 등에 명시.

---

## 갱신 워크플로

자소서·경력기술서·이력서·PPT가 새 버전으로 빌드되면:

```bash
# 1. PDF 동기화 (파일명 버전 미노출 — _sync_pdfs.py가 고정 슬러그로 덮어쓰기)
python outputs/portfolio-hub/_sync_pdfs.py

# 2. (필요 시) index.html 카드 메타의 페이지 수 갱신
#    - <span class="card-meta">3 pages</span>
#    - href 경로는 그대로 (assets/pdfs/cover_letter.pdf 등)

# 3. footer 갱신일 변경
#    - <span id="footer-updated">Last updated · YYYY.MM.DD</span>

# 4. 푸시
cd outputs/portfolio-hub
git add .
git commit -m "Sync PDFs"
git push
```

GitHub Pages는 푸시 후 1~2분 내 자동 갱신.

---

## 트러블슈팅

- **PDF가 GitHub에서 미리보기 안 됨**: 정상. 클릭 시 다운로드 또는 브라우저 PDF 뷰어로 열림.
- **404 페이지**: 저장소 이름이 정확히 `portfolio`인지 확인. URL은 대소문자 구분.
- **CSS·폰트 안 불러와짐**: 인터넷 연결 확인 (Google Fonts 사용). 또는 폰트만 시스템 폰트로 fallback (현재 CSS에 fallback 적용됨).
- **PDF 용량이 너무 큼**: 디멘션 PPT가 690KB로 가장 무거움. GitHub 100MB 제한에서 충분히 여유.

---

## 게임 기록지 사이트와의 관계

두 사이트는 **별개 저장소**로 운영:

- `https://minkwan8048-lgtm.github.io/game-records/` — 본인 플레이 게임 이력
- `https://minkwan8048-lgtm.github.io/portfolio/` — 이직 패키지 PDF 6종

이력서에는 두 URL이 모두 포함됨 (PLAYED GAME 섹션의 게임 기록지 + 추후 portfolio 사이트 추가 검토).
현재 portfolio-hub 사이트에서는 게임 기록지 링크 미노출 (사용자 결정, 2026-05-10).
