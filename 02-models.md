# 02. 모델 및 배포

이 모듈에서는 Microsoft Foundry에서 제공하는 다양한 LLM 모델을 탐색하고 배포하는 방법을 학습합니다.

## 📋 목차

- [모델 탐색 (Discover)](#모델-탐색-discover)
- [모델 비교 및 배포](#모델-비교-및-배포)
- [Embedding 모델 배포](#embedding-모델-배포)
- [Model Router 배포](#model-router-배포)
- [Model Router 구성](#model-router-구성)
- [다음 단계](#다음-단계)

## 🎯 학습 목표

- 모델 리더보드를 통한 모델 성능 비교
- 다양한 AI 모델 배포 방법 이해
- Model Router 설정 및 구성
- 모델 라우팅 전략 이해

## ⏱️ 예상 소요 시간

약 15분

---

## 모델 탐색 (Discover)

Foundry 포털의 Discover 섹션에서 다양한 AI 모델을 탐색할 수 있습니다.

### 단계별 가이드

1. **Discover 섹션 이동**
   - Foundry 포털 우측 상단 메뉴에서 **Discover**를 클릭합니다.

   ![Discover > Models 메뉴](./assets/02-00-discover-overview.png)

   - **Models** 메뉴를 선택합니다.
   
   ![Discover > Models 메뉴](./assets/02-01-discover-models.png)

2. **모델 리더보드 확인**
   - **View leaderboard** 옵션을 클릭합니다.
   - 다양한 모델의 성능 지표를 확인할 수 있습니다:
     - Quality scores
     - Latency
     - Cost
     - Context window
     - Modality support (text, vision, audio)
   
   ![Model Leaderboard 화면](./assets/02-02-model-leaderboard.png)

3. **모델 카테고리 이해**
   - **Language Models**: GPT-5.1, GPT-5, Claude 등
   - **Embedding Models**: text-embedding-3-large, text-embedding-ada-002 등

### 💡 팁

- 리더보드는 정기적으로 업데이트되므로 최신 모델을 확인하세요
- 각 모델의 상세 페이지에서 capabilities와 limitations을 확인하세요

---

## 모델 비교 및 배포

### GPT-5.1 모델 배포

1. **모델 비교 기능 사용**
   - Models 페이지에서 **Compare models** 버튼을 클릭합니다.
   - 비교하고 싶은 모델들을 선택합니다 (예: GPT-5.1, GPT-5, Claude 4.5 Sonnet).
   - 성능, 비용, 기능을 비교합니다.
   
   ![Compare models 기능](./assets/02-03-model-compare.png)

2. **GPT-5.1 선택 및 배포**
   - 모델 목록에서 **gpt-5.1** 을 찾습니다.
   - 모델 카드를 클릭하여 상세 정보를 확인합니다.
   
   ![GPT-5.1 모델 카드](./assets/02-04-gpt51-model-card.png)

3. **배포 설정**
   - **Deploy** 버튼을 클릭합니다.
   
   ![Deploy 버튼](./assets/02-05-gpt51-deploy-button.png)

4. **배포 완료**
   - **Default settings**를 클릭하여 배포를 시작합니다.
   - 배포 완료까지 1-2분 정도 소요됩니다.

### ✅ 확인 사항

- Build > Models 섹션에서 배포된 `gpt-5.1` 모델 확인
- 배포 상태가 "Succeeded"인지 확인
- Endpoint URL이 생성되었는지 확인

![Build > Models에서 배포된 gpt-5.1 확인](./assets/02-07-gpt51-deployed.png)

---

## Embedding 모델 배포

Embedding 모델은 텍스트를 벡터로 변환하여 의미적 검색 및 유사도 계산에 사용됩니다.

### 단계별 가이드

1. **Embedding 모델 검색**
   - Discover > Models 페이지에서 검색창에 **"text-embedding"**을 입력합니다.
   - 필터를 사용하여 Embedding 모델만 표시할 수 있습니다.
   
   ![text-embedding 검색](./assets/02-08-embedding-search.png)

2. **text-embedding-3-large 선택**
   - **text-embedding-3-large** 모델을 선택합니다.
   - 모델 상세 정보 확인:
     - Dimensions: 3072
   
   ![text-embedding-3-large 모델 카드](./assets/02-09-embedding-model-card.png)

3. **배포 설정**
   ```
   Deployment name: text-embedding-3-large
   Model version: [최신 버전]
   Deployment type: Standard
   ```

4. **배포 실행**
   - **Deploy** 버튼을 클릭하여 배포합니다.
   
   ![배포 완료 확인](./assets/02-10-embedding-deployed.png)

---

## Model Router 배포

Model Router는 여러 모델 간의 지능형 라우팅을 제공하여 비용, 품질, 성능을 최적화합니다.

### 단계별 가이드

1. **Model Router 검색**
   - Discover > Models에서 **"model-router"**를 검색합니다.
   
   ![model-router 검색](./assets/02-11-model-router-search.png)

2. **Model Router 정보 확인**
   - Model Router의 주요 기능:
     - 자동 모델 선택
     - 로드 밸런싱
     - 비용 최적화
     - 품질 기반 라우팅

3. **배포 설정**
   ```
   Deployment name: model-router
   Routing strategy: Balanced (기본값)
   Included models: [사용 가능한 모델 자동 감지]
   ```
   
   ![Model Router 배포 설정](./assets/02-12-model-router-deploy.png)

4. **배포 완료**
   - **Deploy** 버튼을 클릭합니다.
   - Model Router가 사용할 수 있는 배포된 모델들을 자동으로 감지합니다.

### ✅ 확인 사항

- Build > Models에서 `model-router` 배포 확인
- 배포 상태 확인
- Router가 접근 가능한 모델 목록 확인

![Build > Models 전체 배포 목록](./assets/02-15-models-overview.png)

---

## Model Router 구성

Model Router의 라우팅 전략을 설정하여 애플리케이션 요구사항에 맞게 최적화합니다.

### 단계별 가이드

1. **Model Router 상세 페이지 이동**
   - Build > Models 섹션으로 이동합니다.
   - 배포된 **model-router**를 클릭합니다.

2. **Edit 모드 진입**
   - **Details** 탭을 선택합니다.
   - **Edit** 버튼을 클릭합니다.
   
   ![Model Router 설정 화면 (Edit 모드)](./assets/02-13-model-router-config.png)

3. **Model Router Configuration 설정**
   
   #### Routing Mode 옵션:
   
   ![Routing Mode 옵션](./assets/02-14-model-router-modes.png)
   
   **a) Balanced Mode (균형 모드)**
   ```
   Description: 비용, 품질, 성능의 균형을 유지
   Use case: 일반적인 프로덕션 워크로드
   Behavior: 요청에 따라 적절한 모델 자동 선택
   ```

   **b) Quality Mode (품질 모드)**
   ```
   Description: 최고 품질의 응답 우선
   Use case: 정확도가 중요한 애플리케이션
   Behavior: 가장 성능이 좋은 모델 우선 사용
   Cost: 상대적으로 높은 비용
   ```

   **c) Cost Mode (비용 모드)**
   ```
   Description: 비용 최적화 우선
   Use case: 대량의 간단한 요청 처리
   Behavior: 비용 효율적인 모델 우선 사용
   Quality: 기본 품질 유지
   ```

4. **라우팅 모드 선택**
   - 워크샵에서는 **Balanced** 모드를 선택합니다.
   - 필요에 따라 다른 모드로 변경 가능합니다.

5. **저장 및 적용**
   - **Save** 버튼을 클릭하여 설정을 저장합니다.
   - 변경사항이 즉시 적용됩니다.

### 📊 Model Router 동작 예시

```
사용자 요청 → Model Router → 판단:
  - 간단한 질문 → GPT-5-nano (저비용)
  - 복잡한 분석 → GPT-5-mini (고품질)
  - 코드 생성 → Codex 계열
  - 높은 부하 → 부하 분산
```

### 💡 최적화 팁

- **개발 환경**: Cost Mode로 비용 절감
- **프로덕션**: Balanced Mode로 안정성 확보
- **고객 대면 서비스**: Quality Mode로 사용자 경험 개선
- **A/B 테스팅**: 모드별 성능 비교 분석

---

## 📚 추가 리소스

- [Model Catalog 가이드](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?view=foundry&tabs=global-standard-aoai%2Cstandard-chat-completions%2Cglobal-standard&pivots=azure-openai)
- [Model Router 개요](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/model-router?view=foundry)
- [Embedding Models 가이드](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/embeddings?view=foundry&tabs=python-new)

---

## 다음 단계

모델 배포가 완료되었습니다! 이제 이 모델들을 활용하여 에이전트를 구축해봅시다:

➡️ **[03. 에이전트 개발](./03-agents.md)**: 다양한 기능을 가진 AI 에이전트를 만들어봅니다.

---

[← 이전: 환경 설정](./01-setup.md) | [메인으로](./README.md) | [다음: 에이전트 개발 →](./03-agents.md)
