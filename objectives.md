# NGINX Ingress Controller Service Level Objectives and Shared Responsibilities with Customers

Last updated: 21. Oct 2020

To supplement our [general Service Level Objectives](https://www.giantswarm.io/blog/the-radical-way-giant-swarm-handles-service-level-objectives), Giant Swarm and its customers have a shared objective to keep the NGINX Ingress Controller app up and running.

This doc clarifies what Giant Swarm and customer need to do in order to accomplish that.

In essence:

*   **Giant Swarm** (1) monitors and alerts on basic metrics, (2) provides release quality assurance, (3) makes upgrades available w/in 30 days of upstream, and (4) communicates customer-impacting changes, provides migration paths, etc. 
*   **Customer** takes care of (1) fine-grained and workload-specific monitoring, and capacity and performance management, (2) testing upgrades when jumping over multiple releases, (3) reading release notes carefully with Solution Engineers.

## Giant Swarm’s responsibility

**First, monitoring and alerting.**

In production, we monitor and alert on these basic metrics:
*   For each workload, when at least one pod was unavailable for more than 5 minutes. In addition, when the error budget’s burn rate
    *   Was in the last 10mins, higher than 1%
    *   Was in the last hour, higher than the max allowable rate
    *   Will run out in ~3 days
*   When a container crashes repeatedly.
*   When an app fails to install or upgrade. We get notified, but not paged yet.

**Second, Quality Assurance of releases to reduce likelihood of introducing regressions.**

Performance Tests
*   Setup: We start a 3-node cluster of m5.xlarge Instance Type on AWS. We use affinity to start three deployments: (1) NGINX IC app, (2) StormForger Load Testing app, and (3) Gatling Performance Testing tool.
*   Generated load
    *   Gatling is configured to hit Stormforger through NGINX IC 
    *   Generated load starts with 150 concurrent users. Over 15 seconds, load ramps up to 500 concurrent users. Each concurrent user issues 100 echo requests to send 50.000 requests in total.
*   Assertion
    *   Request success ratio (HTTP 200 response code) is >= 99.5% of the requests
    *   Throughput is more than 2000 requests per second

General Quality Assurance
*   Static Code Analysis (linting, etc.)
*   Integration Tests to ensure that the Helm chart can be deployed.
*   Functional Tests
    *   Platform Compatibility Testing, with latest platform releases across providers (AWS, Azure, and KVM)
    *   End-to-End smoke tests to make sure Ingress traffic gets routed when (1) installing a new app, and (2) upgrading an app

**Third, 30 day upgrade objective.**

We strive to upgrade all Managed Apps within 30 days of an upstream release. Not falling behind upgrades means better security, smoother upgrades, and less breaking changes. It also means the latest bug fixes and features are always made available to you.

As part of this we:
*   Retag the upstream Docker images to
    *   Scan the images for security
    *   Make the images available in tenant cluster local regions for more predictable image pulling times i.e. more predictable Pod startup times
*   Maintain a Helm chart separate from upstream, in order to
    *   Support customer-requested features not supported by upstream chart
    *   Make chart compliant with hardened security on Giant Swarm clusters
    *   Prevent being blocked by community consensus to ship infrastructure code changes

**Fourth, communication.**

*   We evaluate upstream changes and communicate to our best knowledge potential customer-impacting changes (e.g. configuration defaults changes, breaking features)
*   Provide support through Solution Engineers, with migration paths and scripts, as well as guidance to mitigate breaking changes (where possible)

The above applies only to the Optional NGINX Ingress Controller in AWS 10+, Azure 12+, and KVM 12.2.x+. (Preinstalled NGINX IC in legacy releases are supported on an as-needed basis.)

## Customer’s responsibility

_Below is generally what customers need to take care of, in order to keep our shared objective of 99.5% availability. It is possible to shift many of these to Giant Swarm, but at the expense of making more apps available to customers._

**NGINX IC-specific**
*   More fine-grained availability monitoring (e.g. non-successful HTTP responses 5xx, 4xx)

**Applies to all Managed Apps**
*   Size up, scale, and load test your deployment specific to your needs. In general, workload-specific capacity and performance management in production (auto scaling, latency, resource assignment tuning, cost efficiency).
*   Upgrades - When jumping upgrades, test on non-production environments first. We don’t test compatibility for jumping over multiple releases. e.g. v1.6.0 to v1.8.3
*   Upgrades - Plan releases and read release notes with Solution Engineers. This helps minimize negative impact of changes to your deployments that we might be unaware of
*   Customer configures and tunes the app. Giant Swarm provides sane defaults, APIs, assistance, and knowledge.