# 🍚 밥이화(BabEwha) 🍚
### OCR 기반 배달 애플리케이션 **🍚** **밥이화(BabEwha) 🍚** AI 레포지토리입니다.
#### 1️⃣ Client 레포지토리 링크: https://github.com/BabEwha/BabEwha-Client
#### 2️⃣ AI 레포지토리 링크: https://github.com/BabEwha/BabEwha-AI

<br/>

## 🍙 프로젝트 소개


개발 기간: 2023.03.15(금) ~ 2023.03.17(일) <br/>
예상 사용자 설문조사 링크: https://docs.google.com/forms/d/e/1FAIpQLSfulZbuCy8cGD-FTW601AuBbd7FedH7zUMOYdtjfu-iqWXjSw/viewform?usp=sf_link

<br/><br/>

## 🍙 프로젝트 구조

<img width="1000" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/adda6865-b0f4-4f80-9cad-79eb534990bb"/>

- Client: Swift(iOS)
- Server: Django, MySQL, AWS EC2, AWS S3
- AI: Google Vision, Flask, AWS EC2

<br/><br/>

## 🍙 팀원 소개

| <img width="200" src=""/> | <img width="200" src=""/> | <img width="200" src=""/> | <img width="200" src=""/> | <img width="200" src=""/> |
| --- | --- | --- | --- | --- |
| **엄채은** | **양연우** | **허혜민** | **김원정** | **이남영** |
| 기획 | 디자이너 | 프론트엔드 | 백엔드 | IT기술(AI) |

<br/>

## 🍙 백엔드 사용 기술

| <img width="150" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/e6e67c4b-a277-41ec-b0a4-e7056b3af2b9"/> | <img width="150" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/b77a0873-1c1f-4e9a-b5f2-2bb8a94dc1c7"/> | <img width="150" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/af74bdba-9617-477d-ad85-83b286cf14ea"/> | <img width="150" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/d4c2512a-0dce-4f2e-b2b9-043047349607"/> |
| --- | --- | --- | --- |
| **서버** | **DB 관리** | **데이터 관리** | **배포** |
| Django | MySQL | AWS S3 | AWS EC2 |

<br/>

## 🍙 백엔드 응답 확인 (주기능 3가지)

| <img width="300" src=""/> | <img width="300" src=""/> | <img width="300" src=""/> |
| --- | --- | --- |
| **배달 모임 생성(리더벗)** | **주문 넣기(참여벗)** | **배달 모임 리스트 나열** |
| 리더벗이 Group 테이블의 모든 정보(제목, 내용, 장소, 최대 인원, 배달 링크, 시간 제한)를 기입하여 모임 생성 | 참여벗이 장바구니 캡쳐본으로 주문을 넣을시 주문 생성 | 현재 공구 중인 배달 게시물을 피드의 형태로 나열 |

✅ 웹 서비스 주소 (배포 완료): http://18.116.163.161/
