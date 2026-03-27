
# Dmitry Zhuravlev — Cloud DevOps & Platform Engineering Portfolio

Production-grade cloud platforms, reliability-focused systems, and infrastructure solutions built around operational challenges.

**Focus Areas:** DevSecOps • Platform Engineering • SRE • Cloud Architecture • Kubernetes • CI/CD •  FinOps • Infrastructure as Code • Observability • Automation

---

## Featured Platform Projects

## 1. FinOps & Cloud Cost Optimization

### [Cloud Optimization Engine](https://github.com/DimitryZH/cloud-optimization-engine)

Open-source cost analysis engine for detecting unused cloud resources and modeling savings opportunities across cloud environments.

**Core Components:**
- Python — modular engine separating resource discovery and cost evaluation logic  
- Cloud Run — stateless execution layer for on-demand and scheduled analysis jobs  
- Cloud Scheduler — triggers periodic scans across projects for continuous cost monitoring  
- Terraform — modular infrastructure provisioning with bootstrap layer and demo resource generation for controlled cost analysis scenarios  
- Slack API — real-time alerting channel for detected waste patterns and cost findings  
- Cloud APIs — structured resource discovery across projects for consistent data collection  


**Core Capabilities:**
- Detects cloud waste patterns (unattached disks, idle IPs, stopped resources)  
- Models cost impact using resource-level analysis  
- Provides extensible framework for cost governance rules  
- Represents a foundation for more advanced organization-level cost analysis systems  

---

## 2. SRE & Reliability Engineering Platform

### [SLO-Driven Delivery Platform on GKE](https://github.com/DimitryZH/sre-platform)

GitOps-based platform implementing SLO- and error budget–driven release governance for Kubernetes workloads.

**Core Components:**
- Kubernetes (GKE) — multi-environment cluster setup with namespace isolation and autoscaling for workload segmentation  
- Argo CD — GitOps control plane implementing app-of-apps pattern and environment-based deployment promotion  
- Argo Rollouts — canary deployment strategy with analysis templates driven by Prometheus metrics  
- Prometheus — metrics collection and multi-window SLO evaluation  
- Grafana — visualization of SLOs, error budgets, and live rollout health signals  
- Helm — reusable and environment-specific configuration management for microservices deployment  
- Terraform — modular infrastructure provisioning for clusters, networking, and platform components  

**Core Capabilities:**
- Progressive delivery controlled by observability signals  
- SLO and error budget–driven deployment decisions  
- Automated promotion and rollback strategies  
- Platform-level control over service reliability and release safety  

---

## 3. Continuous Integration Build Platform

### [CI Build Platform](https://github.com/DimitryZH/ci-build-platform)

Scalable build platform based on ephemeral self-hosted runners for cloud CI workloads.

**Core Components:**
- GitHub Actions — orchestration of CI workflows and job scheduling  
- Compute Engine — ephemeral runners providing isolated execution environments  
- Cloud Run — control plane service managing runner lifecycle and scaling decisions  
- Terraform — dynamic provisioning and teardown of compute resources  
- Docker — standardized build environment and artifact packaging  
- Container Registry — storage and distribution of build artifacts  
- Cloud Logging & Monitoring — visibility into runner execution, failures, and system behavior  

**Core Capabilities:**
- On-demand provisioning of isolated CI runners  
- Scalable parallel build execution  
- Automated lifecycle management of build infrastructure  
- Platform-style abstraction over CI workloads  

---

## 4. Secure Delivery Platform

### [GCP Secure Delivery Platform](https://github.com/DimitryZH/gcp-secure-delivery-platform)

Secure cloud-native delivery platform focused on trusted builds, policy enforcement, and Kubernetes-native deployment controls.

**Core Components:**
- Cloud Build — reproducible and isolated build pipeline for trusted artifact creation  
- Artifact Registry — immutable artifact storage with controlled access  
- Binary Authorization — policy-based deployment validation ensuring only trusted images are deployed  
- Cloud Deploy — progressive delivery with controlled rollout strategies  
- Kubernetes (GKE) — controlled runtime environment with enforced deployment policies  
- Secret Manager — centralized secret storage with secure injection into workloads  
- Terraform — standardized infrastructure provisioning using reusable modules  
- Cloud Logging & Monitoring — audit trail and deployment visibility  

**Core Capabilities:**
- Controlled software delivery pipeline with integrated policy validation  
- Deployment verification and enforcement mechanisms  
- Trusted artifact lifecycle from build to runtime  
- Security integrated into the delivery workflow  

---

## 5. Enterprise Cloud Migration

### [Enterprise App Migration to Cloud](https://github.com/DimitryZH/app-migration)

Migration and modernization project focused on architecture, delivery automation, and cloud operating models.

**Core Components:**

**Compute & Runtime**
- Compute Engine + Managed Instance Groups — scalable and resilient application hosting layer  
- Cloud Run — containerized services for flexible workload execution  

**Networking**
- Custom VPC with private subnets — isolated network environment  
- No public IPs on instances — reduced attack surface  
- Cloud NAT — controlled outbound connectivity  
- HTTPS Load Balancer — secure entry point with TLS termination  

**Identity & Access**
- Dedicated service accounts — workload-level identity isolation  
- Granular IAM roles — least-privilege access to Firestore and Cloud Storage  

**Data & Storage**
- Firestore (Datastore mode) — managed NoSQL database  
- Cloud Storage — object storage for application data  

**Infrastructure & Delivery**
- Terraform — infrastructure as code with reproducible environments  
- GitHub Actions — automated build and deployment workflows  


**Core Capabilities**
- Migration from traditional infrastructure to cloud-native architecture  
- Private networking model with controlled access patterns  
- Integration of infrastructure, identity, and application delivery  
- Multi-layer system design across compute, networking, and CI/CD  

---

## Engineering Approach

All projects follow consistent engineering principles:

- Architecture-first design with clear system boundaries and responsibilities  
- Integrated security controls across identity, infrastructure, and delivery  
- Cost-aware infrastructure decisions and resource modeling  
- Structured documentation including architecture, deployment, and operations  
- Troubleshooting and operational scenarios captured as part of the implementation  

---

## Supporting Work

#### [Cloud DevOps Toolkit](https://github.com/DimitryZH/cloud-devops-toolkit)

A curated collection of supporting implementations, experiments, and reusable patterns complementing the platform projects.

Includes:

- CI/CD implementations (GitHub Actions, Cloud Build, Jenkins)  
- Multi-cloud infrastructure examples (AWS, Azure, GCP)  
- Kubernetes patterns (Ingress, Istio, Kustomize, OpenShift)  
- GitOps workflows (ArgoCD, Helm)  
- Observability setups (Prometheus, Grafana, Datadog)  
- Infrastructure modules (Terraform, Ansible)  
- Automation scripts (Python, Bash)  
