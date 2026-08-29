# AI-Assisted Early Disease Prediction Platform: A Literature Survey

**Prepared for:** the proposed AI-assisted early disease prediction platform
**Scope:** machine learning, healthcare analytics, and clinical deployment
**Date:** August 2026

## Abstract

This survey reviews twelve published studies on machine learning for early disease detection and prediction, and extracts what they say about building a platform that improves efficiency, decision-making, monitoring, automation, and user outcomes. The papers cover diabetes, cardiovascular disease, acute kidney injury, sepsis, infectious disease surveillance, and general electronic health record analysis. Taken together, they show three things: machine learning models can outperform traditional risk scores, early warning with enough lead time to act is achievable at hospital scale, and explainability is a practical requirement rather than a bonus. They also show a stubborn problem. Most published models are never validated outside the dataset they were trained on, and very few survive contact with busy clinical settings. The final sections of the survey turn these findings into a set of design decisions and a requirements checklist for the platform.

## 1. Purpose and Scope

The platform we are designing aims to predict disease early using machine learning and healthcare analytics. It has four stated goals: improve efficiency, support decision-making, enable continuous monitoring, and automate work in a way that improves user outcomes. "Early" carries two meanings in this literature. The first is catching a condition before it becomes severe, for example detecting acute kidney injury hours before it damages the kidney. The second is flagging risk months or years before a chronic disease appears, for example estimating type 2 diabetes risk from routine check-up records.

Three questions drive this survey:

1. Which models and data sources actually work for early prediction?
2. What does the evidence say about decisions, monitoring, and automation?
3. What commonly gets in the way of these systems working in real hospitals and clinics?

The survey ends with a mapping of findings to design decisions, because a literature survey that ends at "the literature shows promise" does not help anybody build anything.

## 2. How the Papers Were Chosen

Papers were found through searches of PubMed, IEEE Xplore, ScienceDirect, and publisher websites, covering work published between 2017 and 2025. Three kinds of papers were preferred: systematic reviews and meta-analyses (because they summarise broad evidence rather than one lucky result), landmark primary studies on large clinical datasets (because they show what is possible at scale), and papers about explainability and deployment (because those are where most systems fail in practice). Twelve papers were selected in total.

| # | Author (year) | Type | Domain | Contribution to this project |
|---|---|---|---|---|
| 1 | Kavakiotis et al. (2017) | Review | Diabetes | Baseline picture of ML in diabetes research; names data quality as the weak point |
| 2 | Lundberg and Lee (2017) | Methods paper | All domains | SHAP, the standard method for explaining model predictions |
| 3 | Shickel et al. (2018) | Survey | EHR deep learning | How deep learning is applied to records, and where evaluation falls short |
| 4 | Rajkomar et al. (2018) | Primary study | Hospital EHR | Deep learning on raw patient records at two hospitals; beats logistic regression |
| 5 | Ahamed and Farid (2018) | Review | IoT and wearables | Personalized monitoring; data volume, security, and interoperability problems |
| 6 | Komorowski et al. (2018) | Primary study | Sepsis, ICU | A model that recommends treatment, not just risk; outcomes improve when staff follow it |
| 7 | Tomašev et al. (2019) | Primary study | Acute kidney injury | Continuous hospital-wide early warning; 55.8% of episodes caught up to 48 hours early |
| 8 | Sendak et al. (2020) | Perspective | Deployment | "Model Facts" label: clinicians must know a model's limits, not just its score |
| 9 | Reddy et al. (2020) | Review | Diabetes | Comparison of classifiers for early-stage diabetes screening |
| 10 | Abdulazeem et al. (2023) | Systematic review | Primary care | 106 studies, 42 conditions, 207 models; 90.8% flagged high or unclear risk of bias |
| 11 | Liu et al. (2025) | Review and meta-analysis | Cardiovascular disease | Pooled AUC of ML models versus classic risk scores; bias concerns in model building |
| 12 | Qasrawi et al. (2025) | Systematic review | Infectious disease | Deep learning for pathogen detection and outbreak prediction; infrastructure gaps |

## 3. The Papers in Brief

