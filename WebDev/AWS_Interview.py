# Why you use elastic ip in ec2
"""to prevent your instance's public IP from changing when it is stopped/started, allowing for consistent 
DNS records, firewall whitelisting, and rapid failover by remapping the IP to a new instance. """

# What is static ip in ec2
"""A static IP in Amazon EC2 is known as an Elastic IP (EIP) address. It is a reserved, public IPv4 address 
assigned to your AWS account that remains constant, even if you stop, start, or terminate your instance."""

# How to connect to any aws service using a python library
"""To connect to AWS services using Python, you use the official AWS SDK for Python, called Boto3"""
 
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
"""For lightweight APIs, webhook processing, image processing, or event-driven architecture, 
I would prefer Lambda because of auto-scaling and zero server management."""

# what are the ways for debugging in python at production level?
"""1. Logging: Python's built-in logging module
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

7. Gunicorn & Nginx Logs (Real Production Debugging)"""

# Basic EC2 Commands
"""Connect to EC2: ssh -i mykey.pem ec2-user@<public-ip>
Check OS details: cat /etc/os-release
Check CPU & memory: top, free -m
Check disk usage: df -h, du -sh *

Systemctl & Services:
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart gunicorn
sudo systemctl status gunicorn
sudo systemctl enable gunicorn

Logs:
journalctl -u gunicorn # service logs
journalctl -xefu gunicorn # Live logs
Nginx logs:
cat /var/log/nginx/error.log
cat /var/log/nginx/access.log"""

# Types of EC2 instance
"""General Purpose Instances:
t3 / t3a (burstable - most common in startups) (t3.medium)
t4g (ARM-based, cheaper)
m5 / m6i
Compute Optimized Instances: c5 (c5.large) / c6i/ c7g
Memory Optimized Instances: r5 (r5.large) / r6i / x1"""

# How can I make a file in S3 viewable by only one particular AWS user?
"""I would keep the S3 object private and control access using IAM policies or generate a 
pre-signed URL for that specific user. This ensures only the intended user can access the file securely.
1. Keep S3 Object Private
2. Use IAM Policy: Create IAM User -> Attach a Custom Policy
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject"],
      "Resource": "arn:aws:s3:::my-bucket/private-folder/file1.pdf"
    }
  ]
}

3. Use Pre-Signed URL in Django-Python
import boto3

s3 = boto3.client('s3')

url = s3.generate_presigned_url(
    'get_object',
    Params={
        'Bucket': 'my-bucket',
        'Key': 'private-folder/file1.pdf'
    },
    ExpiresIn=300  # 5 minutes (max limit 7 days)
)
print(url)"""

# types of load balancer in aws
""" AWS has three main load balancers:
Application Load Balancer (ALB):Web apps, REST APIs HTTP/HTTPS apps (Layer 7)
Network Load Balancer (NLB): high-performance & low latency TCP/UDP traffic (Layer 4)
Gateway Load Balancer (GWLB): Security appliances (Layer 3)"""

# What is Request Blocking at Gateway Level (Blacklisting)?
"""Request blocking at gateway level means rejecting malicious or unwanted requests at 
the reverse proxy, load balancer, or WAF before they reach the backend application. 
It improves security, reduces server load, and protects against attacks like brute force, DDoS, SQL injection, etc."""