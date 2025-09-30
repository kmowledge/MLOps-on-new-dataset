### ML Ops Maturity Assessment

Based on the current state of repository.

#### 1. Documentation

##### 1.1. Project Documentation

- [ ] Business goals and KPIs of an ML project are documented and kept up to date.
- [ ] Overview of all team members involved in a machine learning project including their responsibilities are created and kept up to date.
- [ ] ML model risk evaluation is created, documented, and kept up to date.

##### 1.2. ML model documentation

- [x] Steps of gathering, analyzing and cleaning data including motivation for each step should be documented. (partly reported)
- [x] Data definition (what features are used in an ML model and what these features mean) is documented.
- [ ] Choice of machine learning model is documented and justified.

##### 1.3. Technical documentation

- [ ] For real time inference use cases, API is documented: request & response structure and definition, data types.
- [x] Software architecture design is documented and kept up to date.

#### 2. Traceability and reproducibility

##### 2.1. Infrastructure traceability and reproducibility

- [x] Infrastructure is defined as code, later referenced as IaC. (partly)
- [x] IaC is stored in a version control system.
- [x] Pull request process is used to create changes in IaC.
- [x] When pull request is merged, changes will be automatically applied to corresponding environments through a CD pipeline.
- [x] Only CD pipelines can deploy changes, individual developers do not have rights to deploy infrastructure.
- [x] ML projects should have at least two environments (preproduction and production) which are exact copies of each other.
- [x] All environments related to a ML project should have (read and/or write) access to production data (data should be the same at any moment of time).

##### 2.2. ML code traceability and reproducibility

- [x] Code for gathering, analyzing, and cleaning data should be stored in a version control system.
- [x] ML model code is stored in the version control system, together with data preparation code and API code (if applicable).
- [x] Pull requests (PR) are used to make changes in any code related to an ML project.
- [x] When PR is merged, changes will be automatically applied to corresponding environments through a CD pipeline.
- [x] Environment is defined as code and is reproducible. (partly)
- [x] ML model code should not require changes to run in different environments. The processes of deployment of an ML model to all environments should be the same.
- [x] For any given machine learning model run/deployment in any environment it is possible to look up unambiguously: 1. corresponding code/ commit on git, 2. infrastructure used for training and serving, 3. environment used for training and serving, 4. ML model artifacts, 5. what data was used to train the model.
- [ ] ML model retraining strategy is present and motivated.
- [ ] Roll-back strategy is present to be able to revert to the previous ML model version.

#### 3. Code Quality

##### 3.1. Infrastructure code quality requirements

- [x] CI pipeline that includes configuration files validation and running automated tests is triggered at pull request creation.
- [x] Other team members (e.g., developers / security specialists) must review and approve changes before merging a pull request.

##### 3.2. ML model code quality requirements

- [ ] Pre-commit hooks are implemented to ensure that code follows the code quality guidelines before it is pushed to a version control system.
- [ ] ML model code contains tests for all steps in an ML process (data processing, ML model training, API deployment).
- [ ] CI pipeline that includes running automated tests is triggered at pull request creation.
- [s] Other team members (for example, developers/ security specialists) must approve changes before merging a pull request.
- [ ] For real time inference use cases, strategy should be present to perform API load and stress tests regularly and make sure API meets latency requirements.
- [ ] For real time inference use cases, authentication and networking should follow security guidelines.
- [ ] ML model code should be documented (documentation as code).
- [ ] Release notes should be created every time there is a new release of an ML model code.

#### 4. Monitoring & Support

##### 4.1. Infrastructure monitoring requirements

- [ ] Tracking of infrastructure costs is set up; cost estimation is done regularly for an ML project.
- [ ] Health of infrastructure resources is monitored. Alerting is set up in case problems occur.

##### 4.2. Application monitoring requirements

- [ ] For real time inference use cases, all API requests and responses should be logged, API response time, response codes, and health status should be monitored.
- [ ] For batch use cases, continuity of delivery to the target system should be monitored.

##### 4.3. KPI & model performance monitoring requirements

- [x] Offline evaluation metrics (for example, F1 score computed on historical data for classification tasks) is stored and monitored.
- [ ] Feedback loop is used to evaluate and constantly monitor KPIs that were defined together with the business stakeholders for this ML project.

##### 4.4. Data drift & Outliers monitoring

- [ ] Distributions of important model features are recalculated on a regular basis, alerts are created if a significant change in distribution that affects the target is detected.
- [ ] Outlier detection is set up, cases when machine learning models are returning predictions with low certainty are regularly reviewed.
