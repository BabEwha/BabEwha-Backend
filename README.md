# 🍚 밥이화(BabEwha) 🍚
### OCR 기반 배달 어플리케이션 **🍚** **밥이화(BabEwha) 🍚** Backend 레포지토리입니다.
#### 1️⃣ Client 레포지토리 링크: https://github.com/BabEwha/BabEwha-Client
#### 2️⃣ AI 레포지토리 링크: https://github.com/BabEwha/BabEwha-AI

<br/><br/>

## 🍙 프로젝트 소개


개발 기간: 2023.03.15(금) ~ 2023.03.17(일) <br/>
예상 사용자 설문조사: 3.15(금) 21:00 ~ 3.17(일) 14:00<br/>
설문 링크 (현재 폐쇄): https://docs.google.com/forms/d/e/1FAIpQLSfulZbuCy8cGD-FTW601AuBbd7FedH7zUMOYdtjfu-iqWXjSw/viewform?usp=sf_link

<br/><br/>

## 🍙 프로젝트 구조

<img width="800" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/adda6865-b0f4-4f80-9cad-79eb534990bb"/>

- Client: Swift(iOS)
- Server: Django, MySQL, AWS EC2, AWS S3
- AI: Google Vision, Flask, AWS EC2

<br/><br/>

## 🍙 팀원 소개

| <img width="200" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/1a77ca56-1b72-48cc-81e1-09d2d2ee1688"/> | <img width="200" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/0c997a4a-b942-457a-8c20-fb8bdd0a7277"/> | <img width="200" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/f1414b85-9269-4aae-a121-af8e01090579"/> | <img width="200" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/6b676f0c-d5e1-44e9-ab1d-1d00d7c48046"/> | <img width="200" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/4be5a2b8-fd32-4ccc-b89c-00d4269c77ce"/> |
| --- | --- | --- | --- | --- |
| **엄채은** | **양연우** | **허혜민** | **김원정** | **이남영** |
| 기획 | 디자이너 | 프론트엔드 | 백엔드 | IT기술(AI) |

<br/><br/>

## 🍙 백엔드 사용 기술

| <img width="150" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/e6e67c4b-a277-41ec-b0a4-e7056b3af2b9"/> | <img width="150" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/b77a0873-1c1f-4e9a-b5f2-2bb8a94dc1c7"/> | <img width="150" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/af74bdba-9617-477d-ad85-83b286cf14ea"/> | <img width="150" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/d4c2512a-0dce-4f2e-b2b9-043047349607"/> |
| --- | --- | --- | --- |
| **서버** | **DB 관리** | **데이터 관리** | **배포** |
| Django | MySQL | AWS S3 | AWS EC2 |

<br/><br/>

## 🍙 ERD
<img width="800" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/7342b758-3dce-4911-9d31-a736582aec5e"/>

<br/><br/>

## 🍙 백엔드 기능 설명

### 🍘 주요 코드 설명
| <img width="200" src=""/> | 
| --- |
| 이 OrderSerializer는 사용자가 특정 배달 모임에 참여하기 위해 외부 배달 앱을 통해 주문하고자 하는 음식의 장바구니 사진을 업로드할 때 사용됩니다. 사용자가 선택한 배달 모임(group)에 입장할 수 있는 조건을 검증한 후, 조건을 만족하는 경우 Order 테이블에 새로운 인스턴스를 생성하고, 사용자의 모임 참여 여부를 나타내는 Participate 관계 테이블에도 인스턴스를 생성합니다. 이 과정은 Django의 Serializer를 활용하여 데이터를 직렬화함으로써 이루어집니다. |

### **🍘 주요 테이블 설명**

**1️⃣ `Order` 테이블**
- 사용자가 배달 모임을 통해 주문한 음식에 대한 정보 저장
- 주요 필드: **`order_id`** (주문 식별자), **`group`** (배달 모임), **`user`** (주문한 사용자), **`order_image`** (주문 음식의 장바구니 사진), **`order_time`** (주문 시각)
- **`order_id`** 필드는 읽기 전용, 나머지 필드는 주문 생성 시 필요한 데이터 저장

**2️⃣ `Participate` 테이블**
- 사용자와 배달 모임 간의 관계 테이블
- 사용자의 배달 모임 참여 여부, 참여 활성 상태(**`is_active`**)를 포함, 모임의 소유자 여부(**`is_owner`**) 기록

### **🍘 주요 로직 설명**

**1️⃣ 사용자 입장 가능성 검증**: 사용자가 참여하려는 배달 모임의 현재 인원수를 확인하고, 최대 인원수에 도달하지 않았는지 검증합니다. 최대 인원수에 도달한 경우, 추가 참여는 불가능합니다.

**2️⃣ 모임 상태 변경**: 모임의 현재 인원수가 최대 인원수에 1명 미만으로 남았을 경우, 다음 사용자의 참여로 모임이 가득 차게 되면, 모임의 상태를 변경하여 더 이상 새로운 참여자를 받지 않도록 합니다.

**3️⃣ 데이터 인스턴스 생성**: 조건을 만족하는 경우, **`Order`** 테이블에 사용자의 주문 데이터를 저장하는 새 인스턴스를 생성하고, **`Participate`** 테이블에 사용자와 모임의 관계를 나타내는 새 인스턴스를 생성합니다. 이 과정은 모임의 참여 조건과 상태를 엄격하게 관리하며 사용자의 주문 및 참여를 원활하게 처리합니다.

이 기능은 사용자가 배달 모임에 원활하게 참여하고 주문을 진행할 수 있도록 도와주며, 모임의 인원 관리 및 주문 상태를 체계적으로 관리합니다.

<br/><br/>

## 🍙 백엔드 주요 기능 응답 확인

| <img width="300" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/092ea509-35d5-491b-aced-47ed477f1239"/> | <img width="400" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/ab21662a-8203-4395-9842-20cec571714c"/> | <img width="400" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/9f17aabf-5bf6-4eca-a329-9e3efa4b374e"/> |
| --- | --- | --- |
| **1️⃣ 배달 모임 생성(리더벗)** | **2️⃣ 주문 넣기(참여벗)** | **3️⃣ 배달 모임 리스트 나열** |
| 리더벗이 '장소, 최대 인원,시간 제한 등'을 기입하여 모임 생성 | 참여벗이 장바구니 캡쳐본으로 주문을 넣을시 주문 생성 | 현재 공구 중인 배달 게시물을 피드의 형태로 나열 |

<br/>

✅ 웹 서비스 주소 (배포 완료): http://18.116.163.161/ (엔드포인트는 상이함)

<br/><br/><br/><br/>
