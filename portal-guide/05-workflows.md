# 05. 워크플로우

이 모듈에서는 여러 에이전트를 조합하여 복잡한 작업을 수행하는 워크플로우를 구축하는 방법을 학습합니다.

## 📋 목차

- [워크플로우 개요](#워크플로우-개요)
- [Sequential Workflow](#sequential-workflow)
- [Group Chat Workflow](#group-chat-workflow)
- [Human-in-loop Workflow](#human-in-loop-workflow)
- [다음 단계](#다음-단계)

## 🎯 학습 목표

- Microsoft Foundry 워크플로우의 핵심 개념 이해
- Sequential Workflow를 통한 순차적 작업 흐름 구축
- Group Chat Workflow를 통한 다중 에이전트 협업 구현
- Human-in-loop 패턴을 통한 사람 개입 지점 설정
- 워크플로우 배포 및 프로그래매틱 호출

## ⏱️ 예상 소요 시간

약 20분

---

## 워크플로우 개요

### 워크플로우란?

워크플로우는 여러 AI 에이전트를 조율하여 복잡한 작업을 단계적으로 수행하는 자동화 시스템입니다.

### 워크플로우 타입

```
Single Agent → Sequential Workflow → Group Chat → Human-in-loop
(단순)                                                    (복잡)
```

| 타입 | 설명 | 사용 사례 |
|------|------|-----------|
| **Sequential** | 순차적 실행 | 데이터 파이프라인, 문서 처리 |
| **Parallel** | 병렬 실행 | 동시 분석, 다중 검색 |
| **Group Chat** | 에이전트 간 대화 | 협업 문제 해결, 의사결정 |
| **Human-in-loop** | 사람 개입 | 승인 프로세스, 검증 |
| **Conditional** | 조건부 분기 | 동적 라우팅, 에러 처리 |

### 워크플로우 구성 요소

```python
Workflow {
    Agents: [Agent1, Agent2, Agent3]
    Flow: Sequential | Parallel | Conditional
    Inputs: User request, Context
    Outputs: Final result, Intermediate results
    Handoffs: Agent transitions
    Termination: Completion condition
}
```

---

## Sequential Workflow

순차적으로 실행되는 에이전트 체인을 구축합니다. 여행 계획 수립 워크플로우를 예시로 사용합니다.

### 필요한 에이전트 생성

먼저 워크플로우에서 사용할 에이전트들을 생성합니다.

#### 1. TravelPlannerAgent

```
Agent name: TravelPlannerAgent
Description: 여행 목적지와 일정을 기획하는 에이전트
Model: gpt-5.1

Instructions:
당신은 여행 계획 전문가입니다.

역할:
1. 사용자의 여행 요구사항을 분석합니다
2. 목적지의 주요 관광지, 맛집, 숙소를 추천합니다
3. 일자별 여행 일정을 구체적으로 작성합니다
4. 예상 비용과 준비물을 제시합니다

출력 형식:
- 목적지 개요
- 일자별 일정 (아침/점심/저녁 활동)
- 추천 숙소
- 예상 비용
- 준비물 목록

다음 에이전트에게 넘길 정보: 전체 여행 계획
```

#### 2. LocalAgent

```
Agent name: LocalAgent
Description: 현지 정보를 추가하는 에이전트
Model: gpt-5.1

Tools: Web search (활성화)

Instructions:
당신은 현지 정보 전문가입니다.

역할:
1. 이전 에이전트의 여행 계획을 받습니다
2. Web search를 사용하여 최신 현지 정보를 검색합니다
3. 실시간 정보를 추가합니다:
   - 현재 날씨 및 기후
   - 현지 축제 및 이벤트
   - 교통 정보 (노선, 요금, 소요시간)
   - 영업시간 및 예약 정보
   - 현지 문화 및 주의사항

출력 형식:
- 원래 일정 + 현지 정보 보강
- 교통편 상세 정보
- 예약 필요 장소 목록
- 현지 팁

다음 에이전트에게 넘길 정보: 현지 정보가 추가된 여행 계획
```

#### 3. TravelSummaryAgent

```
Agent name: TravelSummaryAgent
Description: 여행 계획을 요약하고 최종 체크리스트를 만드는 에이전트
Model: gpt-5.1

Instructions:
당신은 여행 계획 정리 전문가입니다.

역할:
1. 이전 에이전트들의 정보를 종합합니다
2. 실행 가능한 최종 계획으로 정리합니다
3. 체크리스트를 생성합니다

출력 형식:
📋 여행 요약
- 목적지: 
- 기간:
- 예산:

📅 일정 요약 (한눈에 보는 일정)

✅ 출발 전 체크리스트
- [ ] 항목1
- [ ] 항목2

🎒 준비물 체크리스트

📞 긴급 연락처 및 유용한 정보

최종 출력: 프린트 가능한 여행 가이드
```

### Sequential Workflow 생성

1. **Workflows 섹션 이동**

   - Foundry 포털 우측 상단 메뉴에서 **Build**를 선택합니다.
   - **Workflows** 메뉴를 클릭합니다.
   
   ![Build > Workflows 메뉴](../assets/05-01-workflows-menu.png)

2. **새 워크플로우 생성**

   - **+ Create workflow** 또는 **New workflow** 버튼을 클릭합니다.
   - **Sequential Workflow**를 선택합니다.
   
   ![Create workflow 버튼](../assets/05-02-create-workflow.png)

   ![Create workflow 버튼2](../assets/05-02-create-workflow-2.png)

3. **에이전트 추가**

   순서대로 에이전트를 추가합니다:
   
   ![Select an agent to invoke 버튼](../assets/05-04-workflow-add-agent.png)

   ```
   Step 1: TravelPlannerAgent
     ↓
   Step 2: LocalAgent
     ↓
   Step 3: TravelSummaryAgent
   ```

   - 각 단계에서 **Select an agent to invoke** 버튼을 클릭하여 에이전트를 선택합니다.

   ![Select an agent to invoke 버튼1](../assets/05-04-workflow-add-agent1.png)
   
   ![Select an agent to invoke 버튼2](../assets/05-04-workflow-add-agent2.png)

   ![Select an agent to invoke 버튼3](../assets/05-04-workflow-add-agent3.png)

   ![전체 workflow](../assets/05-02-overall-workflow.png)

4. **워크플로우 저장**

   - **Save** 버튼을 클릭합니다.

   ![Workflow 이름 등록](../assets/05-02-workflow-save.png)

   ![Workflow 이름 저장](../assets/05-02-workflow-saved.png)

### 워크플로우 테스트

1. **Preview 모드**

   - **Preview** 버튼을 클릭합니다.

2. **테스트 질문**

   ```
   사용자: 제주도 2박 3일 여행 계획 세우는 것을 도와줘.
   ```

3. **실행 과정 관찰**

   각 단계에서의 출력을 확인합니다:

   - **Step 1 (TravelPlannerAgent)**: 기본 여행 일정 생성
   - **Step 2 (LocalAgent)**: 현지 정보 추가 (날씨, 교통, 이벤트)
   - **Step 3 (TravelSummaryAgent)**: 최종 요약 및 체크리스트

   ![Workflow Preview](../assets/05-05-workflow-preview.png)

4. **Traces 확인**

   - 각 에이전트의 실행 시간
   - 에이전트 간 데이터 전달
   - 최종 출력 생성 과정

### 워크플로우 배포 및 호출

1. **Publish**

   - **Publish** 버튼을 클릭합니다.

   ![Workflow Publish-1](../assets/05-05-workflow-publish1.png)

   - 버전을 확인하고 게시합니다.

   ![Workflow Publish-2](../assets/05-05-workflow-publish2.png)

   ![Workflow Publish-3](../assets/05-05-workflow-publish3.png)

2. **Python SDK로 호출**

   > 💡 **실습 팁**: 아래 코드는 참고용입니다. 실제 실습 시에는 이 저장소의 루트 경로에 있는 `invokeWorkflow.py` 파일을 열어 `PROJECT_ENDPOINT`와 `WORKFLOW_NAME` 값을 본인 환경에 맞게 수정한 후 실행하세요.

   `invokeWorkflow.py` 파일 예시:

   ```python
   # Microsoft Foundry Workflow Invocation using Foundry SDK
   # Before running: pip install --pre azure-ai-projects>=2.0.0b1
   from azure.identity import DefaultAzureCredential
   from azure.ai.projects import AIProjectClient
   from azure.ai.projects.models import ResponseStreamEventType
   
   # Project configuration
   PROJECT_ENDPOINT = "https://<foundry-resource-name>.services.ai.azure.com/api/projects/proj-default"
   WORKFLOW_NAME = "Sequential-Workflow"
   WORKFLOW_VERSION = "1"  # 게시된 버전으로 업데이트
   
   # Create AI Project client
   project_client = AIProjectClient(
       endpoint=PROJECT_ENDPOINT,
       credential=DefaultAzureCredential(),
   )
   
   with project_client:
       workflow = {
           "name": WORKFLOW_NAME,
           "version": WORKFLOW_VERSION,
       }
       
       # Get OpenAI client from project
       openai_client = project_client.get_openai_client()
   
       # Create a conversation
       conversation = openai_client.conversations.create()
       print(f"Created conversation (id: {conversation.id})")
   
       # Call the workflow with streaming
       print(f"\nCalling workflow: {WORKFLOW_NAME}...\n")
       stream = openai_client.responses.create(
           conversation=conversation.id,
           extra_body={"agent": {"name": workflow["name"], "type": "agent_reference"}},
           input="제주도 2박 3일 여행 일정 짜줘",
           stream=True,
           metadata={"x-ms-debug-mode-enabled": "1"},
       )
   
       # Process streaming events
       for event in stream:
           if event.type == ResponseStreamEventType.RESPONSE_OUTPUT_TEXT_DONE:
               print("\t", event.text)
           elif event.type == ResponseStreamEventType.RESPONSE_OUTPUT_ITEM_ADDED and event.item.type == "workflow_action":
               print(f"\n{'='*60}")
               print(f"Actor - '{event.item.action_id}':")
               print(f"{'='*60}")
           elif event.type == ResponseStreamEventType.RESPONSE_OUTPUT_ITEM_DONE and event.item.type == "workflow_action":
               print(f"\n✓ Workflow Item '{event.item.action_id}' is '{event.item.status}'")
               print(f"  (previous item was: '{event.item.previous_action_id}')")
           elif event.type == ResponseStreamEventType.RESPONSE_OUTPUT_TEXT_DELTA:
               print(event.delta, end="", flush=True)
   
       # Clean up
       print("\n\n✅ Workflow completed!")
       openai_client.conversations.delete(conversation_id=conversation.id)
       print("Conversation deleted")
   ```

3. **실행**

   ```bash
   pip install --pre azure-ai-projects>=2.0.0b1
   python invokeWorkflow.py
   ```

### ✅ 확인 사항

- 모든 에이전트가 순서대로 실행되는지 확인
- 각 에이전트의 출력이 다음 에이전트에 전달되는지 확인
- 최종 출력이 올바르게 생성되는지 확인

---

## Group Chat Workflow

여러 에이전트가 대화를 통해 협업하여 문제를 해결하는 워크플로우입니다.


### 필요한 에이전트 생성

#### 1. StudentAgent

```
Agent name: StudentAgent
Description: 질문에 답변하는 학생 역할
Model: gpt-5.1

Instructions:
너는 문제에 대답하는 에이전트야. 질문이 오면, 항상 답변해줘.

역할:
1. 사용자의 질문을 이해하고 답변을 생성합니다
2. 첫 번째 시도에서는 기본적인 답변을 제공합니다
3. TeacherAgent의 피드백을 받아 답변을 개선합니다
4. 모든 요구사항이 충족될 때까지 답변을 수정합니다

답변 시 고려사항:
- 일정 (날짜, 시간)
- 비용 (예산, 가격)
- 취향 (선호도, 스타일)
- 제약사항 (제한사항, 조건)

개선이 필요하면 TeacherAgent의 피드백을 반영하여 답변을 보완합니다.
```

#### 2. TeacherAgent

```
Agent name: TeacherAgent
Description: 답변을 평가하고 개선을 요청하는 교사 역할
Model: gpt-5.1

Instructions:
너는 답변을 평가하는 에이전트야. 답변이 일정, 비용, 취향 등 다양한 조건에 대한 고려를 했다면 [COMPLETE]이라고 대답해줘. 아니라면, COMPLETE을 표시하지 말고, 수정을 요청해줘.

평가 기준:
1. 일정: 구체적인 날짜, 시간, 기간이 포함되었는가?
2. 비용: 예산, 가격, 비용 정보가 포함되었는가?
3. 취향: 사용자의 선호도나 스타일을 고려했는가?
4. 실용성: 실제로 실행 가능한 계획인가?
5. 완성도: 모든 필요한 정보가 포함되었는가?

응답 형식:
평가 완료 시: "[COMPLETE] 모든 조건이 충족되었습니다."
개선 필요 시: "다음 사항을 보완해주세요: [구체적인 피드백]"

중요: [COMPLETE]는 모든 기준이 충족되었을 때만 사용합니다.
```

### Group Chat Workflow 생성

1. **새 워크플로우 생성**

   - Workflows 섹션에서 **+ Create workflow** 버튼을 클릭합니다.
   - **Group Chat Workflow**를 선택합니다.
   
   ![Group Chat Workflow 생성](../assets/05-09-group-chat-create.png)


2. **에이전트 추가**

   ```
   Participants:
   - StudentAgent
   - TeacherAgent
   
   Termination condition: TeacherAgent가 [COMPLETE]를 응답할 때
   Max turns: 4 (무한 루프 방지)
   ```

   ![여러 에이전트 추가](../assets/05-10-group-chat-agents.png)

3. **대화 흐름 설정**

   ```
   User → StudentAgent → TeacherAgent → StudentAgent → ...
   ```

   - StudentAgent가 먼저 답변을 제공
   - TeacherAgent가 평가 및 피드백
   - [COMPLETE]가 나올 때까지 반복

5. **워크플로우 저장**

   - **Save** 버튼을 클릭합니다.
   
   ![Group Chat Workflow 저장](../assets/05-09-group-chat-save.png)
      
   ![Group Chat Workflow 저장완료](../assets/05-09-group-chat-saved.png)

### 워크플로우 테스트

1. **Preview 모드**

   - **Preview** 버튼을 클릭합니다.

   ![Group Chat Workflow Preview](../assets/05-09-group-chat-preview.png)

2. **테스트 질문**

   ```
   사용자: 제주도 2박 3일 여행 일정을 짜줘.
   ```

3. **대화 흐름 관찰**

   ```
   Turn 1:
   StudentAgent: "제주도 추천 일정입니다. 1일차: 성산일출봉..."
   
   Turn 2:
   TeacherAgent: "비용 정보가 빠져있습니다. 예산을 포함해주세요."
   
   Turn 3:
   StudentAgent: "수정된 일정입니다. 총 예산 50만원... 1일차: 성산일출봉 (입장료 5000원)..."
   
   Turn 4:
   TeacherAgent: "구체적인 시간대가 없습니다. 시간별 일정을 추가해주세요."
   
   Turn 5:
   StudentAgent: "최종 일정입니다. 1일차 오전 9시: 성산일출봉..."
   
   Turn 6:
   TeacherAgent: "[COMPLETE] 모든 조건이 충족되었습니다."
   ```

### 💡 Group Chat 활용 팁

- **역할 분담**: 각 에이전트에 명확한 역할 부여
- **종료 조건**: 무한 루프를 방지하기 위한 명확한 종료 조건
- **최대 턴 수**: 안전장치로 최대 턴 수 설정
- **피드백 구체성**: TeacherAgent의 피드백이 구체적일수록 개선 효과 증가

### ✅ 확인 사항

- 에이전트 간 대화가 자연스럽게 이어지는지 확인
- TeacherAgent의 평가 기준이 적절한지 확인
- [COMPLETE] 조건에서 워크플로우가 종료되는지 확인

---

## Human-in-loop Workflow

사람의 승인이나 입력이 필요한 지점에서 워크플로우를 일시 중지하는 패턴입니다.


### 개념

```
Agent 1 → [Human Approval] → Agent 2 → [Human Input] → Agent 3
```

Human-in-loop는 다음 상황에서 유용합니다:
- 중요한 결정 승인
- 민감한 정보 검증
- 예산 승인
- 개인 선호도 입력

### 워크플로우 설계

1. **에이전트 구성**

   이전에 만든 Sequential Workflow를 기반으로 합니다:

   ```
   TravelPlannerAgent → [사용자 승인] → LocalAgent → TravelSummaryAgent
   ```

2. **Human Approval Point 추가**

   - TravelPlannerAgent 다음에 **Human approval** 단계를 추가합니다.
   - 사용자는 초안 여행 계획을 검토하고:
     - ✅ 승인 → LocalAgent로 진행
     - ❌ 거부 → TravelPlannerAgent로 돌아가서 재생성
     - 📝 수정 요청 → 피드백과 함께 재생성

3. **워크플로우 설정**

   ```
   Workflow name: Human-in-loop-Workflow
   Description: 사용자 승인을 포함한 여행 계획 워크플로우
   
   Steps:
   1. TravelPlannerAgent (초안 생성)
   2. Human Approval (사용자 검토)
   3. LocalAgent (승인 시 현지 정보 추가)
   4. TravelSummaryAgent (최종 요약)
   ```

4. **Approval 설정**

   ```
   Approval message: "생성된 여행 계획을 검토해주세요. 승인하시겠습니까?"
   
   Options:
   - Approve: 다음 단계로 진행
   - Reject: TravelPlannerAgent로 돌아가기
   - Modify: 수정 요청 입력 받기
   
   Timeout: 24시간 (응답 없으면 자동 거부)
   ```

### 테스트 시나리오

1. **승인 시나리오**

   ```
   사용자: 안녕
   TravelPlannerAgent: 여행 일정 초안 생성
   [System]: 사용자 승인 대기...
   사용자: 승인
   LocalAgent: 현지 정보 추가
   TravelSummaryAgent: 최종 요약
   ```

2. **거부 및 재생성 시나리오**

   ```
   사용자: 제주도 여행 계획 짜줘
   TravelPlannerAgent: 초안 생성 (호텔 중심)
   [System]: 사용자 승인 대기...
   사용자: 거부. 펜션으로 변경해줘
   TravelPlannerAgent: 수정된 계획 생성 (펜션 중심)
   [System]: 사용자 승인 대기...
   사용자: 승인
   LocalAgent: 현지 정보 추가
   TravelSummaryAgent: 최종 요약
   ```

   ![Human-in-Loop Workflow Preview](../assets/05-10-human-in-loop-workflow-preview.png)

### 💡 Human-in-loop 모범 사례

```
✅ 권장사항:
- 승인 지점을 명확히 표시
- 타임아웃 설정으로 무한 대기 방지
- 사용자에게 컨텍스트 제공 (이전 대화 요약)
- 간단한 승인 옵션 제공 (예/아니오/수정)

❌ 피해야 할 것:
- 너무 많은 승인 지점
- 불명확한 승인 질문
- 긴 타임아웃 (사용자 경험 저하)
- 승인 후 되돌리기 불가능한 구조
```

### ✅ 확인 사항

- 승인 지점에서 워크플로우가 올바르게 멈추는지 확인
- 승인/거부에 따라 적절히 분기되는지 확인
- 타임아웃이 정상 작동하는지 확인

---

## 📚 추가 리소스

- [Microsoft Foundry Workflows 개요](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/concepts/workflow?view=foundry)
- [Microsoft Agent Framework Workflows Orchestrations 패턴](https://learn.microsoft.com/en-us/agent-framework/user-guide/workflows/orchestrations/overview)

## 다음 단계

복잡한 워크플로우를 구축했습니다! 이제 에이전트와 워크플로우의 성능을 평가하는 방법을 학습합니다:

➡️ **[06. 평가](./06-evaluations.md)**: 에이전트 및 워크플로우의 품질을 체계적으로 평가합니다.

---

[← 이전: Foundry IQ](./04-foundry-iq.md) | [메인으로](./README.md) | [다음: 평가 →](./06-evaluations.md)