**Kavakiotis et al. (2017)** reviewed machine learning and data mining work in diabetes research, covering prediction of onset, glucose management, and complication risk. Their conclusion is sobering: plenty of models, good reported accuracies, but most studies use small clinical datasets and rarely share their code or validate on outside data. They argue that the field needs larger, better-curated cohorts and that algorithm choice matters less than data quality.

**Lundberg and Lee (2017)** introduced SHAP, a method that assigns each feature a number describing how much it contributed to a particular prediction. The mathematical contribution is that SHAP is the only explanation method satisfying three defensible properties at once: local accuracy, missingness, and consistency. Practically, this paper is why most modern clinical machine learning papers show SHAP summary plots. It gives a platform a trustworthy, standards-compliant way to answer the question "why did the model say this?"

**Shickel et al. (2018)** surveyed deep learning applied to electronic health records. They mapped the field across representation learning, recurrent networks for time series, convolutional models, and multimodal combinations of structured and free-text data. Their criticism is important: many papers report good results on small or single-site data, interpretability is usually skipped, and fair comparison between architectures is rare. They argue that representation learning, meaning how records are turned into model inputs, is often more important than the model itself.

**Rajkomar et al. (2018)** built deep learning models on raw electronic health records from 216,221 adults across two academic medical centers. A data processing pipeline converted records into a standard format, and models predicted in-hospital mortality, 30-day unplanned readmission, prolonged length of stay, and discharge diagnoses. Performance beat logistic regression on all tasks, with AUCs ranging from about 0.76 for readmission to 0.94 for mortality. The study is a practical demonstration that models can learn from messy real-world records without hand-engineered features, though the authors note that evaluation was retrospective.

**Ahamed and Farid (2018)** reviewed the combination of Internet of Things devices and machine learning for personalized healthcare. They describe the promise, which is continuous personal data feeding personal models, and then the problems: enormous data volumes, weak security and privacy protections, poor interoperability between device vendors and health systems, and questionable accuracy of consumer sensors. Their warning is directly relevant to any platform planning wearable inputs: the data pipeline and its governance are the hard part, not the model.

**Komorowski et al. (2018)** trained a reinforcement learning agent on roughly 96,000 intensive care patients from the MIMIC-III database to learn optimal treatment strategies for sepsis, specifically fluid and vasopressor dosing. Unlike prediction models that output a risk score, this system outputs a recommended action. The striking result: in an independent validation cohort, mortality was lowest among patients whose clinicians' actual dosing matched what the AI would have recommended. The paper is the clearest evidence in this set that a decision-support system, not just a prediction engine, changes outcomes.

**Tomašev et al. (2019)** developed a deep learning system for continuous prediction of acute kidney injury across a large care network, using records from 703,782 adult patients across 172 inpatient and 1,062 outpatient sites. The model caught 55.8% of all inpatient acute kidney injury episodes and 90.2% of the episodes that later required dialysis, with up to 48 hours of lead time, at a cost of roughly two false alerts for every true alert. Every prediction came with a confidence estimate, the most salient clinical features, and predicted future trajectories for relevant blood tests. This is the best template in the literature for what a monitoring subsystem should look like.

**Sendak et al. (2020)** describe a sepsis prediction model that was already in use at Duke University and the problems they hit when putting it in front of clinicians. Front-line staff often did not know how the model should and should not be used. Their answer was the "Model Facts" label, a one-page summary designed like a nutrition label: what the model predicts, how it was trained, what data it saw, what it does not do, and what the developer's evidence actually supports. The paper argues that communicating model limitations is a safety requirement, not a formality.

**Reddy et al. (2020)** analysed machine learning techniques for early-stage diabetes prediction, comparing commonly used classifiers on a standard clinical dataset and discussing each algorithm's strengths and weaknesses for screening. Two of their points matter for our platform: boosted tree ensembles tend to win on tabular health records, and screening tools live or die on their false-negative rate, because telling a healthy person they are fine when they are not carries a real human cost.

