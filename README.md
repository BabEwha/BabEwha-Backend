# 🍚 밥이화(BabEwha) 🍚
### OCR 기반 배달 어플리케이션 **🍚** **밥이화(BabEwha) 🍚** AI 레포지토리입니다.
#### 1️⃣ Client 레포지토리 링크: https://github.com/BabEwha/BabEwha-Client
#### 2️⃣ Backend 레포지토리 링크: https://github.com/BabEwha/BabEwha-Backend

- 개발 기간: 2023.03.15(금) ~ 2023.03.17(일) <br/>
- 예상 사용자 설문조사: 3.15(금) 21:00 ~ 3.17(일) 14:00<br/>
- 설문 링크 (현재 폐쇄): https://docs.google.com/forms/d/e/1FAIpQLSfulZbuCy8cGD-FTW601AuBbd7FedH7zUMOYdtjfu-iqWXjSw/viewform?usp=sf_link

<br/>

## 🍙 프로젝트 소개

### 기존에 이화인끼리 진행하던 ‘배달톡방’을 어플화하여 직관적이고 신속한 배달을 가능하게 하는 ‘배달 공구 서비스’

### 🍘 문제 상황 및 솔루션
#### 1️⃣ 식사권이 보장되지 않는 상황
- 넓은 부지를 소유하고 있는 우리 학교지만, 상권은 정문 위주로 형성되어 있으며 언덕이 심한 특성으로 인해 한 번 각 건물로 등교하면 다른 장소로의 이동이 어려움
- 공대, 연협, 중도 등 정문과 거리가 있는 건물의 학생들은 근방에 음식점이 없어 편의점이나 배달을 통해 식사를 해결하고 있음.
- 편의점의 경우 영양 불균형 문제가 심각하게 발생함. 그러나 배달의 경우 오르는 배달팁이 부담됨.
#### 2️⃣ 배달 공구를 이용하고 있으나, 현존하는 배달 공구는 카카오톡 오픈채팅을 이용하기에 여러 불편이 따르는 상황
- 공구를 할 때마다 새로 오픈채팅방을 파야 하고, 알림이나 입장/퇴장 등 배달 공구 경험을 방해하는 여러 요소들이 존재함
- 이로 인해 배달 공구를 포기하는 인원이 다수 발생하여 공구 리젠이 줄어듦
- => 직관적인 UI/UX로, 사용자로 하여금 신속하고 긍정적인 배달 공구 경험을 쌓게함. 이를 통해 배달 공구를 활성화하고, 교내 이화 학생들의 식사권 보장 및 배달팁 감소를 통한 금전적 이득 보장을 가능케 함. 

### 🍘 가치
#### '이화’라는 공간 내에서 공동 생활을 하는 이화인이 공동 구매 경험을 통해 서로의 이익 증진과 권리 보장을 도모할 수 있음 
### 🍘 차별성
#### 1️⃣ 실제 사용자 리서치를 통해 얻은 결과로, 사용자 맞춤형 UI/UX 제안
- 총 응답 324개를 바탕으로 신뢰성 향상
- 사용자가 진정으로 원하는 서비스임을 확인
#### 2️⃣ 배달 공구의 신속성을 위하여 AI (OCR) 기술 적용
- 공구 참여자, 공구 개설자의 주문내역 및 영수증을 확인하여 신속하고 안전한 정산

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

## 🍙 API 명세서
<img width="700" src="https://github.com/BabEwha/BabEwha-Backend/assets/121528605/b38c28f5-647e-4d1e-9edf-71df81782e7b"/>



## 🍙 백엔드 기능 설명

### 🍘 주요 코드 설명
| <img width="400" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/68f6c686-5f8e-4dbf-9557-c05176cb64a1"/> | <img width="400" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/784cb07f-3b02-44f7-8cd7-36f937f7edc9"/> | 
| --- | --- |
| **1️⃣** OrderSerializer로 사용자가 특정 배달 모임에 참여하기 위해 외부 배달 앱을 통해 주문하고자 하는 음식의 장바구니 사진을 업로드할 때 사용 <br/> **2️⃣** 사용자가 선택한 배달 모임(group)에 입장할 수 있는 조건을 검증한 후, 조건을 만족하는 경우 Order 테이블과 사용자의 모임 참여 여부를 나타내는 Participate 관계 테이블에 인스턴스를 생성 | **1️⃣** GroupViewSet은 사용자가 특정 그룹에 참여하기 위한 과정을 관리하는 Django REST Framework의 뷰셋 <br/> **2️⃣** 사용자 인증, 그룹 정보 직렬화, 그룹 관련 권한 관리, 그룹의 조회 및 조작을 위한 다양한 액션을 포함|

<br/>

### **🍘 주요 테이블 설명**

