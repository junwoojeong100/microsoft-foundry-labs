# 06. 평가 (Evaluations)

이 모듈에서는 AI 에이전트와 워크플로우의 성능을 체계적으로 평가하는 방법을 학습합니다.

## 📋 목차

- [평가 개요](#평가-개요)
- [평가 생성](#평가-생성)
- [평가 기준 이해](#평가-기준-이해)
- [평가 실행 및 결과 분석](#평가-실행-및-결과-분석)
- [평가 모범 사례](#평가-모범-사례)
- [다음 단계](#다음-단계)

## 🎯 학습 목표

- AI 에이전트 평가의 중요성 이해
- Foundry의 자동 평가 기능 활용
- 다양한 평가 지표의 의미와 활용법 학습
- 합성 데이터를 사용한 평가 수행
- 평가 결과 해석 및 개선 방안 도출

## ⏱️ 예상 소요 시간

약 10분

---

## 평가 개요

### 왜 평가가 중요한가?

AI 에이전트를 프로덕션에 배포하기 전에 다음 사항을 검증해야 합니다:

```
정확성 → 관련성 → 일관성 → 자연스러움 → 안전성
```

평가 없이 배포하면:
- ❌ 부정확한 답변으로 사용자 신뢰 저하
- ❌ 관련 없는 응답으로 사용자 경험 악화
- ❌ 일관성 없는 품질로 브랜드 이미지 손상
- ❌ 부적절한 콘텐츠 생성으로 법적 문제

### 평가 유형

| 평가 유형 | 설명 | 사용 시기 |
|---------|------|---------|
| **Offline Evaluation** | 배포 전 테스트 데이터로 평가 | 개발 단계 |
| **A/B Testing** | 두 버전 비교 | 프로덕션 배포 시 |
| **Online Monitoring** | 실시간 성능 모니터링 | 운영 중 |
| **Human Evaluation** | 사람이 직접 평가 | 품질 검증 |

### Microsoft Foundry의 평가 기능

Foundry는 다음을 자동화합니다:
- ✅ 테스트 데이터 생성 (Synthetic generation)
- ✅ 다양한 평가 지표 적용
- ✅ 대규모 평가 실행
- ✅ 결과 시각화 및 분석

---

## 평가 생성

이전에 만든 `ModelRouterAgent`를 평가해봅니다.

### 단계별 가이드

1. **Evaluations 섹션 이동**

   - Foundry 포털 우측 상단 메뉴에서 **Build**를 선택합니다.
   - **Evaluations** 메뉴를 클릭합니다.
   
   ![Build > Evaluations 메뉴](../assets/06-01-evaluations-menu.png)

2. **Evaluation Catalog**

   ![Evaluations Catalog](../assets/06-01-evaluations-catalog.png)

3. **새 평가 생성**

   - **+ Create new evaluation** 또는 **New evaluation** 버튼을 클릭합니다.
   
   ![Create new evaluation 버튼](../assets/06-02-create-evaluation.png)

4. **Target 선택**

   평가 대상을 선택합니다:
   
   ![Target 선택 (Agent)](../assets/06-03-evaluation-target.png)

   ```
   Target type: Agent
   Agent: ModelRouterAgent
   Version: Latest (또는 특정 버전)
   ```

   **다른 Target 옵션**:
   - **Agent**: 단일 에이전트 평가
   - **Workflow**: 워크플로우 평가
   - **Model**: 모델 직접 평가
   - **Endpoint**: 외부 API 엔드포인트 평가

5. **Data 설정**

   테스트 데이터를 선택합니다:
   
   ![Data 설정 (Synthetic generation)](../assets/06-04-evaluation-data1.png)

   ![Data 설정 (Synthetic generation)](../assets/06-04-evaluation-data2.png)

   ![Data 설정 (Synthetic generation)](../assets/06-04-evaluation-data3.png)

   ```
   Data source: Synthetic generation
   
   Topic: 일반 대화 및 정보 제공
   
   Number of samples: 50
   (더 많은 샘플은 더 신뢰할 수 있지만 시간이 더 걸림)
   
   Languages: Korean, English
   ```

   **Synthetic Generation이란?**
   - AI가 자동으로 다양한 테스트 질문 생성
   - 실제 사용 패턴을 시뮬레이션
   - 수동으로 테스트 케이스를 작성할 필요 없음

   **다른 Data 옵션**:
   - **Upload dataset**: CSV/JSON 파일 업로드
   - **Use existing dataset**: 이전에 저장한 데이터셋 사용

6. **Criteria 선택**

   평가 기준을 선택합니다:

   ```
   ☑ Groundedness (답변이 사실에 기반하는지)
   ☑ Relevance (질문과 답변의 관련성)
   ☑ Coherence (답변의 일관성)
   ☑ Fluency (답변의 자연스러움)
   ```

   ![Metrics 선택 (Groundedness, Relevance 등)](../assets/06-05-evaluation-metrics.png)

   각 기준에 대한 상세 설명은 아래 섹션을 참조하세요.

7. **Review**

   설정을 검토합니다:
   
   ![Review and create](../assets/06-06-evaluation-review.png)

   ```
   Target: ModelRouterAgent (Latest)
   Data: Synthetic (50 samples, Korean/English)
   Criteria: Groundedness, Relevance, Coherence, Fluency
   Estimated time: ~10-15 minutes
   Estimated cost: $2-5 (샘플 수에 따라 다름)
   ```

8. **Submit**

   - 모든 설정을 확인한 후 **Submit** 버튼을 클릭합니다.
   - 평가가 백그라운드에서 실행됩니다.
   - 진행 상황은 Evaluations 페이지에서 확인할 수 있습니다.

   ![Evaluation Run](../assets/06-06-evaluation-run.png)

9. **Evaluation Result**

   ![Evaluation Result](../assets/06-06-evaluation-result.png)

   ![Evaluation Result](../assets/06-06-evaluation-result2.png)

   ![Evaluation Result](../assets/06-06-evaluation-result3.png)

   ![Evaluation Result](../assets/06-06-evaluation-result4.png)

   ![Evaluation Result](../assets/06-06-evaluation-result5.png)

   ![Evaluation Result](../assets/06-06-evaluation-result6.png)

### ✅ 확인 사항

- 평가가 "Running" 상태인지 확인
- 예상 완료 시간 확인
- 필요하면 다른 에이전트나 워크플로우 평가도 생성

---

## 평가 기준 이해

### Foundry 제공 Evaluator 전체 목록

Foundry는 6개 카테고리, 32개의 Evaluator를 제공합니다.

#### 🎯 일반 품질 (General Purpose)

| Evaluator | 설명 |
|-----------|------|
| **CoherenceEvaluator** | 응답의 논리적 일관성과 흐름 측정 |
| **FluencyEvaluator** | 자연어 품질과 가독성 측정 |
| **QAEvaluator** | Q&A 종합 평가 *(복합: Groundedness, Relevance, Coherence, Fluency, Similarity, F1Score)* |

#### 📊 텍스트 유사도 (Textual Similarity)

| Evaluator | 설명 |
|-----------|------|
| **SimilarityEvaluator** | 응답과 정답 간 의미적 유사도 |
| **F1ScoreEvaluator** | 정밀도와 재현율의 조화평균 |
| **BleuScoreEvaluator** | 기계 번역 품질 (n-gram 기반) |
| **GleuScoreEvaluator** | 문장 수준 BLEU 변형 |
| **RougeScoreEvaluator** | 요약 품질 (n-gram 재현율) |
| **MeteorScoreEvaluator** | 유의어/어간 고려 번역 평가 |

#### 🔍 RAG (Retrieval-Augmented Generation)

| Evaluator | 설명 |
|-----------|------|
| **RetrievalEvaluator** | 정보 검색 효과성 |
| **DocumentRetrievalEvaluator** | 정답 대비 검색 정확도 |
| **GroundednessEvaluator** | 응답이 컨텍스트와 일치하는지 (1-5점) |
| **GroundednessProEvaluator** | 고급 근거성 평가 (Azure AI Content Safety 기반) |
| **RelevanceEvaluator** | 응답과 질문의 관련성 (1-5점) |
| **ResponseCompletenessEvaluator** | 정답 대비 응답 완전성 |

#### 🤖 에이전트 (Agentic)

| Evaluator | 설명 |
|-----------|------|
| **IntentResolutionEvaluator** | 사용자 의도 파악 정확도 |
| **TaskAdherenceEvaluator** | 식별된 작업 수행 정도 |
| **ToolCallAccuracyEvaluator** | 올바른 도구 선택 및 호출 |

#### 🛡️ 위험 및 안전 (Risk and Safety)

| Evaluator | 설명 |
|-----------|------|
| **ViolenceEvaluator** | 폭력적 콘텐츠 탐지 |
| **SexualEvaluator** | 성적 콘텐츠 탐지 |
| **SelfHarmEvaluator** | 자해 관련 콘텐츠 탐지 |
| **HateUnfairnessEvaluator** | 혐오/차별 콘텐츠 탐지 |
| **IndirectAttackEvaluator** | 간접적 공격(탈옥 시도 등) 탐지 |
| **ProtectedMaterialEvaluator** | 저작권 보호 자료 탐지 |
| **UngroundedAttributesEvaluator** | 근거 없는 주장 탐지 |
| **CodeVulnerabilityEvaluator** | 코드 보안 취약점 탐지 |
| **ContentSafetyEvaluator** | 안전 종합 평가 *(복합: Violence, Sexual, SelfHarm, HateUnfairness)* |

#### 🔧 Azure OpenAI Graders

| Evaluator | 설명 |
|-----------|------|
| **AzureOpenAILabelGrader** | 레이블 기반 채점 |
| **AzureOpenAIStringCheckGrader** | 문자열 검증 채점 |
| **AzureOpenAITextSimilarityGrader** | 텍스트 유사도 채점 |
| **AzureOpenAIGrader** | 범용 Azure OpenAI 채점 |

---

### 핵심 평가 기준 4가지

이 워크샵에서는 가장 많이 사용되는 4가지 평가 기준을 사용합니다.

| 기준 | 정의 | 점수 기준 |
|------|------|----------|
| **Groundedness** (근거성) | 답변이 사실/컨텍스트에 기반하는지 | 1=환각, 5=사실 기반 |
| **Relevance** (관련성) | 답변이 질문과 관련 있는지 | 1=무관, 5=완벽 관련 |
| **Coherence** (일관성) | 답변이 논리적으로 구조화됐는지 | 1=혼란, 5=완벽 구조 |
| **Fluency** (유창성) | 답변이 문법적으로 자연스러운지 | 1=어색, 5=완벽 자연 |

**각 기준이 중요한 이유**:

| Groundedness | Relevance | Coherence | Fluency |
|--------------|-----------|-----------|---------|
| 사용자 신뢰 확보 | 사용자 만족도 향상 | 이해하기 쉬운 답변 | 사용자 경험 향상 |
| 법적 책임 최소화 | 효율적 정보 전달 | 전문적 이미지 | 브랜드 이미지 유지 |
| 허위 정보 방지 | 대화 흐름 유지 | 신뢰성 향상 | 이해도 증가 |

---

## 평가 모범 사례

| 항목 | 권장 사항 |
|------|----------|
| **샘플 수** | 개발: 10-20개 / 테스트: 50-100개 / 프로덕션: 200+개 |
| **테스트 시나리오** | 일반·복잡·모호·다국어 질문 + Edge cases |
| **평가 주기** | 개발 중: 매 업데이트 / 배포 전: 필수 / 배포 후: 주간/월간 |
| **기준선 점수** | Groundedness ≥4.0 / 나머지 ≥3.5 / Pass rate ≥80% |
| **Human Evaluation** | 자동 평가와 병행하여 새로운 문제 패턴 발견 |

---

## 📚 추가 리소스

- [Azure AI Evaluation 개요](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/observability?view=foundry#what-are-evaluators)
- [파운드리 포털에서 평가 실행](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/evaluate-generative-ai-app?view=foundry)
- [에이전트 평가](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-evaluators/agent-evaluators?view=foundry)

---

## 다음 단계

에이전트와 워크플로우의 품질을 평가하는 방법을 배웠습니다! 이제 프로덕션 환경에서 리소스를 관리하고 모니터링하는 방법을 학습합니다:

➡️ **[07. Control Plane](./07-control-plane.md)**: Fleet 관리, 모니터링, 컴플라이언스 등을 학습합니다.

---

[← 이전: 워크플로우](./05-workflows.md) | [메인으로](./README.md) | [다음: Control Plane →](./07-control-plane.md)