**Abdulazeem et al. (2023)** ran a systematic review of machine learning diagnostic and prognostic models built on real-world primary care data. They found 106 studies covering 42 health conditions, with 207 prediction models built from data on 24.2 million participants in 19 countries. The review is a reality check: 92.4% of studies were retrospective, only 23.6% of models received any external validation, and 90.8% of studies carried a high or unclear risk of bias. Diabetes and Alzheimer's disease were the most studied conditions, and random forest and support vector machines together made up 42.5% of the models. Half of all studies came from the United States or the United Kingdom.

**Liu et al. (2025)** performed a systematic review and meta-analysis of machine learning models predicting cardiovascular disease risk from electronic health records, covering 22 studies. Pooled performance showed ML models reaching an AUC of 0.815, versus 0.765 for conventional risk scores, with ensemble methods performing best at 0.820. The caveat is equally clear: 34.5% of the models had a high risk of bias, mostly from poor handling of missing data, weak preprocessing, and overfitting. Machine learning beats the old scores, but only when built carefully.

**Qasrawi et al. (2025)** reviewed machine learning for infectious disease early detection and outbreak prediction in the Middle East and North Africa, covering studies published between 2016 and 2024. Convolutional neural networks dominated pathogen detection from medical imaging with a mean accuracy of 96.3%, while random forest models were the most successful for outbreak prediction. Transfer learning appeared in a third of studies, usually to cope with scarce data. Their list of barriers is a good summary of the region-wide problem: poor data quality, weak digital infrastructure, and algorithmic bias.

## 4. What the Literature Says, Theme by Theme

### 4.1 Models and Data

There is no single best algorithm, and the papers agree on a rough division of labour. For structured tabular records, boosted trees and ensembles are the consistent winners (Kavakiotis et al. 2017; Reddy et al. 2020; Liu et al. 2025). For imaging, convolutional networks dominate (Qasrawi et al. 2025). For longitudinal records and time series, recurrent architectures and sequence models show the strongest results (Shickel et al. 2018; Tomašev et al. 2019).

What matters more than the algorithm is how data is prepared. Rajkomar et al. (2018) spent most of their engineering effort on a pipeline that turned raw records into a standard representation, and Shickel et al. (2018) state plainly that representation learning often decides performance. Liu et al. (2025) found that the biggest source of bias in cardiovascular models was not the algorithm but preprocessing, missing-data handling, and overfitting. The practical lesson for our platform: invest in the data layer first, and treat the model as a component that can be swapped.

### 4.2 Early Detection Works, Within Limits

The headline numbers are genuinely encouraging. Acute kidney injury was caught in more than half of inpatient episodes, and in 90.2% of dialysis-requiring cases, with up to two days of lead time (Tomašev et al. 2019). Machine learning risk scores for cardiovascular disease outperformed established clinical scores by about 0.05 AUC on pooled analysis (Liu et al. 2025). Deep learning on raw records predicted hospital outcomes better than logistic regression on every task tested (Rajkomar et al. 2018). Imaging-based pathogen detection averaged above 96% accuracy (Qasrawi et al. 2025).

The limits are just as clear. Reported accuracy lives in retrospective datasets, and the most comprehensive review of primary care models found that more than nine in ten studies carried high or unclear risk of bias, with only a quarter externally validated (Abdulazeem et al. 2023). "Early" also only creates value if someone can act in the window created: the lead time is the product, not the model.

### 4.3 Decision Support, Not Just Prediction

Most machine learning papers stop at a probability. Komorowski et al. (2018) is the exception that proves the rule. Their reinforcement learning system recommends concrete treatment actions for sepsis, and patients did better when clinicians followed the recommendations. The paper's title, "the artificial intelligence clinician", is not a boast about replacing doctors. It is a claim that a system which suggests what to do, rather than merely how likely an outcome is, can change real outcomes.

The nearest equivalent in the prediction-only world is Tomašev et al. (2019), whose outputs were designed around action: confidence, salient features, and forecast trajectories for blood tests, so a clinician can see why the alert fired and what is expected to happen next. Sendak et al. (2020) add the missing rule: every model output must be accompanied by honest information about how, when, and when not to use it.

### 4.4 Monitoring and Automation