**1️⃣ `Order` 테이블**
- 사용자가 배달 모임을 통해 주문한 음식에 대한 정보 저장
- 주요 필드: **`order_id`** (주문 식별자), **`group`** (배달 모임), **`user`** (주문한 사용자), **`order_image`** (주문 음식의 장바구니 사진), **`order_time`** (주문 시각)
- **`order_id`** 필드는 읽기 전용, 나머지 필드는 주문 생성 시 필요한 데이터 저장

**2️⃣ `Participate` 테이블**
- 사용자와 배달 모임 간의 관계 테이블
- 사용자의 배달 모임 참여 여부, 참여 활성 상태(**`is_active`**)를 포함, 모임의 소유자 여부(**`is_owner`**) 기록

**3️⃣ `Group` 테이블**
- 그룹 id, 제목, 설명, 장소, 세부 장소, 그룹 이미지, 링크, 생성 시간, 마감 시간, 최대 인원, 현재 인원 수, 그룹 상태 저장

**4️⃣ `Participate` 테이블**
- 사용자의 참여 그룹, 참여 활성 상태, 모임의 소유자 여부를 기록

<br/>

### **🍘 주요 로직 설명**

사용자가 배달 모임에 원활하게 참여하고 주문을 진행할 수 있도록 모임의 인원 관리 및 주문 상태를 체계적으로 관리

**1️⃣ 사용자 입장 가능성 검증**
- 사용자가 참여하려는 배달 모임의 현재 인원수 확인
- 최대 인원수에 도달하지 않았는지 검증 - 최대 인원수 도달시 추가 참여 불가능

**2️⃣ 모임 상태 변경**
- 모임의 최대 인원수 도달시 모임의 상태를 변경하여 더 이상 새로운 참여자를 받지 않도록 설정

**3️⃣ 데이터 인스턴스 생성**
- **`Order`** 테이블에 사용자의 주문 데이터를 저장하는 인스턴스를 생성, **`Participate`** 테이블에 사용자와 모임의 관계를 나타내는 새 인스턴스를 생성

**4️⃣ 그룹 검색 및 필터링**
- 장소, 생성 시간, 마감 시간을 기준으로 그룹 정렬 기능

**5️⃣ 마감 임박 그룹 조회**
- closing_soon 액션을 통해 마감 시간이 현재로부터 10분 이내인 그룹을 조회

**6️⃣ 그룹 상태 변경**
- close_group 액션을 통해 그룹의 상태를 변경하여 더 이상 새로운 참여자를 받지 않도록 설정

**7️⃣ 사용자 참여 가능성 검증**
- 사용자가 이미 활성 상태(is_active==True)로 참여하고 있는 그룹을 제외하고 그룹 목록을 반환

**8️⃣ 보안 및 권한 관리**
- BasicAuthentication과 SessionAuthentication을 통해 사용자 인증 관리, IsOwnerOrReadOnly 권한 클래스를 사용하여 그룹 소유자만 수정 권한 부여
  

<br/><br/>

## 🍙 백엔드 주요 기능 응답 확인

| <img width="300" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/092ea509-35d5-491b-aced-47ed477f1239"/> | <img width="400" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/ab21662a-8203-4395-9842-20cec571714c"/> | <img width="400" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/9f17aabf-5bf6-4eca-a329-9e3efa4b374e"/> |
| --- | --- | --- |
| **1️⃣ 배달 모임 생성(리더벗)** | **2️⃣ 주문 넣기(참여벗)** | **3️⃣ 배달 모임 리스트 나열** |
| 리더벗이 '장소, 최대 인원,시간 제한 등'을 기입하여 모임 생성 | 참여벗이 장바구니 캡쳐본으로 주문을 넣을시 주문 생성 | 현재 공구 중인 배달 게시물을 피드의 형태로 나열 |

<br/>

✅ 웹 서비스 주소 (배포 완료): http://18.116.163.161/ (엔드포인트는 상이함)

<br/><br/>

## 🍙 백엔드 폴더구조

