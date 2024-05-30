# Revision Questions (AWS)
AWS, which stands for Amazon Web Services, is a cloud service provider that helps in providing the services of various fields of domains through the internet with the principle of “Pay as you use”. AWS was started in 2006 with 3 types of services such as storage, computing, and messaging. After, it enhanced its network by providing all the required services based on the market trends.

> 1.  What Is AWS And Why Is It So Popular?

Amazon Web Services (AWS), is an important cloud computing platform known for its wide service offerings. Its popularity is developed through its scalability, cost-effectiveness, and global infrastructure. Businesses increased the AWS to efficiently scale operations, reduce costs, and innovate rapidly.

> 2.  Explain The Key Components Of AWS.

AWS provides the fundamental components crucial for cloud computing such as EC2 provides scalable computing capabilities, S3 offers storage for all kinds of files, RDS manages many kinds of databases, and IAM ensures secured access through addressing Authentication and Authorization. These components collectively empower the users to create and deploy various applications seamlessly.

> 3.  What Is An EC2 Instance And How Does It Work?

Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides secure, resizable compute capacity in the cloud.An EC2 instance stands for Elastic Cloud Compute service, It is a virtual server in the cloud. When we launch this, it will run the selected operating system with a specified application stack. For instance, you can deploy a web server or a database in this EC2 service. It can also be configured for specific computing needs, making it a flexible and scalable solution.

> 4. . Describe The Difference Between S3 And EBS In AWS.

S3 ( Simple Storage Service ) is an object storage service suitable for storing various data types of files that can accessed through the internet. In contrast, EBS ( Elastic Block storage ) is a block-level storage attached to EC2 instances, offering persistent and high-performance storage for applications like databases. EBS provides the raw storage hardware helpful for I/O operations where as S3 comes with pre configured file system. For understaning think of S3 as a file storage system and EBS as a hard drive.

> 5. How Does Auto Scaling Work In AWS? 

Auto Scaling is an aws service that provides dynamically adjusts, on running the number of EC2 instances based on traffic demand. For instance, during the high traffic periods, Auto Scaling adds instances , improving optimal performance as per the policies configuration. Conversely, while during low traffic, it will reduce the number of instances , optimizes the cost efficiency maintaining high availability.

> 6. How Is Data Transfer Handled In AWS?

The data transfer in AWS happens in between regions, within regions, and between the services. It is essential to consider that these data transfer comes with costs when designing the architectures. For example, transfer of the data between an EC2 instance and an S3 bucket within the same region is often free, but the transfer of data in between inter-region comes with charges.

> 7. What Is Amazon RDS, And What Database Engines Does It Support?

Amazon RDS ( Relational Database system) is a managed relational database service that deals with essential hardware infrastructure of Amazon. It supports for the various database engines such as MySQL, SQL Server, Oracle, PostgreSQL and MariaDB. RDS involves in simplifying the database administration tasks on inclusion of backups, software patching, and scaling. It helps the developers to focus on logic of the application rather than focusing on infrastructure setup and management.

> 8. What Is AWS Elastic Beanstalk, And How Does It Simplify Application Deployment?

https://www.w3schools.com/django/django_deploy_provider.php

AWS Elastic Beanstalk is a AWS managed service helps in providing simplifyed application’s deployment and management through automatically handling the infrastructure provision. It allows the developers to focus completely on writing the code. For example, you only need to upload your code for deploying web application , Elastic Beanstalk will care of the rest of underlying infrastructures provisioning of EC2 instances and load balancing.

> 9. What Is Amazon VPC And How Does It Help In Securing Your Resources?

Amazon VPC ( Virutal Private Cloud ) is an AWS service that helps the users to create isolated networks within AWS account through customizing IP address ranges and the defining their subnets. It helps in enhancing the security through controlling both the inbound and outbound of the traffic. For example, To host the web servers in public subnets and connecting to the databases placing in private subnets can be on configuring the VPC. It provides an additional layer of network security to the applications.

> 10. Describe The Use Of Amazon Route 53.

AWS Route 53 is a scalable and highly available Domain Name System (DNS) web service. It plays a crucial role in DevOps by managing domain names, routing traffic to resources like EC2 instances, load balancers, and providing health checks to ensure high availability

> 11. EC2 vs Elastic beanstalk

https://www.sitepoint.com/aws-elastic-beanstalk-vs-ec2/#:~:text=EC2%20(Elastic%20Compute%20Cloud)%20is,deployment%20and%20scaling%20of%20applications.

What are the key differences between AWS Elastic Beanstalk and EC2?

AWS Elastic Beanstalk and EC2 are both services provided by Amazon Web Services, but they serve different purposes. EC2 (Elastic Compute Cloud) is a service that provides scalable computing capacity in the AWS cloud. It is designed to make web-scale cloud computing easier for developers. On the other hand, Elastic Beanstalk is a Platform as a Service (PaaS) that simplifies the deployment and scaling of applications. It automatically handles the details of capacity provisioning, load balancing, scaling, and application health monitoring

When should I use AWS Elastic Beanstalk instead of EC2?

Elastic Beanstalk is ideal for developers who want to deploy and manage applications in the AWS Cloud but don’t want to worry about the infrastructure that runs those applications. It provides an environment to easily deploy and run applications in the language of your choice. If you want more control over the underlying infrastructure, EC2 would be a better choice.