Continuous monitoring is the use case where the literature is strongest, thanks mostly to Tomašev et al. (2019). Their system did not run once per patient. It re-scored continuously across a whole care network, and alarm behaviour was tuned deliberately: two false alerts per true alert is not a failure, it is a design choice to keep clinicians from ignoring alarms. Alert fatigue is a real clinical hazard, and the papers that ignore it tend to be the ones that never reach deployment.

The wearable and IoT track is younger and messier. Ahamed and Farid (2018) describe a pipeline that sounds exactly like an ambitious platform architecture: sensors, gateways, cloud storage, models, and alerts to clinicians. They also list what breaks it. Data volumes overwhelm storage and transfer. Device vendors do not share formats. Consumer-grade sensors drift in accuracy. Security and privacy rules for continuous personal data are unsettled. Any plan to include wearable streams should copy the clinical monitoring pattern, not the consumer wellness pattern.

### 4.5 Explainability and Trust

Explainability is where the method papers and the deployment papers meet. Lundberg and Lee (2017) gave the field a principled attribution method, and it has since become the default way to show why a clinical model made a call (Shickel et al. 2018). The deployment literature is clear that explanations are not decoration: Sendak et al. (2020) found clinicians repeatedly misused a sepsis model because nobody had told them its limits.

Two patterns appear in the strongest systems. First, explanations are local and action-linked: what drove this patient's alert, in this patient's terms (Tomašev et al. 2019). Second, explanations are communicated to humans and tested with them. A SHAP bar chart on a dashboard satisfies no one if the doctor cannot tell whether an alert is worth acting on.

### 4.6 Bias, Fairness, and the Data Gap

Three bias warnings recur. The first is geographic: half the studies in the primary care review came from the United States or the United Kingdom (Abdulazeem et al. 2023), and the MENA review explicitly flags algorithmic bias alongside poor infrastructure (Qasrawi et al. 2025). Models trained on one population can quietly misread another. The second is structural: class imbalance and missing data skew results, and the bias assessment meta-analysis traced most high-risk ratings to exactly these steps (Liu et al. 2025). The third is informational: Sendak et al. (2020) emphasise that clinicians, patients, and even administrators are frequently unaware of what a model cannot do, which is itself a fairness and safety problem.

For a platform that will run on local patient data, the message is direct. Reporting metrics on one population is not enough. Subgroup performance, calibration in the local population, and retraining on local records should be built into the system from day one.

### 4.7 Why Good Models Fail at the Door

The papers converge on three recurring failure points. Validation is the first: 76.4% of primary care models were developed without any external validation (Abdulazeem et al. 2023). Reporting is the second: a third of cardiovascular models showed high risk of bias from method descriptions that were missing or inadequate (Liu et al. 2025). Communication is the third: models reached clinicians without any statement of their intended use, so clinicians guessed (Sendak et al. 2020). Add infrastructural limits in lower-resource regions (Qasrawi et al. 2025) and the picture is complete. Technical performance is rarely what stops these systems. The pipeline around the model is.

## 5. Gaps the Papers Leave Open

1. **Prospective evidence is missing.** 92.4% of primary care prediction studies were retrospective (Abdulazeem et al. 2023). Almost nothing tests whether early detection improves patient outcomes when run forward in time, which is the claim our platform most needs to make.
2. **External validation is rare.** Only 23.6% of models in the primary care review were validated outside their development data. Multi-site and multi-country validation should be a design requirement, not a later step.
3. **Reporting quality is weak.** Missing method details, unclear preprocessing, and absent handling of missing data are the norm in a third of cardiovascular models (Liu et al. 2025). Standardised reporting templates would help every project in this space.
4. **Explainability is rarely evaluated with humans.** SHAP and LIME papers usually show plots; they rarely measure whether clinicians understand or trust them. Sendak et al. (2020) is one of the few works to treat this as an engineering problem.
5. **Predictions are rarely linked to actions.** With the notable exception of Komorowski et al. (2018), almost no system recommends what to do after an alert. Outcome improvement requires the loop to close.
6. **Workflow and alert fatigue get little attention.** Tomašev et al. (2019) tuned their alert threshold deliberately. Most studies say nothing about how often their system would fire in a real ward.
7. **Cost and governance are under-studied.** None of the reviews finds strong evidence on cost-effectiveness, liability, or regulatory pathway, all of which decide whether a platform gets adopted.
8. **Data from outside high-income countries is thin.** The regional review shows high accuracy in imaging tasks but persistent data and infrastructure problems (Qasrawi et al. 2025). A platform targeted at local healthcare systems cannot rely on foreign benchmarks.
9. **Continuous monitoring lags one-off screening.** Disease-onset risk models far outnumber rolling hospital- or home-based monitoring systems, even though monitoring is where early warning creates the most time.

