# Why you use elastic ip in ec2
"""
to prevent your instance’s public IP from changing when it is stopped/started, allowing for consistent 
DNS records, firewall whitelisting, and rapid failover by remapping the IP to a new instance. 
"""
# What is static ip in ec2
"""
A static IP in Amazon EC2 is known as an Elastic IP (EIP) address. It is a reserved, public IPv4 address 
assigned to your AWS account that remains constant, even if you stop, start, or terminate your instance.
"""
# How to connect to any aws service using a python library
"""
To connect to AWS services using Python, you use the official AWS SDK for Python, called Boto3
"""
 
# AWS CloudWatch
"""Amazon CloudWatch is a comprehensive monitoring and observability service for AWS resources and 
applications, enabling DevOps engineers and IT teams to track performance metrics, collect log files, 
and set automated alarms.
Features: 
Metrics & Dashboards, Log Management
Alarms & Automation, Event Monitoring"""


# AWS Route 53
"""Amazon Web Services Route 53 is a scalable and highly available DNS (Domain Name System) 
web service used to route end users to internet applications by translating domain names into IP addresses."""


# lambda over ec2
"""We used EC2 because our Django/FastAPI application required a long-running server process with more control 
over environment configuration, background schedulers, and persistent connections.
Lambda is great for event-driven, short-lived workloads, but our use case required full server control and predictable execution."""

# When WOULD You Choose Lambda?
"""
For lightweight APIs, webhook processing, image processing, or event-driven architecture, 
I would prefer Lambda because of auto-scaling and zero server management."""

# what are the ways for debugging in python at production level?
"""
1. Logging: Python's built-in logging module
What we log:
Request path, User ID, Exception details, SQL query time, Third-party API responses

2. Centralized Log Monitoring Tools: AWS CloudWatch Logs, Datadog
Benefits:
Search logs by request ID / user ID
Filter by error level
Analyze spikes and patterns

3. Error Tracking & Exception Monitoring: Sentry
Integrate error tracking tools like Sentry to capture unhandled exceptions with full stack traces.

4. Metrics & Monitoring: AWS CloudWatch Metrics, Prometheus + Grafana
If response time suddenly increases, we analyze metrics before checking logs.

5. Tracing & Correlation IDs:
Generate a request ID-> Pass it through headers-> Pass it through headers
Trace a single request across services

6. Reproducing Production Issues in Lower Environments:
Use production logs ->Use same data snapshot (sanitized) ->Reproduce in staging/local->Debug safely

7. Gunicorn & Nginx Logs (Real Production Debugging)
"""

