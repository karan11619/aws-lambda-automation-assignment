# AWS Automation with Lambda & Boto3

This repository contains AWS automation assignments developed using **AWS Lambda**, **Python (Boto3)**, and various AWS services. Each assignment demonstrates how serverless computing can automate common cloud administration tasks using event-driven architectures.

---

# Technologies Used

- AWS Lambda
- Python 3.12
- Boto3
- AWS IAM
- Amazon CloudWatch
- Amazon EventBridge / EventBridge Scheduler
- Amazon SNS
- AWS Cost Explorer API
- Amazon EC2
- Amazon EBS
- Amazon S3

---

# Repository Structure

```text
.
├── Assignment-1-S3-Cleanup/
│   ├── lambda_function.py
│   ├── README.md
│   └── screenshots/
│
├── Assignment-2-EBS-Snapshot/
│   ├── lambda_function.py
│   ├── README.md
│   └── screenshots/
│
├── Assignment-3-EC2-AutoTagging/
│   ├── lambda_function.py
│   ├── README.md
│   └── screenshots/
│
├── Assignment-4-Daily-Cost-Alert/
│   ├── lambda_function.py
│   ├── README.md
│   └── screenshots/
│
└── LICENSE
```

---

# Assignments

## Assignment 1 – Automated S3 Bucket Cleanup

### Objective

Automatically delete objects older than a specified number of days from an Amazon S3 bucket using AWS Lambda and EventBridge Scheduler.

### AWS Services

- Amazon S3
- AWS Lambda
- Amazon EventBridge Scheduler
- AWS IAM
- Amazon CloudWatch

---

## Assignment 2 – Automated EBS Snapshot Management

### Objective

Automatically create EBS snapshots and remove older snapshots to optimize storage management.

### AWS Services

- Amazon EC2
- Amazon EBS
- AWS Lambda
- Amazon EventBridge Scheduler
- AWS IAM
- Amazon CloudWatch

---

## Assignment 3 – Auto Tagging EC2 Instances

### Objective

Automatically apply predefined tags to newly launched EC2 instances using EventBridge and AWS Lambda.

### AWS Services

- Amazon EC2
- AWS Lambda
- Amazon EventBridge
- AWS IAM
- Amazon CloudWatch

---

## Assignment 4 – Daily AWS Cost Alert

### Objective

Retrieve daily AWS costs using the AWS Cost Explorer API and send email notifications through Amazon SNS.

### AWS Services

- AWS Cost Explorer API
- Amazon SNS
- AWS Lambda
- Amazon EventBridge Scheduler
- Amazon CloudWatch

---

# Prerequisites

Before running these projects, ensure you have:

- An active AWS account
- IAM permissions to create AWS resources
- AWS Lambda execution roles
- Python 3.12
- Boto3
- AWS Cost Explorer enabled (for Assignment 4)
- Verified Amazon SNS email subscription (for Assignment 4)

---

# Deployment Steps

1. Create the required IAM Role.
2. Create the AWS Lambda function.
3. Upload the Python source code.
4. Configure the required environment variables (if applicable).
5. Create the EventBridge Rule or Scheduler.
6. Test the Lambda function.
7. Verify execution using Amazon CloudWatch Logs.

---

# CloudWatch Monitoring

Each assignment records execution details in Amazon CloudWatch Logs for monitoring and troubleshooting.

Typical log group:

```text
/aws/lambda/<LambdaFunctionName>
```

---

# Security Best Practices

- Follow the Principle of Least Privilege (PoLP).
- Store secrets securely instead of hardcoding them.
- Monitor Lambda execution with CloudWatch Logs.
- Use serverless services to reduce operational overhead.
- Validate IAM permissions before deployment.

---

# Learning Outcomes

After completing these assignments, you will understand:

- Serverless application development
- Event-driven automation
- AWS Lambda programming with Python
- Boto3 SDK usage
- IAM role and policy management
- EventBridge scheduling
- Amazon SNS notifications
- AWS Cost Explorer API
- CloudWatch logging and monitoring

---

# Screenshots

Each assignment contains screenshots demonstrating:

- IAM Roles
- Lambda Configuration
- EventBridge Rules/Schedulers
- CloudWatch Logs
- AWS Console Outputs
- Final Results

---

# Author

**Prabakaran P**

Lead Engineer | PHP & Laravel Developer | AWS Cloud Enthusiast

---

# License

This project is created for educational and learning purposes as part of AWS Automation with Lambda & Boto3 assignments.