## 6. Mapping the Findings to Our Platform

| Literature finding | Design decision for the platform |
|---|---|
| Boosted trees win on tabular data; sequence models win on longitudinal data (Kavakiotis et al. 2017; Shickel et al. 2018; Liu et al. 2025) | Use a hybrid architecture: ensemble models for screening risk, sequence models for monitoring streams; keep the model layer swappable |
| Data preparation and representation decide more than algorithm choice (Rajkomar et al. 2018; Shickel et al. 2018) | Build and version the data pipeline first; automate cleaning, unit normalisation, and missing-data handling |
| External validation is missing in three quarters of studies (Abdulazeem et al. 2023) | Plan multi-cohort validation and a prospective pilot as part of the roadmap, not as a postscript |
| SHAP is the defensible standard for attribution (Lundberg and Lee 2017) | Ship record-level explanations by default on every prediction surface |
| Clinicians misuse models when limits are unclear (Sendak et al. 2020) | Generate a Model Facts style label for every model before it is exposed to users |
| Continuous re-scoring with tuned alerts works at scale (Tomašev et al. 2019) | Build monitoring as an always-on service with clinician-tuned thresholds and explicit false-alert budgeting |
| Predictions should lead to actions (Komorowski et al. 2018) | Attach a recommended next step to every alert: re-test, escalate, refer, or watch |
| Alert fatigue breaks adoption (Tomašev et al. 2019) | Track override and acknowledgement rates as core metrics; suppress redundant alerts |
| Bias risk concentrates in preprocessing and imbalance (Liu et al. 2025) | Audit preprocessing steps, handle class imbalance explicitly, and report subgroup metrics |
| Models trained abroad may not transfer (Abdulazeem et al. 2023; Qasrawi et al. 2025) | Calibrate and retrain on local data; monitor drift continuously |
| Wearable data brings volume, security, and accuracy problems (Ahamed and Farid 2018) | Limit sensor inputs to clinically justified signals; design for disconnection; secure data by default |

## 7. Requirements the Survey Supports

**Efficiency**
- A data pipeline that automates cleaning and standardisation of records before modelling, since preprocessing is the top source of bias (Liu et al. 2025).
- Risk scoring that runs in batch for whole patient populations, not just one record at a time (Rajkomar et al. 2018).
- Reusable model registry with versioning and automatic evaluation reports.

**Decision-making**
- Every prediction displayed with local feature attributions (Lundberg and Lee 2017).
- A stated next action for every alert, because recommendation, not risk, changes outcomes (Komorowski et al. 2018).
- A Model Facts style label for each deployed model: purpose, training data, performance, and limitations (Sendak et al. 2020).

**Monitoring**
- Continuous re-scoring of enrolled patients with lead-time visibility and confidence estimates (Tomašev et al. 2019).
- Thresholds tuned with clinicians and set to tolerate a bounded number of false alerts.
- Trajectory forecasts for key laboratory values where data supports them (Tomašev et al. 2019).

**Automation and outcomes**
- Alert routing and escalation workflows so predictions translate into actions.
- Measurement of downstream outcomes: time to intervention, admission rates, escalation rates, and override rates.
- External validation and prospective evaluation as acceptance criteria for any model, addressing the field's largest gap (Abdulazeem et al. 2023).

## 8. Closing Note

The literature sends a consistent message. Machine learning can find disease earlier than conventional methods, and systems that explain themselves and recommend actions can genuinely change what happens to patients. The risk is not that the models will underperform in principle. The risk is that the platform repeats the field's historical mistakes: retrospective-only evidence, no external validation, unexplained alerts, and predictions that nobody knows how to act on. The papers reviewed here give us both the pattern to follow and the pattern to avoid, and the design decisions in section 6 are the bridge between what the evidence shows and what the platform should do.

