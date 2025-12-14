# Code Guide - Microsoft Foundry 코드 기반 실습

> ⚠️ **작업 중 (Work in Progress)**: 이 가이드는 현재 개발 중입니다. 일부 내용이 불완전하거나 변경될 수 있습니다.

Python 코드와 Azure CLI를 사용하여 Microsoft Foundry 리소스를 자동화하는 실습 가이드입니다.

## 📖 코드 기반 실습 특징

- ✅ **자동화**: Python 코드로 리소스 생성 및 관리
- ✅ **재현 가능**: 코드를 저장하여 언제든 재실행
- ✅ **스크립트 작성**: 실무에 바로 적용 가능한 코드 작성
- ✅ **Infrastructure as Code**: Azure CLI와 REST API 활용

## 🎯 사전 요구사항

### 필수
- Python 3.8 이상
- Azure CLI (`az --version`으로 확인)
- Azure 구독 및 로그인 (`az login`)
- Jupyter Notebook 실행 환경

### 권장
- **GitHub Codespaces** 사용 (모든 도구가 사전 설치됨)
- VS Code + Jupyter Extension
- Python 가상 환경 (venv)

## 📚 실습 모듈 (Jupyter Notebooks)

1. **[01-setup.ipynb](./01-setup.ipynb)** - Resource Group 및 Foundry 리소스 생성
2. **[02-models.ipynb](./02-models.ipynb)** - 모델 배포 및 Model Router 구성
3. **[03-agents.ipynb](./03-agents.ipynb)** - 다양한 에이전트 구축 및 배포
4. **[04-foundry-iq.ipynb](./04-foundry-iq.ipynb)** - AI Search 및 지식 베이스 구축
5. **[05-workflows.ipynb](./05-workflows.ipynb)** - Sequential, Group Chat, Human-in-loop 워크플로우
6. **[06-evaluations.ipynb](./06-evaluations.ipynb)** - 에이전트 성능 평가
7. **[07-control-plane.ipynb](./07-control-plane.ipynb)** - 운영 모니터링 및 관리

## 🔧 추가 스크립트

- **[invokeAgent.py](./invokeAgent.py)** - 배포된 Agent를 외부에서 호출하는 예제
- **[invokeWorkflow.py](./invokeWorkflow.py)** - 배포된 Workflow를 프로그래밍 방식으로 실행하는 예제
- **[knowledge-base.json](./knowledge-base.json)** - FileSearchAgent 실습용 샘플 데이터

## 🚀 시작하기

### 1️⃣ 환경 설정 (로컬 환경)
```bash
# 가상환경 생성 및 활성화
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 필요한 패키지 설치
pip install azure-identity azure-ai-projects openai requests
```

### 2️⃣ Azure 로그인
```bash
az login
az account set --subscription "Your-Subscription-Name"
```

### 3️⃣ 노트북 실행
1. **[01-setup.ipynb](./01-setup.ipynb)** 열기
2. 첫 셀의 `FOUNDRY_NAME` 변수를 고유한 이름으로 변경 (예: `foundry-myname`)
3. 셀을 순서대로 실행

> ⚠️ **중요**: `FOUNDRY_NAME`은 전역적으로 고유해야 합니다. 본인의 이름이나 이니셜을 포함하세요.

### 4️⃣ GitHub Codespaces 사용 (권장)
1. 이 리포지토리를 포크
2. "Code" → "Create codespace on main" 클릭
3. Codespace가 열리면 바로 노트북 실행 가능

## 💡 학습 팁

- **순차적 학습**: 각 노트북은 이전 모듈에서 생성한 리소스를 사용합니다
- **환경 변수 공유**: `.foundry_config.json` 파일로 설정 값을 저장하고 공유합니다
- **에러 처리**: 각 셀의 응답 코드를 확인하고 에러 메시지를 읽어보세요
- **코드 수정**: 제공된 코드를 자유롭게 수정하며 학습하세요

## 🔄 포털 가이드와의 관계

- **동일한 목표**: 포털 가이드와 코드 가이드는 같은 결과물을 만듭니다
- **학습 순서**: 포털로 개념을 익힌 후 코드로 자동화하는 것을 권장합니다
- **선택 가능**: 원하는 방식만 선택하여 실습할 수 있습니다

## 📚 관련 문서

- [Azure AI Foundry SDK for Python](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Azure CLI Reference](https://learn.microsoft.com/cli/azure/)
- [Foundry REST API Documentation](https://learn.microsoft.com/rest/api/aiservices/)

## 💡 다음 단계

코드 실습을 완료한 후:
- 생성한 리소스를 [포털](https://ai.azure.com)에서 확인해보세요
- `invokeAgent.py`와 `invokeWorkflow.py` 스크립트를 실행해보세요
- 자신만의 에이전트나 워크플로우를 만들어보세요

---

**시작하기**: [01-setup.ipynb](./01-setup.ipynb)