```sh
babewha
 ┣ babewha
 ┃ ┣ __pycache__
 ┃ ┃ ┣ middleware.cpython-311.pyc
 ┃ ┃ ┣ settings.cpython-311.pyc
 ┃ ┃ ┣ urls.cpython-311.pyc
 ┃ ┃ ┣ wsgi.cpython-311.pyc
 ┃ ┃ ┗ __init__.cpython-311.pyc
 ┃ ┣ asgi.py
 ┃ ┣ settings.py
 ┃ ┣ urls.py
 ┃ ┣ wsgi.py
 ┃ ┗ __init__.py
 ┣ groups
 ┃ ┣ migrations
 ┃ ┃ ┣ __pycache__
 ┃ ┃ ┃ ┣ 0001_initial.cpython-311.pyc
 ┃ ┃ ┃ ┗ __init__.cpython-311.pyc
 ┃ ┃ ┣ 0001_initial.py
 ┃ ┃ ┗ __init__.py
 ┃ ┣ __pycache__
 ┃ ┃ ┣ admin.cpython-311.pyc
 ┃ ┃ ┣ apps.cpython-311.pyc
 ┃ ┃ ┣ forms.cpython-311.pyc
 ┃ ┃ ┣ models.cpython-311.pyc
 ┃ ┃ ┣ permissions.cpython-311.pyc
 ┃ ┃ ┣ serializers.cpython-311.pyc
 ┃ ┃ ┣ urls.cpython-311.pyc
 ┃ ┃ ┣ views.cpython-311.pyc
 ┃ ┃ ┗ __init__.cpython-311.pyc
 ┃ ┣ admin.py
 ┃ ┣ apps.py
 ┃ ┣ forms.py
 ┃ ┣ models.py
 ┃ ┣ permissions.py
 ┃ ┣ serializers.py
 ┃ ┣ tests.py
 ┃ ┣ urls.py
 ┃ ┣ views.py
 ┃ ┗ __init__.py
 ┣ order
 ┃ ┣ migrations
 ┃ ┃ ┣ __pycache__
 ┃ ┃ ┃ ┣ 0001_initial.cpython-311.pyc
 ┃ ┃ ┃ ┗ __init__.cpython-311.pyc
 ┃ ┃ ┣ 0001_initial.py
 ┃ ┃ ┗ __init__.py
 ┃ ┣ __pycache__
 ┃ ┃ ┣ admin.cpython-311.pyc
 ┃ ┃ ┣ apps.cpython-311.pyc
 ┃ ┃ ┣ models.cpython-311.pyc
 ┃ ┃ ┣ permissions.cpython-311.pyc
 ┃ ┃ ┣ serializers.cpython-311.pyc
 ┃ ┃ ┣ urls.cpython-311.pyc
 ┃ ┃ ┣ views.cpython-311.pyc
 ┃ ┃ ┗ __init__.cpython-311.pyc
 ┃ ┣ admin.py
 ┃ ┣ apps.py
 ┃ ┣ forms.py
 ┃ ┣ models.py
 ┃ ┣ permissions.py
 ┃ ┣ serializers.py
 ┃ ┣ tests.py
 ┃ ┣ urls.py
 ┃ ┣ views.py
 ┃ ┗ __init__.py
 ┣ payment
 ┃ ┣ __pycache__
 ┃ ┃ ┣ admin.cpython-311.pyc
 ┃ ┃ ┣ apps.cpython-311.pyc
 ┃ ┃ ┣ models.cpython-311.pyc
 ┃ ┃ ┣ serializers.cpython-311.pyc
 ┃ ┃ ┣ urls.cpython-311.pyc
 ┃ ┃ ┣ utils.cpython-311.pyc
 ┃ ┃ ┣ views.cpython-311.pyc
 ┃ ┃ ┗ __init__.cpython-311.pyc
 ┃ ┣ admin.py
 ┃ ┣ apps.py
 ┃ ┣ models.py
 ┃ ┣ serializers.py
 ┃ ┣ tests.py
 ┃ ┣ urls.py
 ┃ ┣ utils.py
 ┃ ┣ views.py
 ┃ ┗ __init__.py
 ┣ users
 ┃ ┣ migrations
 ┃ ┃ ┣ __pycache__
 ┃ ┃ ┃ ┣ 0001_initial.cpython-311.pyc
 ┃ ┃ ┃ ┗ __init__.cpython-311.pyc
 ┃ ┃ ┣ 0001_initial.py
 ┃ ┃ ┗ __init__.py
 ┃ ┣ template
 ┃ ┃ ┗ users
 ┃ ┃ ┃ ┗ profile_view.html
 ┃ ┣ __pycache__
 ┃ ┃ ┣ admin.cpython-311.pyc
 ┃ ┃ ┣ apps.cpython-311.pyc
 ┃ ┃ ┣ managers.cpython-311.pyc
 ┃ ┃ ┣ models.cpython-311.pyc
 ┃ ┃ ┣ serializers.cpython-311.pyc
 ┃ ┃ ┣ urls.cpython-311.pyc
 ┃ ┃ ┣ views.cpython-311.pyc
 ┃ ┃ ┗ __init__.cpython-311.pyc
 ┃ ┣ admin.py
 ┃ ┣ apps.py
 ┃ ┣ managers.py
 ┃ ┣ models.py
 ┃ ┣ serializers.py
 ┃ ┣ tests.py
 ┃ ┣ urls.py
 ┃ ┣ views.py
 ┃ ┗ __init__.py
 ┣ __pycache__
 ┃ ┗ manage.cpython-311.pyc
 ┣ .env
 ┣ .gitignore
 ┣ manage.py
 ┗ requirement.txt

<br/><br/><br/><br/>