## References

Abdulazeem, Hazem, Sean Whitelaw, Gunter Schauberger, and Stefanie J. Klug. 2023. "A Systematic Review of Clinical Health Conditions Predicted by Machine Learning Diagnostic and Prognostic Models Trained or Validated Using Real-World Primary Health Care Data." *PLOS ONE* 18 (9): e0274276. https://doi.org/10.1371/journal.pone.0274276.

Ahamed, Faizal, and Farnaz Farid. 2018. "Applying Internet of Things and Machine-Learning for Personalized Healthcare: Issues and Challenges." In *2018 International Conference on Machine Learning and Data Engineering (iCMLDE)*, 19-28. Sydney: IEEE. https://doi.org/10.1109/iCMLDE.2018.00010.

Kavakiotis, Ioannis, Olga Tsave, Athanasios Salifoglou, Nicos Maglaveras, Ioannis Vlahavas, and Ioanna Chouvarda. 2017. "Machine Learning and Data Mining Methods in Diabetes Research." *Computational and Structural Biotechnology Journal* 15:104-116. https://doi.org/10.1016/j.csbj.2016.12.005.

Komorowski, Matthieu, Leo Anthony Celi, Omar Badawi, Anthony C. Gordon, and Aldo A. Faisal. 2018. "The Artificial Intelligence Clinician Learns Optimal Treatment Strategies for Sepsis in Intensive Care." *Nature Medicine* 24 (11): 1716-1720. https://doi.org/10.1038/s41591-018-0213-5.

Liu, Tianyi, Andrew J. Krentz, Lei Lu, and Vasa Curcin. 2025. "Machine Learning Based Prediction Models for Cardiovascular Disease Risk Using Electronic Health Records Data: Systematic Review and Meta-Analysis." *European Heart Journal: Digital Health* 6 (1): 7-22. https://doi.org/10.1093/ehjdh/ztae080.

Lundberg, Scott M., and Su-In Lee. 2017. "A Unified Approach to Interpreting Model Predictions." In *Advances in Neural Information Processing Systems 30*, edited by Isabelle Guyon, Ulrike von Luxburg, Samy Bengio, Hanna Wallach, Rob Fergus, S. V. N. Vishwanathan, and Roman Garnett, 4765-4774. Long Beach, CA: Curran Associates.

Qasrawi, Radwan, et al. 2025. "The Role of Machine Learning in Infectious Disease Early Detection and Prediction in the MENA Region: A Systematic Review." *Informatics in Medicine Unlocked* 56:101651. https://doi.org/10.1016/j.imu.2025.101651.

Rajkomar, Alvin, et al. 2018. "Scalable and Accurate Deep Learning with Electronic Health Records." *npj Digital Medicine* 1:18. https://doi.org/10.1038/s41746-018-0029-1.

Reddy, Shiva Shankar, Neha Sethi, and Rituraj Rajender. 2020. "A Comprehensive Analysis of Machine Learning Techniques for Incessant Prediction of Diabetes Mellitus." *International Journal of Grid and Distributed Computing* 13 (1): 1-22. https://doi.org/10.33832/ijgdc.2020.13.1.01.

Sendak, Mark P., Michael Gao, Nathan Brajer, and Suresh Balu. 2020. "Presenting Machine Learning Model Information to Clinical End Users with Model Facts Labels." *npj Digital Medicine* 3:41. https://doi.org/10.1038/s41746-020-0253-3.

Shickel, Benjamin, Patrick James Tighe, Azra Bihorac, and Parisa Rashidi. 2018. "Deep EHR: A Survey of Recent Advances in Deep Learning Techniques for Electronic Health Record (EHR) Analysis." *IEEE Journal of Biomedical and Health Informatics* 22 (5): 1589-1604. https://doi.org/10.1109/JBHI.2017.2767063.

Tomašev, Nenad, et al. 2019. "A Clinically Applicable Approach to Continuous Prediction of Future Acute Kidney Injury." *Nature* 572 (7767): 116-119. https://doi.org/10.1038/s41586-019-1390-1.
