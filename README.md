# 서민관 — Portfolio Package

게임 기획자 이직 패키지 PDF 6종을 한 URL로 받을 수 있는 정적 사이트.
면접관·인사담당자에게 한 링크로 패키지를 전달하기 위한 진입점.

**공개 URL:** `https://minkwan8048-lgtm.github.io/portfolio/` (배포 후)

---

## 사이트 구성

- **Hero** — 이름 / 직책 / 이력서 슬로건
- **Documents** — PDF 6장 카드 (이력서·자소서·경력기술서·보스몬스터·디멘션·어비스)
- **Footer** — 이메일 / 마지막 갱신일

## 디자인 톤

`outputs/design-system/design-system.md` 그대로:

- 배경: 딥 네이비 #0A0E1A
- 카드: 다크 카드 #1A2035
- 액센트: 사이언 #00D4FF / 옐로우 #F5C518
- 폰트: Pretendard (한글) / Inter (영문)

포트폴리오 PPT 3종와 동일한 톤 — 패키지 일관성 유지.

---

## 파일 구조

```
portfolio-hub/
├── index.html              # 단일 페이지 (Hero + 카드 그리드 + Footer)
├── style.css               # 다크 네이비 + Brandlogy 톤
├── assets/
│   └── pdfs/               # final/ 에서 동기화된 PDF 6종 (버전 미노출)
│       ├── resume.pdf
│       ├── cover_letter.pdf
│       ├── career_history.pdf
│       ├── dimension.pdf
│       └── abyss.pdf
├── _sync_pdfs.py           # final/ → assets/pdfs/ 자동 동기화
├── .nojekyll               # GitHub Pages Jekyll 비활성화
├── .gitignore
├── README.md               # 이 파일
└── _deploy_guide.md        # GitHub Pages 호스팅 가이드
```

---

## PDF 갱신 워크플로

자소서·경력기술서·이력서·PPT가 신규 빌드되어 `final/`에 입주할 때:

```bash
python outputs/portfolio-hub/_sync_pdfs.py
```

스크립트가 `final/`의 PDF 6종을 `assets/pdfs/`에 영문 슬러그로 복사한다.
(매핑: `1. 자기소개서_*.pdf` → `cover_letter.pdf` 형태, 버전 미노출 정책)

PDF 파일명에 버전을 노출하지 않는 정책이라 `index.html`의 href 경로는 갱신 불필요.
다만 페이지 수가 바뀌면 카드 메타(`<span class="card-meta">3 pages</span>`)는 수동 갱신.

---

## 로컬 확인

```bash
# Python 단순 서버
cd outputs/portfolio-hub
python -m http.server 8080
# → http://localhost:8080
```

`file://` 프로토콜로 직접 열어도 PDF 링크는 작동한다 (정적 파일).

---

## 배포

`_deploy_guide.md` 참고. 요약:

1. GitHub 저장소 `minkwan8048-lgtm/portfolio` 생성 (Public)
2. 이 폴더 내용을 푸시
3. Settings → Pages → Source: `main` 브랜치 / `/ (root)`
4. 1-2분 후 `https://minkwan8048-lgtm.github.io/portfolio/`에서 확인

---

## 향후 확장

- 보스 몬스터 PPT (10~11개월차 작업) 추가 시 카드 1장 추가
- 회사별 맞춤 자소서·경력기술서 버전 토글 (현재 범용 버전만 노출)
- 영문 버전 (지원 회사 영문 자료 요구 시)
