# 03. 에이전트 개발

이 모듈에서는 다양한 기능을 가진 AI 에이전트를 생성하고 배포하는 방법을 학습합니다.

## 📋 목차

- [에이전트 개요](#에이전트-개요)
- [ModelRouterAgent 생성](#modelrouteragent-생성)
- [FileSearchAgent 생성](#filesearchagent-생성)
- [WebSearchAgent 생성](#websearchagent-생성)
- [에이전트 배포 및 호출](#에이전트-배포-및-호출)
- [다음 단계](#다음-단계)

## 🎯 학습 목표

- Microsoft Foundry 에이전트의 핵심 개념 이해
- Model Router 기반 에이전트 구축
- File Search 기능을 활용한 문서 기반 에이전트 생성
- Web Search 기능을 활용한 실시간 정보 검색 에이전트 생성
- 에이전트 배포 및 프로그래매틱 호출 방법 학습

## ⏱️ 예상 소요 시간

약 30분

---

## 에이전트 개요

### Microsoft Foundry Agent란?

AI Agent는 사용자의 요청을 이해하고, 필요한 도구를 활용하여 작업을 수행하는 지능형 시스템입니다.

### 주요 구성 요소

```
Agent = Model + Instructions + Tools + Knowledge
```

- **Model**: 기본 언어 모델 (GPT-5.1, Claude 등)
- **Instructions**: 에이전트의 행동 지침 및 페르소나
- **Tools**: File Search, Web Search, Function Calling 등
- **Knowledge**: 연결된 지식 베이스 (Foundry IQ)

### 에이전트 타입

| 타입 | 설명 | 사용 사례 |
|------|------|-----------|
| **Conversational** | 대화형 에이전트 | 챗봇, 고객 지원 |
| **Task-oriented** | 작업 중심 에이전트 | 데이터 분석, 문서 생성 |
| **Retrieval-augmented** | 검색 기반 에이전트 | 지식 베이스 QA |
| **Multi-agent** | 다중 에이전트 협업 | 복잡한 워크플로우 |

---

## ModelRouterAgent 생성

Model Router를 활용하여 지능적으로 모델을 선택하는 에이전트를 만들어봅니다.

### 단계별 가이드

1. **Agents 섹션 이동**
   - Foundry 포털 우측 상단 메뉴에서 **Build**를 선택합니다.
   - **Agents** 메뉴를 클릭합니다.
   
   ![Build > Agents 메뉴](./assets/03-01-agents-menu.png)

2. **새 에이전트 생성**
   - **+ Create agent** 또는 **New agent** 버튼을 클릭합니다.
   
   ![Create agent 버튼](./assets/03-02-create-agent.png)

3. **Playground에서 구성**
   ```
   Agent name: ModelRouterAgent
   Model: model-router (이전에 배포한 Model Router)
   ```

   **Instructions 설정**:
   ```
   당신은 질문에 답변하는 에이전트입니다.
   요청의 복잡도와 요구사항에 따라 가장 적절한 모델을 사용하세요.
   항상 명확하고 정확하며 도움이 되는 답변을 제공하세요.
   ```
   
   **Save** 버튼을 클릭하여 저장합니다.

   ![에이전트 기본 설정](./assets/03-03-agent-basic-settings.png)

4. **에이전트 테스트**

   **Chat 탭에서 다음 질문들을 테스트해봅니다:**

   ```
   사용자: 안녕
   ```
   → 간단한 인사이므로 경량 모델 사용

   ```
   사용자: 너는 언제까지의 데이터로 학습되어있니?
   ```
   → 모델 정보 질문, 기본 모델로 답변

   ```
   사용자: microsoft foundry new portal 실습을 위한 실습 가이드를 만들어줘. 
   foundry models, model-router, foundry agents, foundry tools, foundry knowledge, 
   foundry control plane 등을 모두 foundry portal에서 실습하는 가이드가 필요해
   ```
   → 복잡한 문서 생성 요청이므로 고성능 모델 사용
   
   ![Chat 탭에서 테스트](./assets/03-05-agent-chat-test.png)

5. **추가 탭 탐색**

   **YAML 탭**:
   - 에이전트 설정을 YAML 형식으로 확인
   - Infrastructure as Code로 관리 가능
   
   ![YAML 탭 화면](./assets/03-06-agent-yaml.png)
   
   **Code 탭**:
   - 에이전트를 코드로 호출하는 샘플 확인
   - Python, JavaScript, C# 등 다양한 언어 지원
   
   ![Code 탭 화면](./assets/03-07-agent-code.png)

   **Traces 탭**:
   - 에이전트 실행 과정 추적
   - 모델 선택 결정 확인
   - 성능 및 비용 분석

   **Tracing 활성화**를 위해서 **App Insigts 생성 및 연결**이 필요합니다.
   **Agent Tracing**은 Foundry(New)의 **Sweden Central**에서만 가능합니다.
   
   ![Traces 탭 화면 - Connect](./assets/03-08-agent-traces-connect.png)

   ![Traces 탭 화면 - Create](./assets/03-08-agent-traces-create.png)

   ![Traces 탭 화면 - Traces](./assets/03-08-agent-traces.png)

   ![Traces 탭 화면 - Traces - Details](./assets/03-08-agent-traces-details.png)

   **Monitor 탭**:
   - 실시간 메트릭 모니터링
   - 에러율, 응답 시간 등 확인
   
   ![Monitor 탭 화면](./assets/03-09-agent-monitor.png)

6. **에이전트 저장**
   - **Save** 버튼을 클릭하여 에이전트를 저장합니다.

### ✅ 확인 사항

- ModelRouterAgent가 Agents 목록에 나타나는지 확인
- 다양한 복잡도의 질문에 적절히 응답하는지 테스트
- Traces에서 어떤 모델이 선택되었는지 확인

---

## FileSearchAgent 생성

파일 검색 기능을 활용하여 업로드된 문서에서 정보를 찾는 에이전트를 만듭니다.

### 단계별 가이드

1. **새 에이전트 생성**
   ```
   Agent name: FileSearchAgent
   Model: gpt-5.1
   ```

2. **Instructions 설정**

   Playground의 **Instructions** 섹션에 다음을 입력:
   ```
   너는 Tools에 등록된 File search 기반으로 답변하는 에이전트입니다.
   
   중요 규칙:
   1. 반드시 업로드된 파일의 내용을 기반으로만 답변하세요
   2. 파일에 없는 정보는 "제공된 문서에서 해당 정보를 찾을 수 없습니다"라고 답변하세요
   3. 답변 시 출처 파일명을 언급하세요
   4. 정확한 인용을 사용하세요
   ```
   
   **Save** 버튼을 클릭하여 저장합니다.

   ![FileSearchAgent 생성](./assets/03-10-filesearch-create.png)

3. **File Search Tool 추가**

   - **Tools** 섹션에서 **+ Add** 버튼을 클릭합니다.
   
   - **File Search** 옵션을 선택합니다.
   - File Search가 Tools 목록에 추가되었는지 확인합니다.
   
   ![File Search 도구 선택](./assets/03-13-filesearch-tool-selection.png)

4. **파일 업로드**

   - **Tools > File Search** 섹션에서 **Attach files** 버튼을 클릭합니다.
   
   ![Attach files 버튼](./assets/03-14-filesearch-attach-files.png)
   
   - `knowledge-base.json` 파일을 업로드합니다.
   - 파일이 정상적으로 업로드되었는지 확인합니다.
   
   ![파일 업로드 완료](./assets/03-15-filesearch-file-uploaded.png)

5. **에이전트 저장**
   - **Save** 버튼을 클릭합니다.

6. **에이전트 테스트**

   **Chat 탭에서 다음 질문들을 시도해봅니다:**

   ```
   사용자: 서핑하기 좋은 곳을 추천해줘
   ```
   예상 답변: 양양 서피비치와 제주 중문색달해변 추천

   ```
   사용자: 힐링하기 좋은 해변을 찾아줘
   ```
   예상 답변: 강릉 경포해변과 태안 만리포해변 소개

   ```
   사용자: 사계절 가능한 서핑 장소는?
   ```
   예상 답변: 제주 중문색달해변
   
   ![FileSearchAgent 테스트](./assets/03-16-filesearch-chat-test.png)

7. **Traces 확인**

   - **Traces** 탭에서 File Search가 어떻게 작동했는지 확인합니다.
   - 검색된 문서 조각(chunks)과 관련성 점수를 확인할 수 있습니다.
   
   ![File Search Traces 확인](./assets/03-17-filesearch-traces.png)

   ![File Search Traces 확인](./assets/03-17-filesearch-traces-2.png)

### ✅ 확인 사항

- File Search tool이 활성화되어 있는지 확인
- 업로드된 파일 내용을 기반으로 정확히 답변하는지 테스트
- 파일에 없는 정보에 대해서는 모른다고 답하는지 확인

---

## WebSearchAgent 생성

실시간 웹 검색을 수행하여 최신 정보를 제공하는 에이전트를 만듭니다.

### 단계별 가이드

1. **새 에이전트 생성**
   ```
   Agent name: WebSearchAgent
   Model: gpt-4.1
   ```
   
   **Instructions 설정**

   ```
   너는 Tools에 등록된 Web search 기반으로 답변하는 에이전트입니다.
   
   중요 규칙:
   1. 최신 정보가 필요한 질문에는 반드시 웹 검색을 사용하세요
   2. 검색 결과를 기반으로 정확하고 최신의 정보를 제공하세요
   3. 답변 시 출처 URL을 포함하세요
   4. 여러 출처의 정보를 종합하여 균형잡힌 답변을 제공하세요
   5. 검색 결과가 불충분하면 추가 검색을 수행하세요
   ```
   
   ![WebSearchAgent 생성](./assets/03-18-websearch-create.png)

2. **Web Search Tool 추가**

   - **Tools** 섹션에서 **+ Add** 버튼을 클릭합니다.
   - **Web search** 옵션을 선택합니다.
   - Web Search가 활성화되었는지 확인합니다.
   
   ![Web search 도구 추가](./assets/03-20-websearch-add-tool.png)

3. **에이전트 저장**
   - **Save** 버튼을 클릭합니다.

4. **에이전트 테스트**

   **Chat 탭에서 최신 정보 질문을 테스트합니다:**

   ```
   사용자: Microsoft Ignite 2025에서 발표된 Microsoft Foundry의 주요 신기능을 요약해줘
   ```
   → 웹 검색을 통해 최신 발표 내용 검색 및 요약

   ```
   사용자: Foundry IQ에 대해서 좀더 자세하게 알려줘
   ```
   → Foundry IQ의 최신 기능 및 특징 설명

   ```
   사용자: 기존처럼 Azure AI Search를 사용하는 것 대비 어떤 점이 나아지는거니?
   ```
   → 비교 분석 및 장점 설명
   
   ![WebSearchAgent 테스트](./assets/03-21-websearch-chat-test.png)

5. **Traces 분석**

   - **Traces** 탭에서 웹 검색 과정 확인:
     - 검색 쿼리
     - 검색된 웹사이트 목록
     - 추출된 정보
     - 최종 응답 생성 과정
   
   ![Web Search Traces 확인](./assets/03-22-websearch-traces.png)

   ![Web Search Traces 확인](./assets/03-22-websearch-traces-2.png)

### 💡 Web Search 활용 팁

- **구체적인 질문**: 명확한 검색 결과를 위해 질문을 구체적으로
- **최신 정보**: 뉴스, 이벤트, 기술 발표 등에 유용
- **비교 분석**: 여러 출처의 정보를 종합하여 균형잡힌 답변 제공
- **출처 확인**: 답변의 신뢰성을 위해 출처 URL 확인

### ✅ 확인 사항

- Web Search tool이 활성화되어 있는지 확인
- 최신 정보를 정확하게 검색하고 요약하는지 테스트
- 출처 URL이 응답에 포함되어 있는지 확인

---

## 에이전트 배포 및 호출

생성한 에이전트를 배포하고 외부에서 호출하는 방법을 학습합니다.

### Publish (게시)

1. **Preview 단계**

   - Playground에서 **Preview** 버튼을 클릭합니다.
   - 다음 옵션들을 확인할 수 있습니다:
     - **Preview agent**: 웹 인터페이스로 에이전트 미리보기
     - **View sample app code**: 샘플 애플리케이션 코드 확인
   
   ![Preview 버튼](./assets/03-23-agent-preview-button.png)

   ![Preview](./assets/03-23-agent-preview.png)

2. **Publish 실행**

   - **Publish agent** 버튼을 클릭합니다.
   
   ![Publish agent 버튼 클릭](./assets/03-24-agent-publish-agent.png)

   - **Publish** 버튼을 클릭합니다.
   
   ![Publish 버튼 클릭](./assets/03-24-agent-publish.png)
   
   - 게시 설정 확인:
     ```
     Version: 1.0
     Status: Published
     Endpoint: [자동 생성된 엔드포인트]
     ```
   
   ![게시 완료 확인](./assets/03-25-agent-published.png)

### 에이전트 호출하기

#### 1. Azure CLI 로그인

먼저 Azure에 로그인합니다:

```bash
az login 
```

멀티 테넌트를 사용하는 경우, 테넌트ID를 지정합니다.
```bash
az login --tenant <tenant-id>
```

#### 2. Python SDK를 사용한 호출

> 💡 **실습 팁**: 아래 코드는 참고용입니다. 실제 실습 시에는 이 저장소의 루트 경로에 있는 `invokeAgent.py` 파일을 열어 `FOUNDRY_ENDPOINT`와 `AGENT_NAME` 값을 본인 환경에 맞게 수정한 후 실행하세요.

`invokeAgent.py` 파일 예시:

```python
# Microsoft Foundry Agent Invocation using Activity Protocol
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# TODO: Update these values with your actual Microsoft Foundry details
# Get these from: https://ai.azure.com → Your Project → Deployments
FOUNDRY_ENDPOINT = "https://<foundry-resource-name>.services.ai.azure.com/api/projects/<project-name>"
AGENT_NAME = "ModelRouterAgent"  # 호출할 에이전트 이름
API_VERSION = "2025-11-15-preview"

# Create OpenAI client with Azure authentication
client = OpenAI(
    api_key=get_bearer_token_provider(
        DefaultAzureCredential(), 
        "https://ai.azure.com/.default"
    ),
    base_url=f"{FOUNDRY_ENDPOINT}/applications/{AGENT_NAME}/protocols/openai",
    default_query={"api-version": API_VERSION}
)

try:
    # Call the agent using responses API
    response = client.responses.create(
        input="제주도 2박 3일 여행 코스 추천해줘"
    )
    
    print(f"Response: {response.output_text}")
    
except Exception as e:
    print(f"Error: {e}")
    print("\n🔍 Troubleshooting:")
    print("1. Check your endpoint URL at https://ai.azure.com")
    print("2. Verify the project name and agent name exist")
    print("3. Ensure you're logged in: az login")
    print("4. Confirm the agent is deployed and running")
```

#### 3. 엔드포인트 정보 확인

Foundry 포털에서 엔드포인트 정보를 확인하는 방법:

1. Build > Agents에서 게시된 에이전트 선택
2. **Publish** 버튼 클릭 후, **View details**을 클릭
3. 다음 정보 복사:
   - Agent application
   - Activity Protocol endpoint
   - Response API endpoint

![Endpoint 정보 확인](./assets/03-26-agent-endpoint.png)

#### 4. 실행

```bash
# 가상환경 생성 (선택사항)
python -m venv .venv
source .venv/bin/activate  # Windows: venv\Scripts\activate

# 필요한 패키지 설치 (pre-release 버전 포함)
pip install openai azure-identity
pip install --pre azure-ai-projects

# 스크립트 실행
python invokeAgent.py
```

### 🔐 인증 옵션

#### Option 1: DefaultAzureCredential (권장)
```python
from azure.identity import DefaultAzureCredential
credential = DefaultAzureCredential()
```

#### Option 2: Managed Identity (Azure 리소스에서 실행 시)
```python
from azure.identity import ManagedIdentityCredential
credential = ManagedIdentityCredential()
```

#### Option 3: Service Principal
```python
from azure.identity import ClientSecretCredential
credential = ClientSecretCredential(
    tenant_id="YOUR_TENANT_ID",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET"
)
```

### ✅ 확인 사항

- 에이전트가 성공적으로 게시되었는지 확인
- Python 스크립트가 에러 없이 실행되는지 확인
- 응답이 예상대로 반환되는지 확인

---

## 📚 추가 리소스

- [Microsoft Foundry Agents 개요](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview?view=foundry)
- [Agent SDK 문서](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/develop/sdk-overview?view=foundry&pivots=programming-language-python)
- [File Search 가이드](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/tools/file-search?view=foundry&pivots=python)
- [Web Search 통합](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/tools/web-search?view=foundry&pivots=python)

---

## 다음 단계

다양한 에이전트를 만들어보았습니다! 이제 Foundry IQ를 사용하여 고급 지식 기반을 구축해봅시다:

➡️ **[04. Foundry IQ](./04-foundry-iq.md)**: AI Search와 Blob Storage를 활용한 지식 기반 구축을 학습합니다.

---

[← 이전: 모델 및 배포](./02-models.md) | [메인으로](./README.md) | [다음: Foundry IQ →](./04-foundry-iq.md)
